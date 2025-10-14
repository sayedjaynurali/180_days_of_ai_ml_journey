from tkinter import *

def button_clicked():
    global entry
    my_label.config(text=entry.get())

window = Tk()
window.title("My first TK Window")
window.minsize(width=500,height=300)

my_label = Label(text="My first Text", font=("Arial",24,"italic"))
my_label.grid(column=0,row=0,padx=20,pady=20)

button = Button(text="button1",command=button_clicked)
button.grid(column=2,row=2)

button = Button(text="button2",command=button_clicked)
button.grid(column=3,row=1)

entry = Entry(width=10)
entry.place(x=400,y=0)


window.mainloop()