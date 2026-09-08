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

class employee_manager(DbConnect):
    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from employee"
            self.cursor.execute(query)
            records= self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)


connection_istance = DbConnect()
connection_istance.get_connection()