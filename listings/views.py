from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Listing
from .choices import industry_choices, budget_choices, duration_choices
from django.db.models import Q
from companies.models import Company
from django.contrib import messages  # Added import for messages

# Create your views here.

def listings(request):
    listings = Listing.objects.filter(is_active=True)
    context = {
        "listings": listings
    }
    return render(request, 'listings/listings.html', context)

# def listing(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)
#     context = {"listing": listing}
#     return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-publish_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(title__icontains=keywords)|
                Q(company__name__icontains=keywords)|
                Q(description__icontains=keywords)|
                Q(requirement__icontains=keywords)
                )
    if 'industry' in request.GET:
        industry = request.GET['industry']
        if industry:
            queryset_list = queryset_list.filter(
                Q(industry__iexact=industry)
            )
    if 'budget' in request.GET:
        budget = request.GET['budget']
        if budget:
            queryset_list = queryset_list.filter(
                Q(budget__iexact=budget)
            )
    if 'duration' in request.GET:
        duration = request.GET['duration']
        if duration:
            queryset_list = queryset_list.filter(
                Q(duration__iexact=duration)
            )
    if 'publish_date' in request.GET:
        publish_date = request.GET['publish_date']
        if publish_date:
            queryset_list = queryset_list.filter(
                Q(publish_date__gte=publish_date)
            )
    context = {
        "listings": queryset_list,
        "values": request.GET,
        "industry_choices": industry_choices,
        "budget_choices": budget_choices,
        "duration_choices": duration_choices,
            }
    return render(request, 'listings/search.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    company = Company.objects.all()

    # Check if current user is a company HR
    is_company_hr = False
    user_company = None
    if request.user.is_authenticated:
        try:
            user_company = Company.objects.get(user=request.user)
            is_company_hr = True
        except Company.DoesNotExist:
            pass

    # Check if current user is the company HR who posted this listing
    is_own_company_listing = False
    if is_company_hr and user_company:
        is_own_company_listing = (listing.company == user_company)

    # Handle POST request for editing job (from modal)
    if request.method == 'POST' and is_own_company_listing:
        # Update the job listing
        listing.title = request.POST.get('title', listing.title)
        listing.industry = request.POST.get('industry', listing.industry)
        listing.budget = request.POST.get('budget', listing.budget)
        listing.duration = request.POST.get('duration', listing.duration)
        listing.requirement = request.POST.get('requirement', listing.requirement)
        listing.description = request.POST.get('description', listing.description)
        listing.save()

        # Add success message
        messages.success(request, 'Job updated successfully!')

        # Redirect back to same page (traditional form submit)
        return redirect('listings:listing', listing_id=listing_id)
    
    context = {
        "listing": listing,
        "company": company,
        "is_company_hr": is_company_hr,
        "is_own_company_listing": is_own_company_listing,
        "industry_choices": industry_choices,
        "budget_choices": budget_choices,
        "duration_choices": duration_choices,
    }
    return render(request, 'listings/listing.html', context)

def apply(request):
    context = {
    }
    return render(request, 'listings/apply.html', context)
    # return HttpResponse("<h1>apply</h1>")
