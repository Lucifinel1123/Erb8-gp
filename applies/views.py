from django.shortcuts import render, HttpResponse

# Create your views here.
def applies(request):
    return HttpResponse("<h1>applied</h1>")