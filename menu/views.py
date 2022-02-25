from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'menu'
    }
    return render(request, 'menu/index.html', params)