from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):


    context = {
        'pic': 'img',
    }

    return render(request, 'about/index.html', context)
# Create your views here.