# Password Manager (GUI App with Search)
# download files inside Intermediate/d30/my_code

import json
from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    data_dict={website:{"Email":email,"Password":password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(data_dict, data_file, indent=4)
        else:
            data.update(data_dict)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_passwd():
    website = website_entry.get().strip()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(message=f"No data file found")
    else:
        if website=='':
            messagebox.showinfo(message=f"please enter a website name")
        elif website in data:
            messagebox.showinfo(message=f"Email:{data[website]["Email"]}\nPassword:{data[website]["Password"]}")
        else:
            messagebox.showinfo(message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry()
website_entry.grid(row=1, column=1,sticky='EW')
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2,sticky='EW')
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1,sticky='EW')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2,sticky='EW')
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky='EW')
search_button = Button(text="Search", command=search_passwd)
search_button.grid(row=1, column=2,sticky='EW')

window.mainloop()
