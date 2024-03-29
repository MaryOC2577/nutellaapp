""" Contains the views of the search application. """

from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from nutella.models import Product, Favorite


class ProductResult(ListView):
    template_name = "result.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        expression = self.request.GET.get("expression", "").title()
        print("expression :", expression)
        return Product.objects.filter(name__contains=expression).order_by("id") if expression else []

    def get_context_data(self, **kwargs):
        kwargs["expression"] = self.request.GET.get("expression", "")

        return super().get_context_data(**kwargs)


class OneProduct(DetailView):
    template_name = "product.html"

    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        kwargs["substitutes"] = self.get_object().get_six_better_substitutes()
        self.request.session["product_id"] = self.get_object().id
        return super().get_context_data(**kwargs)


class Substitutes(ListView):
    template_name = "substitutes.html"

    model = Product
    context_object_name = "products"


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")


class SaveFavorites(View):

    def get(self, request, pk):
        favsave = Favorite(product=Product.objects.get(pk=pk), user=request.user)
        favsave.save()
        print('**********************')
        print('\r\n'.join('{}: {}'.format(k, v) for k, v in self.request.headers.items()), self.request.body)
        return redirect("oneproduct", self.request.session["product_id"])
