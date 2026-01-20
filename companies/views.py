from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Company
from listings.models import Listing
from applies.models import Apply
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def company(request,company_id):
    company = get_object_or_404(Company, pk = company_id)
    context = {'company':company}
    return render(request,'companies/company.html', context)

@login_required
def HR_dashboard(request):
    # Check if user is associated with a company
    try:
        company = Company.objects.get(user=request.user)
        job_posts = Listing.objects.all().filter(company = company).order_by('-publish_date')

        # Check if company info is complete
        # Essential fields: name, email, phone, industry, description
        company_info_complete = all([
            company.name,
            company.email,
            company.phone and company.phone != '00000000',
            company.industry,
            company.description
        ])
        context = {
                "company": company,
                "job_post": job_posts,
                "company_info_complete": company_info_complete
        }
        return render(request, 'companies/HR_dashboard.html', context)
    except Company.DoesNotExist:
        # User is not a company HR, silently redirect to individual dashboard
        return redirect('accounts:dashboard')

@login_required
def company_edit_info(request):
    # Check if user is associated with a company
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        # User is not a company HR, silently redirect to individual dashboard
        return redirect('accounts:dashboard')
    
    # Import industry choices from listings
    from listings.choices import industry_choices

    if request.method=='POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        industry = request.POST.get('industry', '')
        serivces = request.POST.get('serivces', '')
        description = request.POST['description']
        
        # Update company info
        company.name = name
        company.email = email
        company.phone = phone
        company.industry = industry
        company.serivces = serivces
        company.description = description
        company.save()
        
        messages.success(request, 'Company information updated successfully')
        return redirect('companies:HR_dashboard')  
    else:
        context = {
            "company": company,
            "industry_choices": industry_choices
    }
        return render(request, 'companies/company_edit_info.html', context)

@login_required
def job_post(request):
    # Check if user is associated with a company
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        # User is not a company HR, silently redirect to individual dashboard
        return redirect('accounts:dashboard')
    
    if request.method=='POST':
        title = request.POST['title']
        industry = request.POST['industry']
        budget = request.POST['budget']
        duration = request.POST['duration']
        requirement = request.POST['requirement']
        description = request.POST['description']
        
        listing = Listing.objects.create(
            title=title, 
            company=company,
            industry=industry,
            budget=budget,
            duration=duration,
            requirement=requirement, 
            description=description
        )
        listing.save()
        
        messages.success(request, 'Job posted successfully')
        return redirect('companies:HR_dashboard')
    else:
        context = {"company": company}
        return render(request,'companies/job_post.html', context)
    
@login_required
def view_candidate(request, listing_id):
    # Check if user is associated with a company
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        # User is not a company HR, silently redirect to individual dashboard
        return redirect('accounts:dashboard')
    
    # Verify that the listing belongs to the user's company
    listing = get_object_or_404(Listing, pk=listing_id, company=company)
    
    user_appliers = Apply.objects.all().filter(
        listing_id = listing_id).order_by('-apply_date')
    context = {
        "listing": listing,
        "user_appliers": user_appliers
    }
    return render(request, 'companies/view_candidate.html', context)

