from django.contrib import admin
from .models import Qualification, Service, Group

admin.site.register(Group)
admin.site.register(Qualification)
admin.site.register(Service)