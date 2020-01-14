from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Image, Background

def index(request):
    image = Image.objects.order_by('pic')
    background = Background.objects.order_by('pic')

    context = {
        'img': image,
        'bg': background
    }
    return render(request, 'store/index.html', context)
# Create your views here.
