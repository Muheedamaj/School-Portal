from django import forms
from .models import StudentRegister
from .models import TeacherRegister
from .models import studentLeave

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRegister
        fields = ['name', 'student_class', 'department', 'email', 'phone', 'username', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'student_class': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }



class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherRegister
        fields = ['name', 'department','subject', 'email', 'phone', 'username', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class StudentLeaveForm(forms.ModelForm):
    class Meta:
        model = studentLeave
        fields = ['name', 'rollno', 'department', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'rollno' : forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'reason': forms.TextInput(attrs={'class':'form-control'}),
            
        }

