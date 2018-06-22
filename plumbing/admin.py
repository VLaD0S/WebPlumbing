from django.contrib import admin
from .models import Qualification, Service, Group, Image

admin.site.register(Group)
admin.site.register(Qualification)
admin.site.register(Service)
admin.site.register(Image)

