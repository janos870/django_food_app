from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def register(requvest):
    if requvest.method == 'POST':
        form = RegisterForm(requvest.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requvest, f"Wellcome {username}, your account is created!")
            return redirect('login')
    else:
        form = RegisterForm()   
    return render(requvest, 'users/register.html', {'form':form})

@login_required
def profilepage(requvest):
    return render(requvest, "users/profile.html")


