import requests
from table.category import Category
from table.product import Product

"""
API connection data
"""
post_data = {"name": "Theotim", "username": "theodrem", "password": "Intelligence97"}
responses = requests.get("https://fr.openfoodfacts.org/categories.json", data=post_data)
current = responses.json()


def update_product_attr(obj, dico):
    """
    Attributes the keys and values as parameters to the object.
    """
    for key, value in dico.items():
        setattr(obj, key, value)


def insert_data_from_openfoodfacts():
    """
    Get the first fifteen categories and add them to our database
    """
    for category in range(15):
        name_category = current["tags"][category]["name"]
        try:
            cat = Category.get_object("name", name_category)
        except Category.ObjectDoesNotExist:
            cat = Category(name_category)
        cat.save()

        """
        Get the first hundred categories and add them to our database
        """
        for page in range(5):
            url_category = "%s/%s.json" % (current["tags"][category]["url"], page + 1)
            products = requests.get(url_category)
            result = products.json()

            try:
                name = result["products"][page]["product_name"]
                url = result["products"][page]["url"]
                description = result["products"][page]["ingredients_text_fr"]
                nutriscore = result["products"][page]["nutrition_grades"]
                store = result["products"][page]["stores"]
                openfoodfact_id = result["products"][page]["id"]
                categories = Category.select_all_where("name", name_category)
                category_id = 0
                for cat in categories:
                    category_id = cat.id
                if (
                    name != ""
                    and url != ""
                    and nutriscore != ""
                    and store != ""
                    and openfoodfact_id != ""
                ):  # If a data is not complete, we do not retrieve it
                    try:
                        product = Product.get_object("openfoodfact_id", openfoodfact_id)
                    except Product.ObjectDoesNotExist:
                        product = Product()
                    update_product_attr(
                        product,
                        {
                            "name": name,
                            "nutriscore": nutriscore,
                            "url": url,
                            "store": store,
                            "description": description,
                            "openfoodfact_id": openfoodfact_id,
                            "category_id": category_id,
                        },
                    )
                    product.save()

            except (IndexError, KeyError, ValueError):
                pass
