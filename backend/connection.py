import mysql.connector

class DbConnection:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost", user="root", password="1990", database="python2")
        self.cursor=self.con.cursor()


    def insert(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def delete(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def select(self,query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.con.commit()


