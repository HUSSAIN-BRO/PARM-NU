import sys
from tkinter import *
def clear():
    global operator
    operator=""
    num1.set(operator)

root=Tk()
root.title("calculator")
frame=Frame(root)
frame.pack()
num1=StringVar()
operator=""
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    num1.set(operator)

def equals():
    global operator
    sumup=float(eval(operator))
    num1.set(sumup)
    operator=""
topframe=Frame(root)
topframe.pack(side=TOP)
textdisplay=Entry(frame,textvariable=num1,bd=30,insertwidth=1,font=30,bg="powder blue",relief=SUNKEN,justify="right")
textdisplay.pack(side=TOP)
button1=Button(topframe,text="1",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("1"),bg="powder blue",relief=RAISED)
button1.pack(side=LEFT)
button2=Button(topframe,text="2",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("2"),bg="powder blue",relief=RAISED)
button2.pack(side=LEFT)
button3=Button(topframe,text="3",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("3"),bg="powder blue",relief=RAISED)
button3.pack(side=LEFT)
button4=Button(topframe,text="4",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("4"),bg="powder blue",relief=RAISED)
button4.pack(side=LEFT)
# ********************row2************
f1=Frame(root)
f1.pack(side=TOP)
button5=Button(f1,text="5",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("5"),bg="powder blue",relief=RAISED)
button5.pack(side=LEFT)
button6=Button(f1,text="6",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("6"),bg="powder blue",relief=RAISED)
button6.pack(side=LEFT)
button7=Button(f1,text="7",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("7"),bg="powder blue",relief=RAISED)
button7.pack(side=LEFT)
button8=Button(f1,text="8",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("8"),bg="powder blue",relief=RAISED)
button8.pack(side=LEFT)
# ****************row 3**************8
f2=Frame(root)
f2.pack(side=TOP)
button9=Button(f2,text="9",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("9"),bg="powder blue",relief=RAISED)
button9.pack(side=LEFT)
button0=Button(f2,text="0",bd=8,padx=16,pady=16,fg="black",font=30,command=lambda:btnclick("0"),bg="powder blue",relief=RAISED)
button0.pack(side=LEFT)
buttonclear=Button(f2,text="C",bd=8,padx=16,pady=16,fg="black",font=30,command=clear,bg="powder blue",relief=RAISED)
buttonclear.pack(side=LEFT)
buttonequals=Button(f2,text="=",bd=8,padx=16,pady=16,fg="black",font=30,command=equals,bg="powder blue",relief=RAISED)
buttonequals.pack(side=LEFT)
# *********************row4*****************
f3=Frame(root)
f3.pack(side=TOP)
buttonmultiply=Button(f3,text="*",bd=8,padx=18,pady=18,fg="black",font=30,command=lambda:btnclick("*"),bg="powder blue",relief=RAISED)
buttonmultiply.pack(side=LEFT)
buttondivison=Button(f3,text="/",bd=8,padx=18,pady=18,fg="black",font=30,command=lambda:btnclick("/"),bg="powder blue",relief=RAISED)
buttondivison.pack(side=LEFT)
buttonaddition=Button(f3,text="+",bd=8,padx=18,pady=18,fg="black",font=30,command=lambda:btnclick("+"),bg="powder blue",relief=RAISED)
buttonaddition.pack(side=LEFT)
buttonminus=Button(f3,text="-",bd=8,padx=18,pady=18,fg="black",font=30,command=lambda:btnclick("-"),bg="powder blue",relief=RAISED)
buttonminus.pack(side=LEFT)


root.mainloop()