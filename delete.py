import mysql.connector

class delete:
    def __init__(self):
        self.connect=mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password='Sattu@1999',
                database='bank'
                )
        
    def specific_del(self,table_name,cusid):
        cur = self.connect.cursor()
        cur.execute(f"DELETE from {table_name} where customerid={cusid}")
        self.connect.commit()
        print("Data has been deleted sucesfuly")


   