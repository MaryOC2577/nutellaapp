""" Search model. """

from django.views.generic import ListView
from nutella.models import Product


class SearchProduct(ListView):
    model = Product
    context_object_name = "products"
