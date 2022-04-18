from rest_framework import serializers
from .models import Student,Donation,userInfo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class user_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=userInfo
        fields='__all__'
