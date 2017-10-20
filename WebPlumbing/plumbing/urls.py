from django.conf.urls import url
from plumbing import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.about, name='about'),
    ]
