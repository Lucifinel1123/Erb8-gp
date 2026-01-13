from django.shortcuts import render
from listings.models import Listing
from .models import Type
from listings.choices import district_choices, room_choices, rooms_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings": listings,
               "title_choices": title_choices,
               "budget_choices": budget_choices,
               "job_type_choices": job_type_choices}
    return render(request,'pages/index.html', context)

def about (request):
    titles = Title.objects.order_by("-post_date")[:3]
    # mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
    context = {"titles": title, "budgets": budget, "job_types":job_type}
    return render(request,'pages/about.html', context)

def about(request):
    #companies = Company.objects.order_by("-create_date")[:3]
    #context = {"companies": companies,}
    return render(request,'pages/about.html')