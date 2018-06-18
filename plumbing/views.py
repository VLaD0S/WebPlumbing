from django.shortcuts import render
from plumbing.models import Review, Qualification, Group, Service
from django.views import View
from django.http import HttpResponse, StreamingHttpResponse
from django.core import serializers


def home(request):
    qualifications = Qualification.objects.all()
    context = {
        "qualifications": qualifications,
    }
    #populate_reviews()
    return render(request, 'home.html', context=context)


class HomeView(View):
    def get(self, request):
        # view logic
        return render(request, 'home.html')


class QualificationView(View):

    def get(self, request):

        if request.method == 'GET':
            context = serializers.serialize("json", Qualification.objects.all(), fields=('qual'))
            return HttpResponse(context)
