from django.contrib import admin

from trp_api.models import Donation, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Donation)