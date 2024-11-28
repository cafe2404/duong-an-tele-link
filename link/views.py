from django.shortcuts import render
from .models import Link
# Create your views here.
def link_detail(request, link_name):
    link = Link.objects.get(name=link_name)
    return render(request, 'link_detail.html', {'link': link})
def link_list(request):
    links = Link.objects.all()
    return render(request, 'links.html', {'links': links})