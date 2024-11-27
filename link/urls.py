from django.urls import path
from . import views

urlpatterns = [
    path('<str:link_name>', views.link_detail, name='index'),
]