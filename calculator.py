from tkinter import *
root=Tk()
root.geometry("600x300+0+0")
root.title("Calculator")
root.wm_minsize(width=600,height=300)
text_input=StringVar()
operator=""



f2=Frame(root,width=600,height=300,bg="powder blue",relief=SUNKEN)
f2.pack(side=TOP)

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
root.mainloop()
