from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50,primary_key=True)
    instructer=models.ForeignKey(User,on_delete=models.CASCADE)

    # chapter_name=models.ForeignKey()


#
class StudentRegistered(models.Model):
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    student_name=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        # unique_together("course_name","student_name")
        unique_together=['course_name','student_name']


#this model done
class Chapter(models.Model):
    chapter_name=models.CharField(max_length=100)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        # unique_together("chapter_name","course_name")
        unique_together=['chapter_name',"course_name"]
    


class Completed(models.Model):
    # course_name=models.ForeignKey()
    chapter_name=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    student_name=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    
    class Meta:
        # unique_together("chapter_name","student_name")
        unique_together=['chapter_name','student_name']

