from django.shortcuts import render
from plumbing.models import Review, Qualification, Group, Service
from django.views import View
from django.http import HttpResponse
from plumbing.forms import ContactForm
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