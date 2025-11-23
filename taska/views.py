from django.shortcuts import render,redirect
from .models import StudentRegister
from .forms import StudentForm
from .models import TeacherRegister
from .models import studentLeave
from .forms import TeacherForm
from .forms import StudentLeaveForm
from django.contrib.auth import authenticate,login as log,logout
from django.core.mail import send_mail


def home(request):
    return render(request,'home.html')




def student_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if StudentRegister.objects.filter(username=username).exists():
            return render(request, 'Regstudent.html', {'error': 'Username already taken!'})

        if StudentRegister.objects.filter(email=email).exists():
            return render(request, 'Regstudent.html', {'error': 'Email already exists!'})

        if password == confirm_password:
            StudentRegister(
                name=name,
                student_class=student_class,
                department=department,
                email=email,
                phone=phone,
                username=username,
                password=password
            ).save()
            return redirect('login')
        else:
            return render(request, 'Regstudent.html', {'error': 'Passwords do not match!'})

    return render(request, 'Regstudent.html')





def teacher_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if TeacherRegister.objects.filter(username=username).exists():
            return render(request, 'Regteacher.html', {'error': 'Username already taken!'})

        if TeacherRegister.objects.filter(email=email).exists():
            return render(request, 'Regteacher.html', {'error': 'Email already exists!'})

        if password == confirm_password:
            TeacherRegister(
                name=name,
                department=department,
                subject=subject,
                email=email,
                phone=phone,
                username=username,
                password=password,
                is_approved=False
            ).save()
            return redirect('login')
        else:
            return render(request, 'Regteacher.html', {'error': 'Passwords do not match!'})

    return render(request, 'Regteacher.html')





def student_leave(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        student_class = request.POST.get('student_class')
        department = request.POST.get('department')
        reason = request.POST.get('reason')
        

        # Save data to database
        studentLeave.objects.create(
            name=name,
            rollno=rollno,
            student_class=student_class,
            department=department,
            reason=reason,
         
        )

        return redirect('profile')  # redirect after success

    return render(request, 'leave.html')






def login(request):
    return render(request,'Logstudent.html')


def logint(request):
    return render(request,'Logteacher.html')


def userlog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = StudentRegister.objects.filter(username=username, password=password)

        if cr:
            user_details = cr.first()
            name = user_details.name

            request.session['name'] = name
            request.session['student_id'] = user_details.id  
            return redirect('profile')

        else:
            return render(request, 'Logstudent.html')
    else:
        return render(request, 'home.html')




def userlogt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = TeacherRegister.objects.filter(username=username, password=password).first()

        if cr:
            if not cr.is_approved:
                return render(request, 'Logteacher.html', {
                    'error': 'Your account is pending admin approval.'
                })

            request.session['name'] = cr.name
            request.session['teacher_id'] = cr.id  
            return redirect('profileteacher')

        else:
            return render(request, 'Logteacher.html')
    else:
        return render(request, 'home.html')





def profile(request):
    student_id = request.session.get('student_id')  # get logged-in student ID
    if not student_id:
        return redirect('login')  # if not logged in, redirect

    student = StudentRegister.objects.get(id=student_id)  # fetch student object
    return render(request, 'Loggedin.html', {'student': student})  # pass to template



def profileteacher(request):
    teacher_id = request.session.get('teacher_id')  # get logged-in teacher ID
    if not teacher_id:
        return redirect('login_Teacher')  # if not logged in, redirect

    teacher = TeacherRegister.objects.get(id=teacher_id)  # fetch teacher object
    return render(request, 'LoggedinTeacher.html', {'teacher': teacher})  # pass to template





def viewprofile(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = StudentRegister.objects.get(id=student_id)
    return render(request, 'viewprofile.html', {'student': student})




def viewprofileteacher(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login_Teacher')
    teacher = TeacherRegister.objects.get(id=teacher_id)
    return render(request, 'viewprofileTeacher.html', {'teacher': teacher})






def update(request, pk):
    
    student = StudentRegister.objects.get(id=pk)# Pre-fill the form with existing student data
    form = StudentForm(instance=student)

    if request.method == 'POST': # Bind POST data to the form with existing instance
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():  # <- parentheses are required
            form.save()      # Save updated data
            return redirect('profile')  # Redirect to profile page after update
    return render(request, 'Regstudent.html', {'form': form})    # Render the same registration page template






def updateteacher(request, pk):
    
    teacher = TeacherRegister.objects.get(id=pk)# Pre-fill the form with existing teacher data
    form = TeacherForm(instance=teacher)

    if request.method == 'POST': # Bind POST data to the form with existing instance
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():  # <- parentheses are required
            form.save()      # Save updated data
            return redirect('profileteacher')  # Redirect to profile page after update
    return render(request, 'Regteacher.html', {'form': form})    # Render the same registration page template





def leave(request):
    return render(request,'leave.html')


def leave_status(request):
    student_id = request.session.get('student_id')
    student = StudentRegister.objects.get(id=student_id)
    leave = studentLeave.objects.filter(name=student.name).first()
    return render(request, 'Leavestatus.html', {'student': student, 'leave': leave})




# Teacher view
def teacher_leaveview(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('logint')  # teacher login
    teacher = TeacherRegister.objects.get(id=teacher_id)
    dept = teacher.department
    leaves = studentLeave.objects.filter(department=dept).order_by('id')  # all students
    return render(request, 'leaveview.html', {'leaves': leaves, 'teacher': teacher})




def approve_leave(request, pk):
    leave = studentLeave.objects.get(id=pk)
    leave.status = "Approved"
    leave.save()
    Email=request.session['Email']
    return redirect('teacher_leaveview')  


def reject_leave(request, pk):
    leave = studentLeave.objects.get(id=pk)
    leave.status = "Rejected"
    leave.save()
    return redirect('teacher_leaveview')



def approved(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('logint')  # teacher login
    teacher = TeacherRegister.objects.get(id=teacher_id)
    dept = teacher.department
    status = "Approved"
    leaves = studentLeave.objects.filter(department=dept,status=status).order_by('id')  # all students
    return render(request, 'Approved.html', {'leaves': leaves, 'teacher': teacher})





    
def delete(request,pk):
    cr = StudentRegister.objects.get(id=pk)
    cr.delete()
    return redirect('login')




def deleteteacher(request,pk):
    cr = TeacherRegister.objects.get(id=pk)
    cr.delete()
    return redirect('logint')





def logoutuser(request):
    logout(request)
    return redirect('login')


def logoutteacher(request):
    logout(request)
    return redirect('logint')











