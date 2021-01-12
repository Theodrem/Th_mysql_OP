from db.model_db import Modeldb
from db.request import INSERT, SELECT, DROP


class ModelTable():
    class ObjectDoesNotExist(Exception): #Custom error class
        pass

    fields = []
    name_table = None
    db = Modeldb()

    def __init__(self):
        self.id = None

    def insert(self):

        """
        Format list columns to string.
        If the column and value parameters does not exist
        execute request insert into table with table_name ,format_column and values
        """

        format_column = (",").join(self.fields)

        attr_field = []  # list values
        list_string_values = []  # list values between quotation marks

        for field in self.fields:
            attr_field.append(getattr(self, field))

        for i in attr_field:
            list_string_values.append('"%s"' % (i))

        format_values = ",".join(map(str, list_string_values))
        request = INSERT["insert"] % (self.name_table, format_column, format_values)
        self.db.execute_and_save(request)

    @classmethod
    def drop_table(cls):
        """
        Drop table
        """
        request = DROP["DROP"] % (cls.name_table)
        cls.db.execute_and_save(request)

    @classmethod
    def select_all(cls):
        """
        Return all datas from table
        """
        request = SELECT["select_all"] % (cls.name_table)
        return cls.get_rows(request)

    @classmethod
    def select_all_where(cls, category, condition):
        """
        Return all datas from table with one condition
        """
        request = SELECT["select_all_where"] % (cls.name_table, category, condition)
        return cls.get_rows(request)

    @classmethod
    def get_object(cls, category, condition):
        """
        Check if the field exists, otherwise it returns our error class
        """
        try:
            return cls.select_all_where(category, condition)[0]
        except IndexError:
            raise cls.ObjectDoesNotExist

    @classmethod
    def _sql_to_objects(cls, rows):
        """
        Create list
        Add fields objects in list
        Return list
        """
        objects = []
        for row in rows:
            obj = cls()
            obj.id = row[0]

            for index, field in enumerate(cls.fields):
                setattr(obj, field, row[index + 1])
            objects.append(obj)

        return objects

    @classmethod
    def get_rows(cls, request):
        """
        Get data with fetchall
        Return data as objects
        """
        rows = cls.db.fetch_rows(request)
        return cls._sql_to_objects(rows)

    def save(self):
        """
         if id exist:
            update database
         else:
             insert
        """
        if self.id is None:
            self.insert()
        else:
            self.update()







        
                



            



        
    
   
    
    

    
    
