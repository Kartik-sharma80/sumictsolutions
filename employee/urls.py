from django.contrib import admin
from django.urls import path
from employee.views import *
from . import views

urlpatterns = [
    path('',index),
    path('contact', views.contact, name='contact.html'),
    path('about', views.about, name='about.html'),
    path('career', views.career, name='career.html'),
    path('registration',registration),
    path('emp_login/',emp_login),
    path('emp_home',emp_home),
    path('logout',Logout),
    path('profile',profile),
    path('myexperience',myexperience,name='myexperience'),
    path('edit_myexperience',edit_myexperience,name='edit_myexperience'),
    path('myeducation',myeducation,name='myeducation'),
    path('edit_myeducation',edit_myeducation,name='edit_myeducation'),
    path('change_password',change_password,name='change_password'),
    path('admin_login',admin_login,name='admin_login'),
    path('admin_home',admin_home,name='admin_home'),
    path('change_passwordadmin',change_passwordadmin,name='change_passwordadmin'),
    path('all_employee',all_employee, name='all_employee'),
    path('delete_employee/<int:pid>',delete_employee, name='delete_employee'),
    path('edit_profile/<int:pid>',edit_profile, name='edit_profile'),
    path('edit_education/<int:pid>',edit_education, name='edit_education'),
    path('edit_experience/<int:pid>',edit_experience, name='edit_experience'),
    path('all_query', all_query, name='all_query'),
    path('delete_query/<int:pid>', delete_query, name='delete_query'),
    path('all_career_application', all_career_application, name='all_career_application'),
    path('delete_career_application/<int:pid>', delete_career_application, name='delete_career_application'),
]