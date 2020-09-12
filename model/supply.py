from tkinter import *
from tkinter import ttk
from backend.connection import *
import mysql.connector


class suppliestrack:

    db_name ='database.db'
    def __init__(self,wind):
        self.wind=wind
        self.wind.title ('Supplies')

        self.tree = ttk.Treeview (height=10, columns=2)
        self.tree.grid (row=4, column=0, columnspan=2)
        self.tree.heading('40',text='Name', anchor='w')
        self.tree.heading(2, text='price', anchor='w')

        self.dbconnect = DbConnection()

        self.viewing_records()


    def run_query (self,query, values):
        with mysql.connect(self.db_name) as conn:
            cursor=conn.cursor()
            query_result = cursor.execute(query,values)
            conn.commit()
        return query_result

    def viewing_records(self):
        records=self.tree_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM supplies ORDER BY name Desc'
        db_rows = self.run_query (query)
        for row in db_rows:
            self.tree.insert ('', 0, text=row[1], values=row[2])

if __name__ == '__main__':
    wind = Tk ()
    suppliestrack (wind)
    wind.mainloop()
