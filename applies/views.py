from django.shortcuts import render,redirect, get_object_or_404
from .models import Apply
from django.contrib import messages

# Create your views here.
def apply(request):
    if request.method=='POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            has_applied = Apply.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_applied:
                messages.error(request, 'You have already apply this job')
                return redirect('listings:listing', listing_id=listing_id)
        apply = Apply(listing=listing, listing_id=listing_id, name=name, 
                        email=email, phone=phone, message=message, user_id=user_id)
        apply.save()
        messages.success(request, 'Your request has been submitted, the company will get back to you soon.')
        return redirect('listings:listing', listing_id=listing_id)