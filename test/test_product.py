import pytest
from nutella.models import Product

@pytest.mark.django_db
def test_substitutes():
    product = Product.objects.get(pk=1)
    assert len(product.get_six_better_substitutes()) == 6