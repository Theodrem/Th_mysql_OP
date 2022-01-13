import mysql.connector as MC


class Modeldb:
    def __init__(self):
        """
        Contains the connection data to mysql
        """
        self.conn = MC.connect(
            host="localhost",
            user="theotim",
            password="",
            database="openfoodfacts",
        )
        self.cursor = self.conn.cursor(buffered=True)

    def fetch_rows(self, request):
        """
        Execute mysql requests
        Returns the list of data
        """

        self.cursor.execute(request)
        data_list = self.cursor.fetchall()
        return data_list

    def close(self):
        """
        Close cursor
        """

        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

    def execute_and_save(self, request):
        """
        Execute and save one request
        """
        self.cursor.execute(request)
        self.conn.commit()
