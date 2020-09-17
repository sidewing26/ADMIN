from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'indec.html')

def detail(request, pk):

    return render(request, 'detail.html')