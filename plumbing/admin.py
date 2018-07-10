from django.contrib import admin
from .models import qualification, service, group, image, contact, review

admin.site.register(group)
admin.site.register(qualification)
admin.site.register(service)
admin.site.register(image)
admin.site.register(contact)
admin.site.register(review)