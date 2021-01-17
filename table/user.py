from db.request import INSERT, SELECT, UPDATE
from db.model_table import ModelTable


class User(ModelTable):
    fields = ["pseudo"]
    name_table = "User"

    def __init__(self, pseudo=None):
        super().__init__()
        self.pseudo = pseudo
        self.id = None

    @classmethod
    def get_pseudo(cls, user):
        """
        Get user id where pseudo
        """
        request = SELECT["select_id_user"] % (user)
        return cls.get_rows(request)

    def get_id(self):
        """
        Check if the id matches with a substitute id
        """
        print(self.pseudo, self.fields[0])
        users = self.select_all_where(self.fields[0], self.pseudo)
        for user in users:
            self.id = user.id
