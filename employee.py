import mysql.connector


class DbConnect:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="gym_db"
            )
            return self.connection

        except Exception as e:
            return None

connection_istance = DbConnect()
connection_istance.get_connection()