""" Contains the urls of the favorite application. """

from . import views
from django.urls import path

app_name = "favorite"

urlpatterns = [
    path("", views.ShowFavorites.as_view(), name="favorites"),
    path("delete/<int:pk>/", views.DeleteFavorites.as_view(), name="delete"),
]
