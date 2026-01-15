from django.shortcuts import render, HttpResponse

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
    return render(request, 'listings/listings.html')

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

def apply(request):
    return render(request,'listings/apply.html')