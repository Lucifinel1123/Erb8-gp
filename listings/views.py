from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Listing
from .choices import industry_choices, budget_choices
from django.db.models import Q

# Create your views here.
# def listings(request):
    # listings = Listing.objects.filter(is_published=True)
    # paginator = Paginator(listings, 3)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)
    # context = {"listings": paged_listings}
    # return render(request, 'listings/listings.html', 
                #   context
                # )
    # return HttpResponse("<h1>about</h1>")

def listings(request):
    listings = Listing.objects.filter(is_active=True)
    context = {
        "listings": listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
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
                Q(budget__gte=budget)
            )
    if 'duration' in request.GET:
        duration = request.GET['duration']
        if duration:
            queryset_list = queryset_list.filter(
                Q(duration__lte=duration)
            )
    if 'publish_date' in request.GET:
        publish_date = request.GET['publish_date']
        if publish_date:
            queryset_list = queryset_list.filter(
                Q(publish_date__gte=publish_date)
            )

    context = {
        'listings': queryset_list,
        'industry_choices': industry_choices,
        'budget_choices': budget_choices,
    }

    return render(request, 'listings/search.html', context)