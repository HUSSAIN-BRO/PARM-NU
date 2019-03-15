from tkinter import *
root=Tk()
root.title("LOAN CALCULATOR")
root.geometry("500x210")
root.wm_minsize(width=500,height=100)
root.wm_maxsize(width=500,height=300)
def showinterest():
   p=float(e1.get())
   n=float(e2.get())
   r=float(e3.get())/100*12
   si=p*n*r
l1=Label(root,text="ENTER PRINCIPAL AMOUNT-->",font=("calibri",14,"bold"),fg="green")
l2=Label(root,text="ENTER TIME IN MONTHS-->",font=("calibri",14,"bold"),fg="green")
l3=Label(root,text="ENTER RATE OF INTEREST-->",font=("calibri",14,"bold"),fg="green")
l1.place(x=10,y=10)
l2.place(x=10,y=60)
l3.place(x=10,y=110)
e1=Entry(root,font=("calibri",14,"bold"),borderwidth=2,relief="solid",bg="silver")
e2=Entry(root,font=("calibri",14,"bold"),borderwidth=2,relief="solid",bg="silver")
e3=Entry(root,font=("calibri",14,"bold"),borderwidth=2,relief="solid",bg="silver")
e4=Entry(root,font=("calibri",14,"bold"),borderwidth=2,relief="solid",bg="silver")
e1.place(x=270,y=10)
e2.place(x=270,y=60)
e3.place(x=270,y=110)
e4.place(x=270,y=160)
b=Button(root,text="CALCULATE",width=10,height=1,font=("calibri",14,"bold"),bg="red",fg="black",command=showinterest)
b.place(x=10,y=160)




root.mainloop()