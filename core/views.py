from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

from django.shortcuts import render

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def health(request):
    return HttpResponse("ok")