import mysql.connector

class update:
    def __init__(self):
        self.connect=mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password='Sattu@1999',
                database='bank'
                )
        
    def myupdate(self,table_name,column_name,new_value,cusid):
        cur = self.connect.cursor()
        if new_value.isnumeric():
            print("test1")
            cur.execute(f"UPDATE {table_name} set {column_name}={int(new_value)} where customerid={cusid}")
        else:
            print("test2")
            cur.execute(f"UPDATE {table_name} set {column_name}='{new_value}' where customerid={cusid}")
        self.connect.commit()
        print("updated sucessfully")    