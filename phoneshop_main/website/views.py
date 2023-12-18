from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You are now signed in!"))
            return redirect('index')
        else:
            messages.error(request, ("Unable to sign in. Please check your details and try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.error(request, ("You have been logged out!"))
    return redirect('index')

def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Register successful. Welcome ' + username + '!'))
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                error_message = ', '.join(errors)
                if field in ['password1', 'password2']:
                    error_message += '. Password must contain at least 8 characters'
                messages.error(request, f'{field.capitalize()}: {error_message}')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, foo):
    foo = foo.replace('-', ' ')

    try:
        # look up the category
        category = Category.objects.get(name=foo)
        print('line 70')
        products = Product.objects.filter(category=category)
        print('line 72')
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.error(request, ("The category does not exist..."))
        return redirect('index')
