from tkinter import*
from model.customer import*

import mysql.connector



class customertier:
    def __init__(self, window):
        self.wn = window
        self.wn.title('welcome')
        self.wn.config(bg='grey')
        self.wn.geometry('900x800')

        ###############connection object#########



        self.lb_heading = Label(self.wn, text='Customer Tier Info', bg='grey', fg='brown', font=('Rockwell', 39, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn, bg='grey')
        self.frame1.place(x=100, y=100)

        self.lb_customername = Label(self.frame1, text='Customer Name:', fg='black', bg='grey', font=('Rockwell', 15, 'bold'))
        self.lb_customername.grid(row=0, column=0, padx=10, pady=10)

        self.ent_customername = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.ent_customername.grid(row=0, column=1, padx=10, pady=10)

        self.lb_tier = Label(self.frame1, text='Tier', fg='black', bg='grey', font=('Rockwell', 15, 'bold'))
        self.lb_tier.grid(row=1, column=0, padx=10, pady=10)

        self.ent_tier = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.ent_tier.grid(row=1, column=1, padx=10, pady=10)



        self.btn_add = Button(self.frame1, text='Add', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                              command=self.add)
        self.btn_add.grid(row=2, column=1)

        self.btn_reset = Button(self.frame1, text='Reset', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                                command=self.btn_reset_click)
        self.btn_reset.grid(row=2, column=2)


    def add(self):
        con=mysql.connector.connect(host="localhost",user="root",password="1990",database="python2")
        cur=con.cursor()
        cur.execute("insert into customertier values(%s,%s)",(self.ent_customername.get(),
                                                              self.ent_tier.get()
                                                              ))
        con.commit()
        con.close()
    def btn_reset_click(self):
        self.ent_customername.delete(0, "end")
        self.ent_tier.delete(0, "end")




#wn = Tk()
#customertier(wn)
#wn.mainloop()