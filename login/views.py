from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import View, TemplateView
from login.models import User


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        """Authenticate a user."""

        # Etape 1 :
        email = username = request.POST["username"]
        password = request.POST["password"]

        # Etape 2 :
        user = authenticate(request, email=email, username=username, password=password)

        # Etape 3 :
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
            return redirect("account")
        
        else:
            messages.add_message(
                request, messages.ERROR, "Les champs renseignés sont invalides."
            )
            return render(request, "login.html")


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous êtes déconnecté !")
    return redirect("home")


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(
                request,
                "registration.html",
                {"error": "Les mots de passe de correspondent pas."},
            )

        User.objects.create_user(username=username, email=email, password=password1)
        return HttpResponse(f"Bienvenue {username} !")

    return render(request, "registration.html")


class MyAccount(TemplateView):
    template_name = "account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context