from django.shortcuts import render
#from listings.models import Listing
from companies.models import Company

def index(request):
    #listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #context = {"listings": listings,}
    return render(request,'pages/index.html')

def about(request):
    #companies = Company.objects.order_by("-create_date")[:3]
    #context = {"companies": companies,}
    return render(request,'pages/about.html')