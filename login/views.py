""" Contains the views of the login application. """

from __future__ import print_function
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import View, TemplateView
from login.models import User, PassChange
from login.mail import send_reset_password_mail
import uuid
from datetime import datetime, timezone, timedelta


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        """Authenticate a user."""

        # Step 1 :
        email = username = request.POST["username"]
        password = request.POST["password"]

        # Step 2 :
        user = authenticate(request, email=email, username=username, password=password)

        # Step 3 :
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
        context["user"] = self.request.user
        return context


class PasswordReset(TemplateView):
    template_name = "change_password.html"


class PasswordDone(TemplateView):
    template_name = "password_done.html"

    def post(self, request):
        umail = self.request.POST.get("usermail", "")

        if umail:
            try:
                user = User.objects.get(email=umail)
                myuuid = uuid.uuid4()

            except Exception:
                pass
            else:
                PassChange.objects.create(email=umail, token=myuuid)
                send_reset_password_mail(umail, myuuid, user)
                print(f"{request.get_host()}/login/password_reset/{myuuid}")
        return render(request=request, template_name="password_done.html")


class NewPassword(TemplateView):
    template_name = "new_password.html"

    def get(self, request, **kwargs):
        # récupérer passchange équivalent au token
        passchange = PassChange.objects.get(token=kwargs.get("token"))
        print(passchange.date)
        # vérifier que le token existe et que la date est valide
        if datetime.now(timezone.utc) - passchange.date > timedelta(minutes=20):
            print("perimee")
            return render(request, "wrong_token.html")
        else:
            return render(request, "new_password.html")


class ChangePassword(TemplateView):
    template_name = "new_password.html"

    def post(self, request):
        email = request.POST.get("email")
        newpassword = request.POST.get("newpass")
        newpasswordtwo = request.POST.get("newpasstwo")
        username = User.objects.get(email=email).username
        if newpassword != newpasswordtwo:
            return render(
                request,
                "registration.html",
                {"error": "Les mots de passe de correspondent pas."},
            )

        User.objects.update(password=newpassword)
        return HttpResponse(f"Bienvenue {username} !")
