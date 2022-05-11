from django.db import models
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
    donation_time=models.DateTimeField(auto_now=True,)
    def __str__(self,):
        return str(self.id)

class userInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fName=models.CharField(max_length=25,blank=False,null=False)
    lName=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(blank=True,null=True,)
    def __str__(self,):
        return str(self.user.username)