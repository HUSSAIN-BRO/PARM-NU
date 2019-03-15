from tkinter import*
import random
import time;
root=Tk()
root.title("Restaurent management systems")
root.geometry("1600x800+0+0")
text_input=StringVar()
operator=""

tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
# .......................for time..................
localtime=time.asctime(time.localtime(time.time()))
# .......................for information,,...........

lbl_info=Label(tops,font=("arial",50,"bold"),text="Restaurent Management System",bd=10,fg="steel blue",anchor="w")
lbl_info.grid(row=0,column=0)
lbl_info=Label(tops,font=("arial",20,"bold"),text=localtime,bd=10,fg="steel blue",anchor="w")
lbl_info.grid(row=1,column=0)
# **********************calculator******************
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btncleartext():
    global operator
    operator=""
    text_input.set("")
def equals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
def ref():
    x=random.randint(90210,210357)
    randomref=str(x)
    rand.set(randomref)

    cof=float(fries.get())
    cod=float(Drinks.get())
    coburger=float(burger.get())
    cofilet=float(filet.get())
    cochickenburger=float(chicken_burger.get())
    cocheeseburger=float(cheese_burger.get())

    cost_of_fries=cof*80
    cost_of_drinks=cod*20
    cost_of_burger=coburger*65
    cost_of_filet=cofilet*230
    cost_of_chickenburger=cochickenburger*130
    cost_of_cheeseburger=cocheeseburger*89

    cost_of_meal="₹"+str("%.2f"%(cost_of_fries+cost_of_drinks+cost_of_burger+cost_of_filet+cost_of_chickenburger+cost_of_cheeseburger))
    paytax=(cost_of_fries+cost_of_drinks+cost_of_burger+cost_of_filet+cost_of_chickenburger+cost_of_cheeseburger)*0.15
    totalcost=(cost_of_fries+cost_of_drinks+cost_of_burger+cost_of_filet+cost_of_chickenburger+cost_of_cheeseburger)
    displayabletax="₹"+str("%.2f"%paytax)
    ser_charge=totalcost/99
    servicecharge="₹"+str("%.2f"%ser_charge)
    overallcost="₹"+str("%.2f"%(paytax+totalcost+ser_charge))
    cost.set(cost_of_meal)
    Tax.set(displayabletax)
    service_charge.set(servicecharge)
    subtotal.set(cost_of_meal)
    total.set(overallcost)

   
    

def reset():
    rand.set("")
    fries.set("")
    burger.set("")
    filet.set("")
    subtotal.set("")
    total.set("")
    service_charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    chicken_burger.set("")
    cheese_burger.set("")
def qexit():
    root.destroy()



text_display=Entry(f2,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,
                   bg="powder blue",justify="right")
text_display.grid(columnspan=4)
btn7=Button(f2,font=("arial",20,"bold"),text="7",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(7)).grid(row=2,column=0)
btn8=Button(f2,font=("arial",20,"bold"),text="8",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(8)).grid(row=2,column=1)
btn9=Button(f2,font=("arial",20,"bold"),text="9",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(9)).grid(row=2,column=2)
addition=Button(f2,font=("arial",20,"bold"),text="+",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick("+")).grid(row=2,column=3)
# **************second row*******************************
btn4=Button(f2,font=("arial",20,"bold"),text="4",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(4)).grid(row=3,column=0)
btn5=Button(f2,font=("arial",20,"bold"),text="5",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(5)).grid(row=3,column=1)
btn6=Button(f2,font=("arial",20,"bold"),text="6",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(6)).grid(row=3,column=2)
subtraction=Button(f2,font=("arial",20,"bold"),text="-",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick("-")).grid(row=3,column=3)
# **********************third row***************
btn1=Button(f2,font=("arial",20,"bold"),text="1",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(1)).grid(row=4,column=0)
btn2=Button(f2,font=("arial",20,"bold"),text="2",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(2)).grid(row=4,column=1)
btn3=Button(f2,font=("arial",20,"bold"),text="3",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(3)).grid(row=4,column=2)
multiplication=Button(f2,font=("arial",20,"bold"),text="*",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick("*")).grid(row=4,column=3)
# ******************************fourth row*****************
btn0=Button(f2,font=("arial",20,"bold"),text="0",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick(0)).grid(row=5,column=0)
btnclear=Button(f2,font=("arial",20,"bold"),text="C",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=btncleartext).grid(row=5,column=1)
btnequals=Button(f2,font=("arial",20,"bold"),text="=",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=equals).grid(row=5,column=2)
divison=Button(f2,font=("arial",20,"bold"),text="/",padx=16,pady=16,bd=8,bg="powder blue",fg="black",
            command=lambda:btnclick("/")).grid(row=5,column=3)
# **************************************************************restaurent info 1**********************************
rand=StringVar()
fries=StringVar()
burger=StringVar()
filet=StringVar()
subtotal=StringVar()
total=StringVar()
service_charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
cost=StringVar()
chicken_burger=StringVar()
cheese_burger=StringVar()

lblreference=Label(f1,font=("arial",16,"bold"),text="Reference",bd=16,anchor="nw").grid(row=0,column=0)
textreference=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=rand,bg="powder blue",justify="right")
textreference.grid(row=0,column=1)

lblfries=Label(f1,font=("arial",16,"bold"),text="Large fries",bd=16,anchor="nw").grid(row=1,column=0)
textfries=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=fries,bg="powder blue",justify="right")
textfries.grid(row=1,column=1)

lblburger=Label(f1,font=("arial",16,"bold"),text="Burger_Meal",bd=16,anchor="nw").grid(row=2,column=0)
textburger=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=burger,bg="powder blue",justify="right")
textburger.grid(row=2,column=1)

lblfilet=Label(f1,font=("arial",16,"bold"),text="Filet_o_Meal",bd=16,anchor="nw").grid(row=3,column=0)
textfilet=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=filet,bg="powder blue",justify="right")
textfilet.grid(row=3,column=1)

lblchicken_burger=Label(f1,font=("arial",16,"bold"),text="Chicken_Burger",bd=16,anchor="nw").grid(row=4,column=0)
textchicken_burger=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=chicken_burger,bg="powder blue",justify="right")
textchicken_burger.grid(row=4,column=1)

lblcheese_meal=Label(f1,font=("arial",16,"bold"),text="Cheese_Meal",bd=16,anchor="nw").grid(row=5,column=0)
textcheese_meal=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=cheese_burger,bg="powder blue",justify="right")
textcheese_meal.grid(row=5,column=1)
# **************************************************************restaurent info2**********************************
lbldrinks=Label(f1,font=("arial",16,"bold"),text="Drinks",bd=16,anchor="w").grid(row=0,column=2)
textdrinks=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=Drinks,justify="right")
textdrinks.grid(row=0,column=3)

lblcost=Label(f1,font=("arial",16,"bold"),text="Cost_of_Meal",bd=16,anchor="nw").grid(row=1,column=2)
textcost=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=cost,justify="right")
textcost.grid(row=1,column=3)

lblsubtotal=Label(f1,font=("arial",16,"bold"),text="Sub_Total",bd=16,anchor="nw").grid(row=2,column=2)
textsubtotal=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=subtotal,justify="right")
textsubtotal.grid(row=2,column=3)

lbltax=Label(f1,font=("arial",16,"bold"),text="State_Tax",bd=16,anchor="nw").grid(row=3,column=2)
texttax=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=Tax,justify="right")
texttax.grid(row=3,column=3)

lblservice_charge=Label(f1,font=("arial",16,"bold"),text="Service_Charge",bd=16,anchor="nw").grid(row=4,column=2)
textservice_charge=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=service_charge,justify="right")
textservice_charge.grid(row=4,column=3)

lbltotal=Label(f1,font=("arial",16,"bold"),text="Total_Cost",bd=16,anchor="nw").grid(row=5,column=2)
texttotal=Entry(f1,font=("calibri",16,"bold"),bd=10,insertwidth=4,textvariable=total,justify="right")
texttotal.grid(row=5,column=3)

btntotal=Button(f1,padx=16,pady=8,font=("arial",16,"bold"),bd=16,fg="black",text="Total",width=10,bg="powder blue",
     command=ref)
btntotal.grid(row=7,column=1)
btnreset=Button(f1,padx=16,pady=8,font=("arial",16,"bold"),bd=16,fg="black",text="Reset",width=10,bg="powder blue",
     command=reset)
btnreset.grid(row=7,column=2)
btnexit=Button(f1,padx=16,pady=8,font=("arial",16,"bold"),bd=16,fg="black",text="Exit",width=10,bg="powder blue",
     command=qexit)
btnexit.grid(row=7,column=3)



root.mainloop()
