from rest_framework.response import Response
from rest_framework import  viewsets
from .serializer import StudentSerializer,DonationSerializer,userInfo
from .models import Student,Donation,userInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



# Create your views here.

class Student_Viewsets(viewsets.ModelViewSet): 
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Donation_mixins(ListCreateAPIView,):
    permission_classes = (IsAuthenticated,)
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def list(self,request):
        queryset = self.get_queryset()
        data =[]
        for obj in queryset:
            donation_id = obj.id
            donor=obj.donor
            donor_name=donor.__class__.objects.get(id=donor.id)
            amount = obj.donation_amount
            student = obj.student
            student_id=student
            date = obj.donation_time
            field = {
                
                "id":donation_id,
                "donor": donor_name.username,
                "donation_amount":amount,
                "student": student_id.id,
                "date":date,
            }
            data.append(field)
        return Response(data)

############## Registration , Login & getting account informations ########################

@api_view(['POST'])
def register(request):
    usre_name = request.data['username']
    password = request.data['password']
    fName = request.data['fristName']
    lName = request.data['lastName']
    email = request.data['email']
    user = User.objects.create_user(username=usre_name, password=password)

    if user is not None:
        user.save()
    info_user = userInfo(by_user=user,
                         fName=fName, lName=lName,
                         email=email,)
    if info_user:
        info_user.save()
    Token.objects.create(user=user)

    return Response(request.data)

@api_view(['GET'])
def get_user(request):
    usre_name = request.data['username']
    password = request.data['password']
    user = authenticate(username=usre_name, password=password)
    if user is not None:
        currentUser = User.objects.get(username=user)
        token_ob = Token.objects.get(user_id=currentUser)
        data = {
            "username":usre_name,
            "token": token_ob.key
        }
    else:
        data = {
            "details": "user or password is wrong"
        }






