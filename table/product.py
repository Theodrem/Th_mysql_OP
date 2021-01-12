from db.model_table import ModelTable
from db.model_db import Modeldb
from db.request import SELECT
from db.request import UPDATE


class Product(ModelTable):
    fields = [
        "name",
        "nutriscore",
        "url",
        "store",
        "description",
        "openfoodfact_id",
        "category_id"
    ]
    name_table = "Product"

    def __init__(self, name=None, nutriscore=None, url=None, store=None, description=None, openfoodfact_id=None,
                 category_id=None):
        super().__init__()
        self.name = name
        self.nutriscore = nutriscore
        self.url = url
        self.store = store
        self.description = description
        self.openfoodfact_id = openfoodfact_id
        self.category_id = category_id

    def update(self):
        """
        Updates database
        """
        request = UPDATE["update_product"] % (
        self.name, self.nutriscore, self.url, self.store, self.description, self.openfoodfact_id
        , self.category_id, self.id)

        self.db.execute_and_save(request)

    @classmethod
    def get_proposition_substitute(cls, categoryid, nutriscore, id):
        """
       Return the substitutes proposition
       """
        request = SELECT["select_proposition_substitute"] % (categoryid, nutriscore, id)
        return cls.get_rows(request)

    @classmethod
    def get_substitute(cls, column, user):
        """
        Return user substitutes
        """
        request = SELECT["select_substitute"] % (column, user)
        return cls.get_rows(request)
