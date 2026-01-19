from django.shortcuts import render
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-publish_date').filter(is_active=True)[:3]
    context = {"listings": listings}
    return render(request,'pages/index.html', context)

def about (request):
    return render(request,'pages/about.html')
