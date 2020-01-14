from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Background

def index(request):

    img = Background.objects.order_by('pic')

    context = {
        'pic': img,
    }

    return render(request, 'home/index.html', context)
# Create your views here.