"""TRP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from trp_api import views
from knox import views as knox_views

router = DefaultRouter()
router.register('student', views.Student_Viewsets)

urlpatterns = [
    path('admin/', admin.site.urls),#admin site
    path('viewsets/', include(router.urls)),#Students who recevied the donations from the donors(users) (pass a token)
    path('donations/', views.Donation_mixins.as_view()),#donations made by users for the sudents (pass a token)
                  #
    path('user/', views.get_user),#getting user informations by passing "username" "email" and the token
    path('login/', views.login),# user login  by passing "username" "email" and get a token
    path('register/', views.register),# user registeration  by passing "username" "email" "first_name" "last_name" and get a token
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),# user logout from the current session token  by passing "username" "email" and token of the session
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),# user logout from the all sessions token  by passing "username" "email" and token of the session

]
