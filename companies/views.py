from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Company
from .form import CompanyInfo, Job_post
#from django.contrib import messages

# Create your views here.
def company(request, company_id):
    company = get_object_or_404(Company, pk = company_id)
    context = {'company': company}
    return render(request,'companies/company.html', context)


def HR_dashboard(request, company_id):
    '''
    job_post = Listing.objects.all().filter()
    user_appliers = Apply.objects.all().filter(
        user_id = request.user.id).order_by('-apply_date')
    context = {"job_post": job_post, "user_appliers": user_appliers}
    '''
    company = get_object_or_404(Company, pk = company_id)
    context = {
        'company': company,
    }
    return render(request, 'companies/HR_dashboard.html', context)

def company_edit_info(request, company_id):
    company = get_object_or_404(Company, pk = company_id)
    if request.method == "POST":    
        form = CompanyInfo(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('companies:HR_dashboard', company_id)
    else:
        form = CompanyInfo(instance = company)
    context = {
        "company": company,
        "form": form,
    }
    return render (request, "companies/company_edit_info.html", context)


def job_post(request, company_id):
    company = get_object_or_404(Company, pk = company_id)
    if request.method == "POST":    
        form = Job_post(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('companies:HR_dashboard', company_id)
    else:
        form = Job_post(instance = company)
    context = {
        "company": company,
        "form": form,       
    }
    return render (request, "companies/job_post.html", context)
