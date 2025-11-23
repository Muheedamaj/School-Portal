from django.db import models

class StudentRegister(models.Model):
    name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class TeacherRegister(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False) 

    def __str__(self):
        return self.name



STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]


class studentLeave(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)
    student_class = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    

    def __str__(self):
        return f"{self.name} ({self.rollno})"


