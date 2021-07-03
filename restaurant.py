from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root, bg="black", width=1600, height=500, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg='blue', bd=10, anchor=W)
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text=localtime, fg="red", anchor=W)
lblinfo.grid(row=1, column=0)

text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg='green', justify='right')
txtdisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def equals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def ref():
    x = random.randint(0, 50000)
    randomRef = str(x)
    rand.set(randomRef)

    fries = float(Fries.get())
    lunch_meal = float(LargeFries.get())
    burger_meal = float(Burger.get())
    poutine_meal = float(Poutine.get())
    cheese_burger = float(Cheese_Burger.get())
    drinks = float(Drinks.get())

    fries_cost = fries*4
    lunch_cost = lunch_meal*10
    burger_cost = burger_meal*8
    poutine_cost = poutine_meal*6
    cheese_burger_cost = cheese_burger*7
    drinks_cost = drinks*3

    Meal_cost = "$ ", str('%.2f'% (fries_cost + lunch_cost + burger_cost + poutine_cost + cheese_burger_cost + drinks_cost))

    Tax_Payable = ((fries_cost + lunch_cost + burger_cost + poutine_cost + cheese_burger_cost + drinks_cost)*0.13)

    Totalcost = (fries_cost + lunch_cost + burger_cost + poutine_cost + cheese_burger_cost + drinks_cost)

    Ser_Charge = ((fries_cost + lunch_cost + burger_cost + poutine_cost + cheese_burger_cost + drinks_cost)/99)

    Service = "$ ", str('%.2f'% Ser_Charge)

    OverallCost = "$ ", str(Tax_Payable + Totalcost + Ser_Charge)

    PaidTax = "$ ", str('%.2f'% Tax_Payable)

    Service_Charge.set(Service)
    Cost.set(Meal_cost)
    Tax.set(PaidTax)
    SubTotal.set(Meal_cost)
    Total.set(OverallCost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    LargeFries.set("")
    Burger.set("")
    Poutine.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Cheese_Burger.set("")

btn7 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="7", bg="black", command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="8", bg="black", command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="9", bg="black", command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="+", bg="black", command=lambda: btnclick("+"))
Addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="4", bg="black", command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="5", bg="black", command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="6", bg="black", command=lambda: btnclick(6))
btn6.grid(row=3, column=2)

Subtraction = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="-", bg="black", command=lambda: btnclick("-"))
Subtraction.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="1", bg="black", command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="2", bg="black", command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="3", bg="black", command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

Multiply = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="-", bg="black", command=lambda: btnclick("*"))
Multiply.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="0", bg="black", command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="c", bg="black", command=lambda: clrdisplay)
btnc.grid(row=5, column=1)

decimal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text=".", bg="black", command=lambda: btnclick("."))
decimal.grid(row=5, column=2)

Division = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="/", bg="black", command=lambda: btnclick("/"))
Division.grid(row=5, column=3)

btnequal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial',20,'bold'), text="=", bg="black", command=equals)
btnequal.grid(columnspan=4)

rand = StringVar()
Fries = StringVar()
LargeFries = StringVar()
Burger = StringVar()
Poutine = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Cheese_Burger = StringVar()

lblreference = Label(f1, font=('aria', 16, 'bold'), text= "Order No.", fg="black", bd=10, anchor=W)
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('arial', 17, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="red", justify="right")
txtreference.grid(row=1, column=1)

lblfries = Label(f1, font=('aria', 16, 'bold'), text= "Fries", fg="black", bd=10, anchor=W)
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('arial', 17, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="red", justify="right")
txtfries.grid(row=1, column=1)

lbllargefries = Label(f1, font=('aria', 16, 'bold'), text= "LargeFries", fg="black", bd=10, anchor=W)
lbllargefries.grid(row=2, column=0)
txtlargefries = Entry(f1, font=('arial', 17, 'bold'), textvariable=LargeFries, bd=6, insertwidth=4, bg="red", justify="right")
txtlargefries.grid(row=2, column=1)

lblburger = Label(f1, font=('aria', 16, 'bold'), text= "Burger", fg="black", bd=10, anchor=W)
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="red", justify="right")
txtburger.grid(row=3, column=1)

lblpoutine = Label(f1, font=('aria', 16, 'bold'), text= "Poutine", fg="black", bd=10, anchor=W)
lblpoutine.grid(row=4, column=0)
txtpoutine = Entry(f1, font=('arial', 17, 'bold'), textvariable=Poutine, bd=6, insertwidth=4, bg="red", justify="right")
txtpoutine.grid(row=4, column=1)

lblcheese_burger = Label(f1, font=('aria', 16, 'bold'), text= "Cheese Burger", fg="black", bd=10, anchor=W)
lblcheese_burger.grid(row=5, column=0)
txtcheese_burger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cheese_Burger, bd=6, insertwidth=4, bg="red", justify="right")
txtcheese_burger.grid(row=5, column=1)

lbldrinks = Label(f1, font=('aria', 16, 'bold'), text= "Drinks", fg="black", bd=10, anchor=W)
lbldrinks.grid(row=0, column=2)
txtdrinks = Entry(f1, font=('arial', 17, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="red", justify="right")
txtdrinks.grid(row=0, column=3)

lblcost = Label(f1, font=('aria', 16, 'bold'), text= "Cost", fg="black", bd=10, anchor=W)
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cost, bd=6, insertwidth=4, bg="red", justify="right")
txtcost.grid(row=1, column=3)

lblservice_charge = Label(f1, font=('aria', 16, 'bold'), text= "Service Charge", fg="black", bd=10, anchor=W)
lblservice_charge.grid(row=2, column=2)
txtservice_charge = Entry(f1, font=('arial', 17, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg="red", justify="right")
txtservice_charge.grid(row=2, column=3)

lbltax = Label(f1, font=('aria', 16, 'bold'), text= "Tax", fg="black", bd=10, anchor=W)
lbltax.grid(row=3, column=2)
txttax = Entry(f1, font=('arial', 17, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="red", justify="right")
txttax.grid(row=3, column=3)

lblsubtotal = Label(f1, font=('aria', 16, 'bold'), text= "Sub-Total", fg="black", bd=10, anchor=W)
lblsubtotal.grid(row=4, column=2)
txtsubtotal = Entry(f1, font=('arial', 17, 'bold'), textvariable=SubTotal, bd=6, insertwidth=4, bg="red", justify="right")
txtsubtotal.grid(row=4, column=3)

lbltotal = Label(f1, font=('aria', 16, 'bold'), text= "Total", fg="black", bd=10, anchor=W)
lbltotal.grid(row=5, column=2)
txttotal = Entry(f1, font=('arial', 17, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="red", justify="right")
txttotal.grid(row=5, column=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width=10, text="TOTAL", bg="black", command=ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width=10, text="RESET", bg="black", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width=10, text="EXIT", bg="black", command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x200")
    roo.title("Price List")
    x = Frame(roo, bg="white", width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="ITEM", fg="red", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="_______", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="PRICE", fg="red", bd=5, anchor=W)
    lblinfo.grid(row=0, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="4", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Lunch Combo", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="8", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Poutine", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="6", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="7", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=5)

    lblinfo = Label(x, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(x, font=('aria', 15, 'bold'), text="3", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=5)

    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width=10, text="PRICE", bg="black", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()





