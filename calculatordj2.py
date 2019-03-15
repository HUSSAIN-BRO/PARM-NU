from tkinter import *
root=Tk()
root.title("calculator two")
root.geometry()
frame=Frame(root)
frame.pack()
topframe=Frame(root)
topframe.pack(side=TOP)
num1=StringVar()
operator=""

def clearall():
    global operator
    operator=""
    num1.set(operator)
def text_input(numbers):
    global operator
    operator=operator+str(numbers)
    num1.set(operator)
def equals():
    global operator
    sumup=float(eval(operator))
    num1.set(sumup)
    operator=""
def clear():
    global operator
    n=len(operator)
    operator=operator[0:n-1]
    num1.set(operator)

textdisplay=Entry(frame,textvariable=num1,bd=30,insertwidth=1,font=30,bg="powder blue",relief=SUNKEN,width=29,justify="right")
textdisplay.pack(side=TOP)
b1=Button(topframe,bd=8,padx=12,pady=12,text="1",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("1"))
b1.pack(side=LEFT)
b2=Button(topframe,bd=8,padx=12,pady=12,text="2",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("2"))
b2.pack(side=LEFT)
b3=Button(topframe,bd=8,padx=12,pady=12,text="3",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("3"))
b3.pack(side=LEFT)
b4=Button(topframe,bd=8,padx=12,pady=12,text="(",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("("))
b4.pack(side=LEFT)
b5=Button(topframe,bd=8,padx=13,pady=12,text=")",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input(")"))
b5.pack(side=LEFT)
# **********************row2***********************
f1=Frame(root)
f1.pack(side=TOP)
b6=Button(f1,bd=8,padx=12,pady=12,text="4",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("4"))
b6.pack(side=LEFT)
b7=Button(f1,bd=8,padx=12,pady=12,text="5",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("5"))
b7.pack(side=LEFT)
b8=Button(f1,bd=8,padx=12,pady=12,text="6",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("6"))
b8.pack(side=LEFT)
bmultiply=Button(f1,bd=8,padx=12,pady=12,text="*",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("*"))
bmultiply.pack(side=LEFT)
bdivison=Button(f1,bd=8,padx=13,pady=12,text="/",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("/"))
bdivison.pack(side=LEFT)
# **************************row3*****************
f2=Frame(root)
f2.pack(side=TOP)
b9=Button(f2,bd=8,padx=12,pady=12,text="7",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("7"))
b9.pack(side=LEFT)
b10=Button(f2,bd=8,padx=12,pady=12,text="8",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("8"))
b10.pack(side=LEFT)
b11=Button(f2,bd=8,padx=12,pady=12,text="9",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("9"))
b11.pack(side=LEFT)
bminus=Button(f2,bd=8,padx=13,pady=12,text="-",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("-"))
bminus.pack(side=LEFT)
bplus=Button(f2,bd=8,padx=11,pady=12,text="+",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("+"))
bplus.pack(side=LEFT)
# *********************row 4*****************
f3=Frame(root)
f3.pack(side=TOP)
bdot=Button(f3,bd=8,padx=15,pady=12,text=".",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("."))
bdot.pack(side=LEFT)
b12=Button(f3,bd=8,padx=12,pady=12,text="0",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=lambda:text_input("0"))
b12.pack(side=LEFT)
bclearall=Button(f3,bd=8,padx=3,pady=12,text="CE",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,
                 command=clearall)
bclearall.pack(side=LEFT)
bclear=Button(f3,bd=8,padx=8,pady=12,text="C",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=clear)
bclear.pack(side=LEFT)
bequals=Button(f3,bd=8,padx=12,pady=12,text="=",font=("arial",16,"bold"),bg="powder blue",relief=RAISED,command=equals)
bequals.pack(side=LEFT)





root.mainloop()