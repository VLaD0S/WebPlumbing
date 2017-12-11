from django.shortcuts import render
from .tasks import populate_reviews
from plumbing.models import Review

def index(request):

    return render(request, 'index.html')
    
def about(request):   
    #populate_reviews()
    return render(request, 'about.html')


