from plumbing.models import Review, Qualification, Group, Service, Contact
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import json


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class QualificationView(View):

    def get(self, request):
        if request.method == 'GET':
            jsonarr = []
            for qual in Qualification.objects.all():
                jsonarr.append({"qualification": qual.qual})

            return HttpResponse(json.dumps(jsonarr))


class ServicesView(View):

    def get(self, request):
        jsonarr = []
        for gr in Group.objects.all():
            servicelist = []

            for serv in Service.objects.all():
                if serv.group.name == gr.name:
                    servicelist.append(serv.service)

            jsonarr.append({
                "group":gr.name,
                "services": servicelist
            })
        return HttpResponse(json.dumps(jsonarr), content_type='application/json')


class ContactSave(View):

    def post(self, request):

        jsonarr = {}
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        jsonarr['name'] = name

        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        jsonarr['errors'] = []
        try:
            contact.full_clean()
            contact.save()
            jsonarr['stat'] = "ok";

        except ValidationError:
            jsonarr['stat'] = "error"
            jsonarr['errors'].append("form isn't vaid")


        print(jsonarr)
        return HttpResponse(json.dumps(jsonarr), content_type='application/json')
