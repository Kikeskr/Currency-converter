from tkinter import *
from tkinter import messagebox as mb
#3hours=56min
#11.00
#20 mins used for brainstorming the draft into existence
import sys
import re

currency=Tk()
currency.geometry("450x500")
currency.title("Currency converter")
frame1=Frame(currency,bg="black",height=97,width=700)
frame2=Frame(currency,bg="black",height=97,width=700)
frame3=Frame(currency,bg="black",height=97,width=700)

def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)
        expression = ""
    except:

        equation.set("Syntax error ")
        expression = ""
expression=""
equation = StringVar()
def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)

def nth():
    enaira=EntryNGN.get()
    en=760
    eusd=EntryUSD.get()
    if enaira == "":

        mon="Please enter something"
    ru=str(mon)
    ansentry.config(text=ru)
def exit():

    sys.exit()
def clear():
    ansentry.config(text="")
def NGNturn():

#    mb.showerror("showerror", "Error")
    enaira=EntryNGN.get()
    en=725.00
    eusd=EntryUSD.get()

    if enaira != "" :
        moneyin=float(enaira) / float(en)
    ran=str(moneyin)
    ansentry.config(text=ran)

def USDturn():
    #clear()
    eusd = EntryUSD.get()
    es = 725.00
    if eusd != "":
        usdin = float(eusd) * float(es)
        run = str(usdin )
        ansentry.config(text=run)
def Rateturn():
    eoc = ocentry.get()
    erate = rateentry.get()
    if eoc!="" and erate!="":
        rating=float(eoc)*float(erate)
        rin=str(rating)
        ansentry.config(text=rin)

mb= Menu(currency)
filemenu = Menu(mb)
editmenu = Menu(mb)
viewmenu = Menu(mb)
runmenu = Menu(mb)
helpmenu = Menu(mb)
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)
mb.add_cascade(label="File", menu=filemenu)
editmenu.add_command(label="Light Mode")
editmenu.add_command(label="Dark Mode")
mb.add_cascade(label="View", menu=editmenu)
runmenu.add_command(label="ClearAll",command=clear)
mb.add_cascade(label="Clear", menu=runmenu)
helpmenu.add_command(label="Press F1 for enquires")
mb.add_cascade(label="Help", menu=helpmenu)
currency.config(menu=mb)

frame1.propagate(0)
frame2.propagate(0)
frame3.propagate(0)
frame1.pack()
frame2.pack()
frame3.pack()
#label naira
labelN=Label(frame1,text="",bg="green",fg="White",font=("Aerial",50),width=1)
labelNG=Label(frame1,text="",bg="white",fg="White",font=("Aerial",50),width=1)
labelNGN=Label(frame1,text="",bg="green",fg="White",font=("Aerial",50),width=1)
labelcn1=Label(frame1,text="NGN",bg="black",fg="white",font=("Papyrus",15),height=3)
#label dollar
labellogo1=Label(frame1,text="",bg="red",fg="white",font=("Rockwell",15),width=1,height=3)
labellogo2=Label(frame1,text="",bg="white",fg="white",font=("Rockwell",15),width=1,height=3)
labellogo3=Label(frame1,text="$",bg="red",fg="green",font=("Rockwell",22),width=2,height=2)
labellogo4=Label(frame1,text="",bg="white",fg="white",font=("Rockwell",15),width=1,height=3)
labellogo5=Label(frame1,text="",bg="red",fg="white",font=("Rockwell",15),width=1,height=3)
labellogo8=Label(frame1,text="",bg="white",fg="white",font=("Rockwell",15),width=1,height=3)
labellogo6=Label(frame1,text="",bg="red",fg="white",font=("Rockwell",15),width=1,height=3)
labelUSD=Label(frame1,text="USD",bg="black",fg="white",font=("Papyrus",15),height=3)
#label other currencies
#entry
EntryNGN=Entry(frame1,bg="black",fg="white",width=7,font=("Times New Roman",25))
EntryUSD=Entry(frame1,bg="black",fg="white",width=7,font=("Times New Roman",25))
#other currency label and text
octext=Label(frame2,text="OTHER CURRENCIES",bg="black",fg="white",font=("Arial Rounded MT Bold",12))
ocentry=Entry(frame2,bg="black",fg="white",font=("Times New Roman",25),width=10)
#rate label and text
ratetext=Label(frame2,text="RATE",bg="black",fg="white",font=("Arial Rounded MT Bold",12))
rateentry=Entry(frame2,bg="black",fg="white",font=("Times New Roman",25),width=10)
#submit forum
ansbutton=Button(frame3,text="Convert to USD",bg="green",fg="black",font=("Aerial",7),command=NGNturn)
ansbutton2=Button(frame3,text="Convert to Naira",bg="green",fg="black",font=("Aerial",7),command=USDturn)
ansbutton3=Button(frame3,text="Convert to other currencies",bg="green",fg="black",font=("Aerial",7),command=Rateturn)#command=lambda: press("*"))
ansentry=Label(frame3,text="",bg="black",fg="orange",width=30,height=3,font=("Times New Roman",15))
ansentr=Label(frame3,text="Total:",bg="black",fg="orange",width=5,height=4,font=("Times New Roman",15))

labelN.pack(side="left")
labelNG.pack(side="left")
labelNGN.pack(side="left")
labelcn1.pack(side="left")
EntryNGN.pack(side="left")
labellogo1.pack(side="right")
labellogo4.pack(side="right")
labellogo5.pack(side="right")
labellogo8.pack(side="right")
labellogo6.pack(side="right")
labellogo3.pack(side="right")
labelUSD.pack(side="right")
labelUSD.pack(side="right")
EntryUSD.pack(side="right")
octext.pack(side="left")
ocentry.pack(side="left")
ratetext.pack(side="left",padx=40)
rateentry.pack(side="left")
ansbutton.pack(side="left",padx=15)
ansbutton2.pack(side="left",padx=15)
ansbutton3.pack(side="left",padx=15)
ansentr.pack(side="left")
ansentry.pack(side="left")


currency.mainloop()