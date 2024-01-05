from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout    #authenticate is letirly to do the loggin in proccess
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request,'about.html', {})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # authinticate is to take this and pass it to backend
        if user is not None:
            login(request, user)
            messages.success(request, ("Logged in!"))
            return redirect('core:index')
        else:
            messages.success(request, ("Error"))
            return redirect('core:login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out!"))
    return redirect ('core:index')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid(): #if it got filled correctly
            form.save() # save the signup form to the users list ?
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #we log in the user right after register is successful and deliver a reporting alert 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered!"))
            return redirect('core:index')
        else:
            messages.success(request, ("Error Registering!"))
            return redirect('core:register')
    else:
        return render(request, 'register.html', {'forms': form})