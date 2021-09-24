from django.contrib import admin
from django.urls import path
from eLearn import views

urlpatterns = [
    path("",views.index,name = 'home'),
    path("signup",views.handleSignup,name = 'handleSignup'),
    path("course_frontend",views.course_frontend,name = 'course_frontend'),
    path("course_backend",views.course_backend,name = 'course_backend'),
    path("course_database",views.course_database,name = 'course_database'),
    path("login",views.handleLogin,name = 'handleLogin'),
    path("logout",views.handleLogout,name = 'handleLogout'),
    path("contact",views.handleContact,name="handleContact") 
]