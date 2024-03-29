""" Nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from login.views import registration


class Home(TemplateView):
    template_name = "index.html"


class Legal(TemplateView):
    template_name = "legal.html"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("login/", include("login.urls")),
    path("registration/", registration, name="registration"),
    path("search/", include("search.urls")),
    path("favorites/", include("favorite.urls")),
    path("legal/", Legal.as_view(), name="legal")
]
