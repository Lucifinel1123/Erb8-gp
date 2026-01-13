from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Company
#from django.contrib import messages

# Create your views here.
def company(request):
    if request.method=='POST':
        company_id = request.POST['company_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        company = Company(company_id=company_id, name=name, 
                        email=email, phone=phone)
        company.save()
        return redirect('companies:company', company_id = company_id)
    return HttpResponse("<h1>company</h1>")

def HR_dashboard(request):
    '''
    job_post = Listing.objects.all().filter()
    user_appliers = Apply.objects.all().filter(
        user_id = request.user.id).order_by('-contact_date')
    
    context = {"job_post": job_post, "user_appliers": user_appliers}
    '''
    return render(request, 'companies/HR_dashboard.html')

