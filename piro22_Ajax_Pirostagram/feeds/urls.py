from django.urls import path
from .views import *

app_name = "feeds"

urlpatterns = [
    path('', my_page, name='my_page'),
]