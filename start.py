from api import insert_data_from_openfoodfacts
from shema_generate import shema_generate
from table.category import Category
from table.product import Product
from table.substitute import Substitute
from table.user import User
from db.model_db import Modeldb
from config import INTERACTION, SUB, NUTRI


class Start():
    def __init__(self):
        self.run = True
        self.pseudo_id = 0
        self.choice = 0
        self.category_choice = 0

    def login(self):
        """
        The user enters his nickname
        Then saves it in the user database
        """
        try:
            self.choice = int(input(INTERACTION["ASK_PSEUDO"]))
            pseudo = input(INTERACTION["ENTER_PSEUDO"])

        except ValueError:
            self.login()

        if self.choice == 2:
            user = User(pseudo)
            user.save()

        pseudos = User.get_pseudo(pseudo)

        for pseudo in pseudos:
            self.pseudo_id = pseudo.id

        if self.pseudo_id == 0:
            print(INTERACTION["USER_ERR"])
            self.login()

    def choose_category(self):
        """
        Display all categories and user chooses one
        """
        categories = Category.select_all()

        for category in categories:
            print(category.id, category.name)

        self.category_choice = int(input(INTERACTION["CAT_CHOICE"]))

    def choose_product(self):
        """
        Displays the products of the chosen category
        """
        products = Product.select_all_where("category_id", self.category_choice)

        for product in products:
            print(product.id, product.name)

        self.choice = int(input(INTERACTION["PROD_CHOICE"]))
        self.propose_substitute()

    def propose_substitute(self):
        """
        Suggest a substitute with a better nutritional score
        """
        products = Product.select_all_where("id", self.choice)

        nutriscore = ""

        for product in products:
            category_id = product.category_id
            print(product.id, product.name, product.nutriscore)
            nutriscore = product.nutriscore

        if category_id != self.category_choice:
            print("Le produit ne correspond pas à la categorie sélectionné")
            self.choose_product()
        else:
            print(SUB["SUBSTITUTE"])
            id_substitute = 0

            try:
                substitutes = Product.get_proposition_substitute(self.category_choice, nutriscore, self.choice)

                for substitute in substitutes:
                    print(substitute.id, substitute.name, substitute.nutriscore, substitute.store, substitute.url)
                    id_substitute = substitute.id

                save = int(input(SUB["SAVE"]))
                if save == 1:
                    self.save_substitute(id_substitute)

            except AttributeError:
                print("Pas de substitut trouvé")

    def save_substitute(self, id_substitut):
        """
        The user chooses to save the substitute or not.
        """
        substitute = Substitute(id_substitut, self.choice, self.pseudo_id)
        substitute.save()

    def show_substitutes(self):
        """
        Displays the user's substitutes and substituted products
        """

        print(SUB["SUBSTITUTE"])
        substitutes = Product.get_substitute("substitute_id", self.pseudo_id)

        for substitute in substitutes:
            print(substitute.id, substitute.name, substitute.nutriscore, substitute.url, substitute.store,
                  substitute.description)
        print(SUB["SUBSTITUTED"])

        substituted_products = Product.get_substitute("substituted_product_id", self.pseudo_id)
        for substituted in substituted_products:
            print(substituted.id, substituted.name, substituted.nutriscore, substituted.url, substituted.store,
                  substituted.description)

    def running(self):
        """
        Logins user.
        Program while loop

        The user makes a choice:
        1 = Displays the categories, products.Save the substitute
        2 = Dysplays his substitutes
        3 = Refresh db
        4 =  Stop the program and close the cursor.

        """
        self.login()

        while self.run:
            try:
                self.choice = int(input(INTERACTION["FIRST_CHOICE"]))

                if self.choice == 1:
                    self.choose_category()
                    self.choose_product()

                elif self.choice == 2:
                    self.show_substitutes()

                elif self.choice == 3:
                    insert_data_from_openfoodfacts()

                elif self.choice == 4:
                    db = Modeldb()
                    db.close()
                    self.run = False

            except ValueError:
                print(INTERACTION["VALUE_ERR"])












