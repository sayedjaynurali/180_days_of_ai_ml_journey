from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100,height=100)

def convert_to_km():
    global entry
    to_miles = int(entry.get())
    text2 = Label(text=(to_miles//1.609),font=("arial",10,"normal"))
    text2.grid(row=1,column=1)

entry = Entry(width=10)
entry.grid(row=0,column=1)

text0 = Label(text="miles",font=("arial",10,"normal"))
text0.grid(row=0,column=2)

text1 = Label(text="is equal to",font=("arial",10,"normal"))
text1.grid(row=1,column=0)

text2 = Label(text="0",font=("arial",10,"normal"))
text2.grid(row=1,column=1)

text3 = Label(text="km",font=("arial",10,"normal"))
text3.grid(row=1,column=2)

button = Button(text="Calculate",command=convert_to_km)
button.grid(row=2,column=1)

window.mainloop()