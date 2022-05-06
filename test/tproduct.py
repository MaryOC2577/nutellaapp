import pytest
from nutella.models import Product

@pytest.fixture
def create_products():
    tproducts = {
        {name:"pizza_1", stores:"auchan", nutriscore:"C"},
        {name:"pizza_2", stores:"leclerc", nutriscore:"B"},
        {name:"pizza_3", stores:"carrefour", nutriscore:"C"},
        {name:"pizza_4", stores:"intermarche", nutriscore:"A"},
        {name:"pizza_5", stores:"auchan", nutriscore:"B"},
        {name:"pizza_6", stores:"super u", nutriscore:"A"},
    }
    return tproducts

@pytest.mark.django_db
def test_substitutes():
    # product = Product.objects.get(pk=1)
    # product = create_products().objects.get(pk=1)
    product = Product().objects.get(pk=1) in create_products()
    assert (len(product.get_six_better_substitutes()) == 6) in create_products()