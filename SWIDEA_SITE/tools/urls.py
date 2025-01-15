from django.urls import path
from .views import *

app_name = 'tools'

urlpatterns = [
    path('tool/', tool_list, name="tool_list"),
    path('tool/detail/<int:pk>/', tool_detail, name="tool_detail"),
    path('tool/delete/<int:pk>/', tool_delete, name="tool_delete"),
    path('tool/update/<int:pk>/', tool_update, name="tool_update"),
    path('tool/create/', tool_create, name="tool_create"),
]
