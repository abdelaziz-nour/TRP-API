from numpy import double
from rest_framework.response import Response
from rest_framework import  viewsets
from .serializer import RegisterSerializer, StudentSerializer,DonationSerializer
from .models import Student,Donation,userInfo
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BaseAuthentication



# Create your views here.

############################# simple APIs ########################################
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
    def post(self, request, *args, **kwargs):
        current_user= User.objects.get(id=request.user.id)
        donationAmount=request.data["donation_amout"],
        student1 = Student.objects.get(id=request.data["studentID"])
        print(current_user,student1,double(donationAmount))
        donation = Donation(donor=current_user,donation_amount=double(donationAmount),student=student1)
        if donation:
            donation.save()
            return Response("Donation done successfully")
        return Response("Donation done unsuccessfully")

############## Registration  & getting account informations ########################
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([AllowAny])
@api_view(['post'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = User.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            )
        if user is not None:
                user.save()
        info_user = userInfo(user=user,fName=request.data["first_name"],lName=request.data["last_name"],email=request.data["email"])
        if info_user:
            info_user.save()
            token =Token.objects.create(user=user)

        return Response(token.key)

#@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
#@permission_classes([AllowAny])
#@api_view(['POST'])
#def get_token(request):
#    usre_name = request.data['username']
#    password = request.data['password']
#    user = authenticate(username=usre_name, password=password)
#    if user is not None:
#        token = Token.objects.get(user_id=user)
#        return Response(token.key)
#    else :
#       return Response('Incorrect username or password')


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    usre_name = request.data['username']
    password = request.data['password']
    user = authenticate(username=usre_name, password=password)
    if user is not None:
        print(user)
        info= userInfo.objects.get(user_id=user.id)
        return Response({
            'username':info.user.username,
            'fname':info.fName,
            'lname':info.lName,
            'email':info.email
        })


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_user_donations(request):
    user= User.objects.get(id=request.user.id)
    if user is not None:
        mydonations = Donation.objects.filter(donor=user.id)
        data =[]
        for x in mydonations:
            field = {
                "donation_amount": x.donation_amount,
                "student":x.student.id,
                "student_semester": x.student.student_semester,
                "donation_time": x.donation_time,
            }
            data.append(field)
        return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_student_donations(request):
    studentid=request.data['id']
    if studentid is not None:
        mydonations = Donation.objects.filter(student=studentid)
        data =[]
        for x in mydonations:
            field = {
                "donation_amount": x.donation_amount,
                "donation_time": x.donation_time,
            }
            data.append(field)
        return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    user= User.objects.get(id=request.user.id)
    return Response(user.username) 




