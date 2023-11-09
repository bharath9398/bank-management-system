
import mysql.connector

class insert:
    def __init__(self):
        self.connect=mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password='Sattu@1999',
                database='bank'
                )

    
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.connect.cursor() # creating cursor
        cur.execute(f"insert into  personal_details values({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.connect.commit()
        print("-----------personal information saved sucessfully-------------")

    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.connect.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.connect.commit()
        print("-----------Bank details has been saved sucessfuly------------------")

    def transaction_details(self,tid,sac,rac,am,mtd):
        cur=self.connect.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sac},{rac},{am},'{mtd}')")
        self.connect.commit()
        print("----------- transaction details has been saved sucessfuly------------------")

    def account_details(self,acn,tid,am,cb,tp):
        cur=self.connect.cursor()
        cur.execute(f"insert into account_details values({acn},{tid},{am},{cb},'{tp}')")
        self.connect.commit()
        print("----------- account details has been saved sucessfuly------------------")


 
