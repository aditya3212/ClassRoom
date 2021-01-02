from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include("student.urls")),
    path('',index),
    path('register',register),
    path('login',user_login),
    path('logout',user_logout),
    path('home',home_view),
    path('courseAdd',courseAdd),
    path('enrollStudent',enrollStudent),
    path('completedChapter',completedChapter),
    path('addChapter',addChapter)
]