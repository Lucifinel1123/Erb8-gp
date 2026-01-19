from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Company
from listings.models import Listing
from applies.models import Apply
#from .forms import CompanyInfo, Job_post
#from django.shortcuts import login_required
#from django.contrib import messages

# Create your views here.
def company(request,company_id):
    company = get_object_or_404(Company, pk = company_id)
    context = {'company':company}
    return render(request,'companies/company.html', context)


def HR_dashboard(request):
    try:
        company = get_object_or_404(Company, user=request.user.id)
        job_posts = Listing.objects.all().filter(company = company).order_by('-publish_date')
        context = {"job_post": job_posts}
        return render(request, 'companies/HR_dashboard.html', context)
    except:
        return render(request, 'companies/HR_dashboard.html')

#@login_required
def company_edit_info(request):
    if request.method=='POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        industry = request.POST['industry']
        serivces = request.POST['serivces']
        description = request.POST['description']
        company = Company(user_id=user_id, name=name, 
                        email=email, phone=phone, industry=industry,
                        serivces=serivces, description=description)
        company.save()
        return render(request, 'companies/HR_dashboard.html')  
    else:
        return render(request, 'companies/company_edit_info.html')

def job_post(request):
    if request.method=='POST':
        user_id = request.POST['user_id']
        company = get_object_or_404(Company, user_id=user_id)
        title = request.POST['title']
        industry = request.POST['industry']
        budget = request.POST['budget']
        duration = request.POST['duration']
        requirement = request.POST['requirement']
        description = request.POST['description']
        listing = Listing(title=title, company=company,
                        industry=industry, budget=budget, duration=duration,
                        requirement=requirement, description=description)
        listing.save()
        context = {"company": company}
        return render(request, 'companies/HR_dashboard.html',context)
    else:
        return render(request,'companies/job_post.html')
    

def view_candidate(request, listing_id):
    listing_id = request.POST['listing_id']
    user_appliers = Apply.objects.all().filter(
        listing_id = listing_id).order_by('-apply_date')
    context = {"user_appliers":user_appliers}
    return render(request, 'companies/view_candidate.html',context)
