from tkinter import *
from tkinter import messagebox
import pyperclip
import string
from random import randint, shuffle, choice
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list('!#$%&()*+')

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(numbers) for _ in range(randint(2,4))]
    password_numbers = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    
    pyperclip.copy(password)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get().strip().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{"email":email,"password":password}}

    if not website or not email or not password:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title="Website",message=f"Website: {website}\nEmail/Username: {email}\nPassword: {password}\nIs this OK to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    #Reading the data
                    data = json.load(data_file)
                    #Updating the data
                    data.update(new_data)
            
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)

            else:
                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data,data_file,indent=4)
            
            finally:
                website_entry.delete(0,'end')
                email_entry.delete(0,'end')
                email_entry.insert(0,"user@email.com")
                password_entry.delete(0,'end')
                
                messagebox.showinfo(message="Credentials Saved!")

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #

def find_password():
    website = website_entry.get().strip().capitalize()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file) # Return a dictionary
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Website not found",message=f"No Details for '{website}' found!")

# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=20)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus() 

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0,"user@email.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = Button(text="Search",command=find_password)
search_button.grid(row=1, column=2, sticky="NSEW")

generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(row=3, column=2, sticky="NSEW")

add_button = Button(text="Add",command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="NSEW", pady=5)

window.mainloop()