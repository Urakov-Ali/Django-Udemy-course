from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', indexView, name = 'index'),
    path('thanks', thanks_view, name = 'thanks_page')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)