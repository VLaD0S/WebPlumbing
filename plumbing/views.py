from plumbing.models import review , qualification, group, service, contact, image
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import json


class HomeView(View):

    def get(self, request):
        return render(request, '_homefile.html')


class QualificationView(View):

    def get(self, request):
        jsonarr = []
        for qual in qualification.objects.all():
            jsonarr.append({"qualification": qual.qual})

        return HttpResponse(json.dumps(jsonarr))


class ServicesView(View):

    def get(self, request):
        jsonarr = []
        for gr in group.objects.all():
            servicelist = []
            for serv in service.objects.all():
                if serv.group.name == gr.name:
                    servicelist.append(serv.service)

            jsonarr.append({
                "group":gr.name,
                "services": servicelist, })
        return HttpResponse(json.dumps(jsonarr), content_type='application/json')


class ContactSave(View):

    def post(self, request):

        jsonarr = {}
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        cont = contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        try:
            cont.full_clean()
            cont.save()
            jsonarr['stat'] = "ok";

        except ValidationError as e:
            jsonarr['stat'] = "error"
            jsonarr['errors'] = e.message_dict

        return HttpResponse(json.dumps(jsonarr), content_type='application/json')


class GalleryView(View):

    def get(self, request):
        images = image.objects.all()
        return render(request, 'gallery.html', context={'images':images})


