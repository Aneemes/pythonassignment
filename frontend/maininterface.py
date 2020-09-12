from tkinter import *
import frontend.welcomepage
import tkinter.messagebox



class Login_form:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Resturant Management System')
        self.wn.config(bg='grey')
        self.wn.geometry('800x800')

        self.lb_heading = Label(self.wn, text='Login Form', bg='grey', fg='black', font=('Rockwell', 20, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn, bg='grey')
        self.frame1.place(x=50, y=100)

        self.lb_branchname = Label(self.frame1, text='Branch Name:', fg='black', bg='grey',
                                   font=('Rockwell', 15, 'bold'))
        self.lb_branchname.grid(row=0, column=0, padx=10, pady=10)

        self.ent_branchname = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.ent_branchname.grid(row=0, column=1, padx=10, pady=10)

        self.lb_password = Label(self.frame1, text='Password:', fg='black', bg='grey', font=('Rockwell', 15, 'bold'))
        self.lb_password.grid(row=1, column=0, padx=10, pady=10)

        self.ent_password = Entry(self.frame1, font=('arial', 15, 'bold'), show='*')
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        self.btn_login = Button(self.frame1, text='Login', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                                command=self.btn_login_click)
        self.btn_login.place(x=180, y=100)

        self.btn_reset = Button(self.frame1, text='Reset', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                                command=self.btn_reset_click)
        self.btn_reset.grid(row=2, column=1)





    def btn_login_click(self):
        user_window = Tk()
        frontend.welcomepage.welcome(user_window)


    def btn_reset_click(self):
        self.ent_password.delete(0, "end")
        self.ent_branchname.delete(0, "end")

wn = Tk()
Login_form(wn)
wn.mainloop()
