from django.contrib import admin
from .models import Qualification, Service, Group, Image, Contact, Review

admin.site.register(Group)
admin.site.register(Qualification)
admin.site.register(Service)
admin.site.register(Image)
admin.site.register(Contact)
admin.site.register(Review)
