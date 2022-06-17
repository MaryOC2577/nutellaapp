import pytest
from django.urls import reverse
from django.test import Client
from nutella.models import Product, Category

@pytest.fixture
def test_data():
    cat = Category.objects.create(name="pizza")
    Product.objects.create(name="pizza1", stores="auchan", nutriscore="C", category=cat)
    Product.objects.create(name="pizza2", stores="carrefour", nutriscore="B", category=cat)
    Product.objects.create(name="pizza3", stores="leclerc", nutriscore="A", category=cat)
    Product.objects.create(name="pizza4", stores="super u", nutriscore="A", category=cat)
    Product.objects.create(name="pizza5", stores="aldi", nutriscore="D", category=cat)
    Product.objects.create(name="pizza6", stores="lidl", nutriscore="A", category=cat)
    Product.objects.create(name="pizza7", stores="lidl", nutriscore="B", category=cat)

@pytest.mark.django_db
class TestProducts():
    @pytest.mark.usefixtures("test_data")
    def test_product_substitutes(self):
        product = Product.objects.get(pk=5)
        substitutes = product.get_six_better_substitutes()
        assert substitutes.count() == 6
