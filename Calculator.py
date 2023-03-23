from tkinter import*

def addSelfVal(buttonPress):
    collect = enterDigit["text"]
    print(collect)
    print(buttonPress)
    enterDigit["text"] += buttonPress

def calculate():
    collect = eval(enterDigit["text"])
    print(collect)
    enterDigit["text"] = str(collect)

def clearEntry():
    enterDigit["text"] = ""

def removeLast():
    collect = enterDigit["text"]
    enterDigit["text"] = collect[:-1]




root = Tk()
root.geometry("350x400")
root.title("Calculator")
root.resizable(False,False)


enterDigit = Label(root,fg="white",bg="black",font=("Arial",20),justify=RIGHT)
enterDigit.pack(fill="x")

Buttons = Frame(root)
Buttons.pack()

syncH = 1
syncW = 3
syncFont = ("Arial",20)

#x²
#numbers
Button(Buttons,text="%",font=syncFont,width=syncW,height=syncH,command=lambda nV="%":addSelfVal(nV)).grid(row=0,column=0)
Button(Buttons,text="𝑥²",font=syncFont,width=syncW,height=syncH,command=lambda nV="**2":addSelfVal(nV)).grid(row=0,column=1)
Button(Buttons,text="C",font=syncFont,width=syncW,height=syncH,command=clearEntry).grid(row=0,column=2)
Button(Buttons,text="←",font=syncFont,width=syncW,height=syncH,command=removeLast).grid(row=0,column=3)

Button(Buttons,text="7",font=syncFont,width=syncW,height=syncH,command=lambda nV="7":addSelfVal(nV)).grid(row=1,column=0)
Button(Buttons,text="8",font=syncFont,width=syncW,height=syncH,command=lambda nV="8":addSelfVal(nV)).grid(row=1,column=1)
Button(Buttons,text="9",font=syncFont,width=syncW,height=syncH,command=lambda nV="9":addSelfVal(nV)).grid(row=1,column=2)
Button(Buttons,text="4",font=syncFont,width=syncW,height=syncH,command=lambda nV="4":addSelfVal(nV)).grid(row=2,column=0)
Button(Buttons,text="5",font=syncFont,width=syncW,height=syncH,command=lambda nV="5":addSelfVal(nV)).grid(row=2,column=1)
Button(Buttons,text="6",font=syncFont,width=syncW,height=syncH,command=lambda nV="6":addSelfVal(nV)).grid(row=2,column=2)
Button(Buttons,text="1",font=syncFont,width=syncW,height=syncH,command=lambda nV="1":addSelfVal(nV)).grid(row=3,column=0)
Button(Buttons,text="2",font=syncFont,width=syncW,height=syncH,command=lambda nV="2":addSelfVal(nV)).grid(row=3,column=1)
Button(Buttons,text="3",font=syncFont,width=syncW,height=syncH,command=lambda nV="3":addSelfVal(nV)).grid(row=3,column=2)
Button(Buttons,text="0",font=syncFont,width=syncW,height=syncH,command=lambda nV="0":addSelfVal(nV)).grid(row=4,column=1)
Button(Buttons,text=".",font=syncFont,width=syncW,height=syncH,command=lambda nV=".":addSelfVal(nV)).grid(row=4,column=2)


#operand
Button(Buttons,text="×",font=syncFont,width=syncW,height=syncH,command=lambda nV="*":addSelfVal(nV)).grid(row=1,column=3)
Button(Buttons,text="-",font=syncFont,width=syncW,height=syncH,command=lambda nV="-":addSelfVal(nV)).grid(row=2,column=3)
Button(Buttons,text="+",font=syncFont,width=syncW,height=syncH,command=lambda nV="+":addSelfVal(nV)).grid(row=3,column=3)
Button(Buttons,text="=",font=syncFont,width=syncW,height=syncH,command=calculate).grid(row=4,column=3)






root.mainloop()
