from django.shortcuts import render, redirect
from accounts.forms import LogInForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def accounts_login(request):
    if request.method =="POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request,
                username=username,
                password=password)

            if user is not None:
                login(request, user,)
                return redirect("list_projects")
    else:
        form = LogInForm()
    context = {
        "form": form
    }

    return render(request, "accounts/login.html", context)

def accounts_logout(request):
    logout(request)
    return redirect("login")
