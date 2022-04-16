from rest_framework.response import Response
from rest_framework import  viewsets
from .serializer import StudentSerializer,DonationSerializer,RegisterSerializer
from .models import Student,Donation
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

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
def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })

@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({})






