from django.contrib import admin
from trp_api.models import Donation, Student, userInfo

# Register your models here.
admin.site.register(Student)
admin.site.register(Donation)
admin.site.register(userInfo)
