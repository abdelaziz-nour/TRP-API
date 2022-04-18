from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Student(models.Model):
    student_semester = models.IntegerField()
    student_education_dues = models.IntegerField()
    student_details = models.TextField(max_length=1000)
    def __str__(self):
        return str(self.id)


class Donation(models.Model):
    donor = models.ForeignKey(User, related_name='donation', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='donation', on_delete=models.CASCADE)
    donation_amount = models.IntegerField()
    donation_time=models.DateTimeField('%Y-%m-%d ||%H:%M:%S',auto_now=True,)

class userInfo(models.Model):
    by_user=models.OneToOneField(User,on_delete=models.CASCADE)
    fName=models.CharField(max_length=25,blank=False,null=False)
    lName=models.CharField(max_length=25,blank=False,null=False)
    education=models.TextField(max_length=100,blank=False,null=False)
    email=models.EmailField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)