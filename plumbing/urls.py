from django.conf.urls import url
from plumbing.views import HomeView, QualificationView, ServicesView, ContactSave, GalleryView, ReviewView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', HomeView.as_view()),
    url(r'^qualifications/', QualificationView.as_view()),
    url(r'^services/', ServicesView.as_view()),
    url(r'^reviews/', ReviewView.as_view()),
    url(r'^contact/', ContactSave.as_view()),
    url(r'^gallery/', GalleryView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
