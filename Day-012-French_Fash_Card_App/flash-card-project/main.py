from tkinter import *
import pandas
from generate_card import GenerateInterface

bg_color = "#B1DDC6"

#-------------------------------- UI Setup ------------------------------------#

window = Tk()
window.title("Flashy")
window.config(bg=bg_color,padx=50,pady=50)

generate_card = GenerateInterface()


window.mainloop()