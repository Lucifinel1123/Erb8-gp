from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Company
from .forms import CompanyInfo, Job_post
#from django.contrib import messages

# Create your views here.
def company(request,company_id):
    company = get_object_or_404(Company, pk = company_id)
    context = {'company':company}
    return render(request,'companies/company.html', context)


def HR_dashboard(request):
    '''
    job_post = Listing.objects.all().filter()
    user_appliers = Apply.objects.all().filter(
        user_id = request.user.id).order_by('-apply_date')
    context = {"job_post": job_post, "user_appliers": user_appliers}'''
    return render(request, 'companies/HR_dashboard.html')

def company_edit_info(request,company_id):
    company = get_object_or_404(Company, pk = company_id)
    if request.method == "POST":    
        form = CompanyInfo(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('companies:HR_dashboard')
    else:
        form = CompanyInfo(instance = company)
    return render (request, "company_edit_info.html", {"form":form, "company":company})


def job_post(request,company_id):
    company = get_object_or_404(Company, pk = company_id)
    if request.method == "POST":    
        form = Job_post(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('companies:HR_dashboard')
    else:
        form = Job_post(instance = company)
    return render (request, "job_post.html", {"form":form, "company":company})
