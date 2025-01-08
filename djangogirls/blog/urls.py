from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    # 127.0.0.1:8000/ 접속 시 views.post_list를 보여줌
]
