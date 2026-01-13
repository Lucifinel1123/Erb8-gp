from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .forms import NormalUserRegisterForm, HRUserRegisterForm
from .models import Company, Profile
from contacts.models import Contact


def register(request):
    if request.method == "POST":
        account_type = request.POST.get("account_type", "user")  # 'user' or 'company'
        if account_type == "company":
            form = HRUserRegisterForm(request.POST)
            role = "HR"
        else:
            form = NormalUserRegisterForm(request.POST)
            role = "NORMAL"

        if form.is_valid():
            # 1) Create user
            user = form.save()

            company = None
            if role == "HR":
                company_name = form.cleaned_data.get("company_name")
                company_address = form.cleaned_data.get("company_address", "")
                company, _ = Company.objects.get_or_create(
                    name=company_name,
                    defaults={"address": company_address},
                )

            # 2) Create profile
            Profile.objects.create(user=user, role=role, company=company)

            messages.success(request, "You are now registered and can log in.")
            return redirect("accounts:login")
        # If invalid, fall through to render form with errors
    else:
        form = NormalUserRegisterForm()
        account_type = "user"

    context = {
        "form": form,
        "account_type": account_type,
    }
    return render(request, "accounts/register.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, "accounts/login.html")


def logout_view(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out.")
        return redirect("pages:index")


@login_required
def dashboard(request):
    user_contacts = Contact.objects.filter(user_id=request.user.id).order_by("-contact_date")
    context = {"contacts": user_contacts}
    return render(request, "accounts/dashboard.html", context)
