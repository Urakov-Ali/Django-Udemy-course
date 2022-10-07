from django.urls import path
from .views import *

urlpatterns = [
    path('', home_View, name='home'),
    path('generated_password/', pass_View, name='password'),
]