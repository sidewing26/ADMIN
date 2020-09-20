from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    celebrity = Celebrity.objects.all()

    return render(request, 'index.html', {'celebrity':celebrity})

def detail(request, pk):
    celebrity = get_object_or_404(Celebrity, pk=pk)

    visitor = celebrity.visitor

    return render(request, 'detail.html', {'celebrity':celebrity})