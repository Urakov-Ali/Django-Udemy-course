from unicodedata import name
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blogView, name='all_blog'),
    path('<int:blog_id>', blogDetailView, name='blog_detail')
]