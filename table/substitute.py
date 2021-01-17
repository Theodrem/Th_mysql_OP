from db.model_table import ModelTable
from db.request import SELECT, UPDATE


class Substitute(ModelTable):
    fields = ["substitute_id", "substituted_product_id", "user_id"]
    name_table = "Substitute"

    def __init__(self, substitute_id=None, substituted_product_id=None, user_id=None):
        super().__init__()
        self.substitute_id = substitute_id
        self.substituted_product_id = substituted_product_id
        self.user_id = user_id

    def update(self):
        """
        Updates database
        """
        request = UPDATE["update_substitute"] % (
            self.substitute_id,
            self.substituted_product_id,
            self.user_id,
            self.id,
        )
        self.db.execute_and_save(request)
