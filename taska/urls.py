from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),                 
    path('student_register/', views.student_register, name='student_register'),
    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('login/',views.login,name='login'),
    path('login_Teacher/',views.logint,name='login_Teacher'),
    path('userlog/',views.userlog,name='userlog'),
    path('userlogTeacher/',views.userlogt,name='userlogTeacher'),
    path('profile/',views.profile,name='profile'),
    path('profileteacher/',views.profileteacher,name='profileteacher'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('viewprofileTeacher/',views.viewprofileteacher,name='viewprofileTeacher'),
    path('update/<str:pk>',views.update,name='update'),
    path('updateteacher/<str:pk>',views.updateteacher,name='updateteacher'),
    path('leave/',views.student_leave,name='leave'),
    path('teacher_leaveview',views.teacher_leaveview,name='teacher_leaveview'),
    path('teacher_leaveview/<int:pk>/approve/', views.approve_leave, name='approve_leave'),
    path('teacher_leaveview/<int:pk>/reject/', views.reject_leave, name='reject_leave'),
    path('leaveStatus/',views.leave_status,name='leaveStatus'),
    path('approved/',views.approved,name='approved'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('deleteteacher/<str:pk>',views.deleteteacher,name='deleteteacher'),
    path('logout/',views.logoutuser,name='logout') ,
    path('logoutteacher/',views.logoutteacher,name='logoutteacher') 
]

