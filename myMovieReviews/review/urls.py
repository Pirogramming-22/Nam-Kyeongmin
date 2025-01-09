from django.urls import path
from .views import *

app_name = 'review'

urlpatterns = [
    # list
    path('review/', review_list, name='review_list'),
    
    # detail
    path('review/<int:pk>/', review_detail, name="review_detail"),
    
    # create
    path('review/create/', review_create, name="review_create"),
    
    # update
    path('review/<int:pk>/update/', review_update, name="review_update"),
    
    # delete
    path('review/<int:pk>/delete/', review_delete, name="review_delete"),
]