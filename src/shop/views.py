from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from shop.models import Product, Order


def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {"products": products})


# Partie Authentification
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)

        except IntegrityError:
            error_message = "Ce nom d'utilisateur est déjà pris. Veuillez choisir un autre nom d'utilisateur."
            return render(request, "shop/signup.html", {'error_message': error_message})

    return render(request, "shop/signup.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        try:
            if user:
                login(request, user)
                return redirect('home')
            else:
                raise ValueError("Nom d'utilisateur ou mot de passe incorrect.")
        except ValueError as e:
            error_message = str(e)
            return render(request, "shop/login.html", {'error_message': error_message})

    return render(request, "shop/login.html")


def logout_user(request):
    logout(request)
    return redirect('home')
