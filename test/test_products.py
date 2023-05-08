import pytest
from nutella.models import Product, Category, Favorite
from login.models import User


@pytest.fixture
def test_data():
    cat = Category.objects.create(name="pizza")
    fake_user = User.objects.create(username="test")
    fake_product = Product.objects.create(
        name="pizza1", stores="auchan", nutriscore="E", category=cat
    )
    Favorite.objects.create(product=fake_product, user=fake_user)
    Product.objects.create(
        name="pizza2", stores="carrefour", nutriscore="A", category=cat
    )
    Product.objects.create(
        name="pizza3", stores="leclerc", nutriscore="A", category=cat
    )
    Product.objects.create(
        name="pizza4", stores="super u", nutriscore="A", category=cat
    )
    Product.objects.create(name="pizza5", stores="aldi", nutriscore="A", category=cat)
    Product.objects.create(name="pizza6", stores="lidl", nutriscore="A", category=cat)
    Product.objects.create(name="pizza7", stores="lidl", nutriscore="B", category=cat)
    Product.objects.create(name="pizza8", stores="auchan", nutriscore="A", category=cat)
    Product.objects.create(
        name="pizza9", stores="leclerc", nutriscore="B", category=cat
    )


@pytest.mark.django_db
class TestProducts:
    @pytest.mark.usefixtures("test_data")
    def test_product_substitutes(self):
        product = Product.objects.get(pk=1)
        substitutes = product.get_six_better_substitutes()
        assert substitutes.count() == 6
