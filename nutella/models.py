""" Database models. """

from django.db import models
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    image = models.URLField(default="")
    nutrition = models.URLField(default="")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def get_six_better_substitutes(self):

        unavaillable_substitutes = list(
            set([favorite.product.id for favorite in Favorite.objects.all()])
        )

        # retourner les 6 produits avec le meilleur nutriscore possible
        return Product.objects.filter(category=self.category, nutriscore__lte=self.nutriscore).exclude(pk=self.id).order_by("nutriscore")[:6]  

class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
