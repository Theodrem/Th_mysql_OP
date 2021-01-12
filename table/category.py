from db.model_table import ModelTable
from db.model_db import Modeldb
from db.request import SELECT
import random
from db.request import UPDATE


class Category(ModelTable):
    fields = [
        "name"
    ]
    name_table = "Category"

    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.id = None

    def update(self):
        """
        Updates database
        """
        request = UPDATE["update_category"] % (self.name, self.id)
        self.db.execute_and_save(request)
