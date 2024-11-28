from django.urls import path
from . import views

urlpatterns = [
    path('<link_name>', views.link_detail, name='link_detail'),
    path('', views.link_list, name='link_list'),
]