from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    # age=forms.IntegerField()

    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']

# class GeeksForm(forms.ModelForm): 
# 	# specify the name of model to use 
# 	class Meta: 
# 		model = GeeksModel 
# 		fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"
    

class StudentRegisteredForm(forms.ModelForm):
    class Meta:
        model=StudentRegistered
        fields="__all__"


class ChapterForm(forms.ModelForm):
    class Meta:
        model=Chapter
        fields="__all__"

class CompletedForm(forms.ModelForm):
    class Meta:
        model=Completed
        fields="__all__"

