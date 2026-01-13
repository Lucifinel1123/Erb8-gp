from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
#from applys.models import Apply

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You logged in")
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Invalid user")
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html') 

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('pages:index')

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Exists. ")
                return redirect("accounts:register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email registed. ")
                    return redirect("accounts:register")
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name = last_name)
                    user.save()
                    messages.success(request, "Registered!You can log in. ")
                    return redirect("accounts:login")
        else:
            messages.error(request, "Password do not match. ")
            return redirect("accounts:register")
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    user_apply = Apply.objects.filter(
        user_id = request.user.id).order_by('-apply_date')
    context = {"applys": user_apply}
    return render(request,'accounts/dashboard.html', context)