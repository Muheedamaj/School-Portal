from django.contrib import admin
from .models import StudentRegister
from .models import TeacherRegister
from .models import studentLeave

# Register your models here.
admin.site.register(StudentRegister)
admin.site.register(TeacherRegister)
admin.site.register(studentLeave)