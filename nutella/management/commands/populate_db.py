from django.core.management.base import BaseCommand, CommandError
import requests
import pprint
from nutella.models import Category, Product

from requests.models import encode_multipart_formdata


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--category", type=str, default="pizza")
        parser.add_argument("--page", type=int, default=1)
        parser.add_argument("--page_size", type=int, default=1)

    def handle(self, *args, **options):
        category_name = options["category"][0]
        page = options["page"]
        page_size = options["page_size"]
        
        response = requests.get(url=
            f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={category_name}&search_simple=1&action=process&json=1&page={page}&page_size={page_size}"
        )

        product_list = response.json()

        cat, created = Category.objects.get_or_create(name=category_name)

        for product_data in product_list["products"]:
            if not self.check_product_data(product_data):
                continue
       
            product = Product.objects.update_or_create(
                name=product_data["product_name_fr"],
                stores=product_data["stores"],
                nutriscore=product_data["nutrition_grade_fr"].upper(),
                url=product_data["url"],
                image=product_data["image_url"],
                nutrition=product_data["image_nutrition_url"],
                category=cat

            )

            

            print(
                "Nom du produit : ",
                product_data["product_name_fr"],
                "\nCatégories : ",
                product_data["categories"],
                "\nMagasins :",
                product_data["stores"],
                "\nNutriscore : ",
                product_data["nutrition_grade_fr"],
                "\nUrl : ",
                product_data["url"],
                "\n",
            )

    def check_product_data(self, product_data):
        if not "categories_lc" in product_data: 
            return False
        if product_data["categories_lc"] != "fr":
            return False
        if not "image_nutrition_url" in product_data:
            return False
        if not "stores" in product_data:
            return False
        return True