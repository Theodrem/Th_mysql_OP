from db.model_db import Modeldb
from db.request import CREATE


def shema_generate():
    """
    Execute and commit request create table:
    Category
    Product
    Substitute
    """
    db = Modeldb()
    db.execute_and_save(CREATE["Category"])
    db.execute_and_save(CREATE["Product"])
    db.execute_and_save(CREATE["Substitute"])
