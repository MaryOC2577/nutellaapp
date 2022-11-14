""" Custom command to populate the database. """

import requests
from django.core.management.base import BaseCommand
from nutella.models import Category, Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--category", type=str, default="pizza")
        parser.add_argument("--page", type=int, default=1)
        parser.add_argument("--page_size", type=int, default=1)

    def handle(self, *args, **options):
        category_name = options["category"][0]
        page = options["page"]
        page_size = options["page_size"]
        response = requests.get(
            url=f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={category_name}&search_simple=1&action=process&json=1&page={page}&page_size={page_size}"
        )

        product_list = response.json()

        cat, created = Category.objects.get_or_create(name=category_name)

        for product_data in product_list["products"]:
            if not self.check_product_data(product_data):
                continue
            else:
                print(cat)
                product = Product.objects.update_or_create(
                    name=product_data["product_name_fr"],
                    stores=product_data["stores"],
                    nutriscore=product_data["nutrition_grade_fr"].upper(),
                    url=product_data["url"],
                    image=product_data["image_url"],
                    nutrition=product_data["image_nutrition_url"],
                    # category=cat,
                )
                product.category.add
        print("Les données ont été enregistrées avec succès.")

    def check_product_data(self, product_data):
        if "categories_lc" not in product_data:
            return False
        if product_data["categories_lc"] != "fr":
            return False
        if "image_nutrition_url" not in product_data:
            return False
        if "stores" not in product_data:
            return False
        return True
