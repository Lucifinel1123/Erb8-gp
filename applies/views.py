from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Apply
from listings.models import Listing

# Create your views here.
@login_required(login_url='accounts:login')
def apply(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method=='POST':
        listing_id = request.POST.get('listing_id')
        name = request.POST.get('name', '')
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '').strip()

        cv_file = request.FILES.get('cv')
        
        if Apply.objects.filter(listing=listing, user=request.user).exists():
            messages.error(request, 'You have already applied for this job')
            return redirect('listings:listing', listing_id=listing_id)
        
        apply = Apply(listing=listing, listing_id=listing_id, name=name, cv=cv_file,
                        email=email, phone=phone, message=message, user=request.user)
        apply.save()
        messages.success(request, 'Apply success')
        return render(request, 'accounts:dashboard')
        # return redirect('listings:listing', listing_id=listing_id)
    else:
        context = {"listing": listing}
        return render(request, 'applies/apply.html', context)