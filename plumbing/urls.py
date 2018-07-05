from django.conf.urls import url
from plumbing import views
from plumbing.views import HomeView, QualificationView, ServicesView, ContactSave

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', HomeView.as_view()),
    url(r'^qualifications/', QualificationView.as_view()),
    url(r'^services/', ServicesView.as_view()),
    url(r'^contact/', ContactSave.as_view()),
    ]
