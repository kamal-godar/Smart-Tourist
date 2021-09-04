from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def planmytrip(request):
    return render(request, 'planmytrip.html')

def explore(request):
    return render(request, 'explore.html')
    