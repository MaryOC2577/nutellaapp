from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from nutella.models import Favorite
from login.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ShowFavorites(LoginRequiredMixin, ListView):
    template_name = "favorite/favorite_list.html"
    model = Favorite
    context_object_name = "favorites"

    def get_queryset(self):
        return Favorite.objects.filter(user__pk=self.request.user.id)


class DeleteFavorites(View):
    def post(self, request, pk):
        favorite = Favorite.objects.get(pk=pk)
        if self.request.user.id == favorite.user.id:
            favorite.delete()
        return redirect("favorite:favorites")
