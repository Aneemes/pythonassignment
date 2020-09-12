from tkinter import *
import random

root = Tk()
root.geometry("1000x1000")
root.title("Restaurant Management System")
root.configure(background='grey')

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN, bg="grey")
f1.pack(side=LEFT)




lblInfo = Label(Tops, font=('Rockwell', 50, 'bold'), text="BILLING", fg="Black", bg="grey", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    if (Fries.get() == ""):
        CoFries = 0
    else:
        CoFries = float(Fries.get())

    if (Noodles.get() == ""):
        CoNoodles = 0
    else:
        CoNoodles = float(Noodles.get())

    if (Pizza.get() == ""):
        CoPizza = 0
    else:
        CoPizza = float(Pizza.get())

    if (Burger.get() == ""):
        CoBurger = 0
    else:
        CoBurger = float(Burger.get())

    if (Sandwich.get() == ""):
        CoSandwich = 0
    else:
        CoSandwich = float(Sandwich.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    CostofFries = CoFries * 100
    CostofDrinks = CoD * 80
    CostofNoodles = CoNoodles * 150
    CostofPizza = CoPizza * 400
    CostBurger = CoBurger * 300
    CostSandwich = CoSandwich * 200

    CostofMeal = "Rs", str(
        '%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofPizza + CostBurger + CostSandwich))

    PayTax = ((CostofFries + CostofDrinks + CostofNoodles + CostofPizza + CostBurger + CostSandwich) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofPizza + CostBurger + CostSandwich)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofPizza + CostBurger + CostSandwich) / 99)

    Service = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Pizza.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")


rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Pizza = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Burger = StringVar()
Sandwich = StringVar()

lblReference = Label(f1, font=('Rockwell', 16, 'bold'), text="Reference", anchor="center", bg="grey")
lblReference.grid(row=0, column=0, padx=10, pady=10)
txtReference = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=rand, insertwidth=4, bg="white",
                     justify='right')
txtReference.grid(row=0, column=1, padx=10, pady=10)

lblFries = Label(f1, font=('Rockwell', 16, 'bold'), text="Fries", anchor="center", bg="grey")
lblFries.grid(row=1, column=0, padx=10, pady=10)
txtFries = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Fries, insertwidth=4, bg="white",
                 justify='right')
txtFries.grid(row=1, column=1, padx=10, pady=10)

lblNoodles = Label(f1, font=('Rockwell', 16, 'bold'), text="Noodles", anchor="center", bg="grey")
lblNoodles.grid(row=2, column=0, padx=10, pady=10)
txtNoodles = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Noodles, insertwidth=4, bg="white",
                   justify='right')
txtNoodles.grid(row=2, column=1, padx=10, pady=10)

lblPizza = Label(f1, font=('Rockwell', 16, 'bold'), text="Pizza", anchor="center", bg="grey")
lblPizza.grid(row=3, column=0, padx=10, pady=10)
txtPizza = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Pizza, insertwidth=4, bg="white", justify='right')
txtPizza.grid(row=3, column=1, padx=10, pady=10)

lblBurger = Label(f1, font=('Rockwell', 16, 'bold'), text="Burger", anchor="center", bg="grey")
lblBurger.grid(row=4, column=0, padx=10, pady=10)
txtBurger = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Burger, insertwidth=4, bg="white",
                  justify='right')
txtBurger.grid(row=4, column=1, padx=10, pady=10)

lblSandwich = Label(f1, font=('Rockwell', 16, 'bold'), text="Sandwich", anchor="center", bg="grey")
lblSandwich.grid(row=5, column=0, padx=10, pady=10)
txtSandwich = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Sandwich, insertwidth=4, bg="white",
                    justify='right')
txtSandwich.grid(row=5, column=1, padx=10, pady=10)


lblDrinks = Label(f1, font=('Rockwell', 16, 'bold'), text="Drinks", anchor="center", bg="grey")
lblDrinks.grid(row=0, column=2, padx=10, pady=10)
txtDrinks = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Drinks, insertwidth=4, bg="white",
                  justify='right')
txtDrinks.grid(row=0, column=3, padx=10, pady=10)

lblCost = Label(f1, font=('Rockwell', 16, 'bold'), text="Cost of Meal", anchor="center", bg="grey")
lblCost.grid(row=1, column=2, padx=10, pady=10)
txtCost = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Cost, insertwidth=4, bg="white", justify='right')
txtCost.grid(row=1, column=3, padx=10, pady=10)

lblService = Label(f1, font=('Rockwell', 16, 'bold'), text="Service Charge", anchor="center", bg="grey")
lblService.grid(row=2, column=2, padx=10, pady=10)
txtService = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Service_Charge, insertwidth=4, bg="white",
                   justify='right')
txtService.grid(row=2, column=3, padx=10, pady=10)

lblStateTax = Label(f1, font=('Rockwell', 16, 'bold'), text="State Tax", anchor="center", bg="grey")
lblStateTax.grid(row=3, column=2, padx=10, pady=10)
txtStateTax = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Tax, insertwidth=4, bg="white",
                    justify='right')
txtStateTax.grid(row=3, column=3, padx=10, pady=10)

lblSubTotal = Label(f1, font=('Rockwell', 16, 'bold'), text="Sub Total", anchor="center", bg="grey")
lblSubTotal.grid(row=4, column=2, padx=10, pady=10)
txtSubTotal = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=SubTotal, insertwidth=4, bg="white",
                    justify='right')
txtSubTotal.grid(row=4, column=3, padx=10, pady=10)

lblTotalCost = Label(f1, font=('Rockwell', 16, 'bold'), text="Total Cost", anchor="center", bg="grey")
lblTotalCost.grid(row=5, column=2, padx=10, pady=10)
txtTotalCost = Entry(f1, font=('Rockwell', 16, 'bold'), textvariable=Total, insertwidth=4, bg="white",
                     justify='right')
txtTotalCost.grid(row=5, column=3, padx=10, pady=10)


btnTotal = Button(f1, padx=10, pady=10, fg="black", font=('Rockwell', 16, 'bold'), width=10, text="Total",
                  bg="white", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=10, pady=10, fg="black", font=('Rockwell', 16, 'bold'), width=10, text="Reset",
                  bg="white", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=10, pady=10,  fg="black", font=('Rockwell', 16, 'bold'), width=10, text="Exit",
                 bg="white", command=qExit).grid(row=7, column=3)

root.mainloop()

