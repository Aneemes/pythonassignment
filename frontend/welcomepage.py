from tkinter import *
import frontend.customertier
import frontend.billing
import model.supply


class welcome:
    def __init__(self, window):
        self.wn = window
        self.wn.title('welcome')
        self.wn.config(bg='grey')
        self.wn.geometry('900x800')

        self.lb_heading = Label(self.wn, text='WELCOME', bg='grey', fg='brown', font=('Rockwell', 39, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.frame = Frame(self.wn, bg='grey')
        self.frame.place(x=100, y=100)

        self.btn_supp = Button(self.frame, text='Supplies Track', fg='black', font=('Rockwell', 35, 'bold'),
                               command=self.btn_supp_click)
        self.btn_supp.grid(row=1, column=1, ipadx=10, ipady=10)

        self.btn_customertier = Button(self.frame, text='Customer Tier Info', fg='black',
                                     font=('Rockwell', 35, 'bold'), command=self.btn_customertier_click)
        self.btn_customertier.grid(row=2, column=1, ipadx=10, ipady=10)

        self.btn_checkout = Button(self.frame, text='Checkout', fg='black', font=('Rockwell', 35, 'bold'),
                                  command=self.btn_checkout_click)
        self.btn_checkout.grid(row=3, column=1, ipadx=10, ipady=10)

        self.btn_exit = Button(self.frame, text='Exit', fg='black', font=('Rockwell', 35, 'bold'),
                               command=self.wn.destroy)
        self.btn_exit.grid(row=4, column=1, ipadx=10, ipady=10)

    def btn_supp_click(self):
        user_window = Tk()
        model.supply.suppliestrack(user_window)

    


    def btn_customertier_click(self):
        user_window = Tk()
        frontend.customertier.customertier(user_window)

    def btn_checkout_click(self):
        user_window = Tk()
        frontend.billing(user_window)


#wn = Tk()
#welcome(wn)
#wn.mainloop()