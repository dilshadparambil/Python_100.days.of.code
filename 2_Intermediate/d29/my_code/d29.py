# Password Manager (GUI App) 
# download files inside Intermediate/d29/my_code

import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list =  [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password="".join(password_list)
    passwd_text.delete(0,'end')
    passwd_text.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website=web_text.get().strip()
    username=username_text.get().strip()
    password=passwd_text.get().strip()
    if website=="" or username=="" or password=="" :
        messagebox.showerror(title='Oops',message='Please dont leave any fields empty!')
    else:
        conformation= messagebox.askokcancel(title='',message=website,detail=f"You have entered the following data:\nEmail:{username}\nPassword:{password}\nIs it ok to save?")
        if conformation:
            with open("data.txt",'a') as file:
                file.write(f"{website}  |  {username}  |  {password}")
                file.write('\n')
                web_text.delete(0, 'end')
                passwd_text.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

scr=tkinter.Tk()
scr.title("Password Manager")
scr.config(padx=50,pady=50)

logo=tkinter.PhotoImage(file="./logo.png")

canvas=tkinter.Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

label1=tkinter.Label(text="Website:")
label1.grid(row=1,column=0)
label1.focus()
web_text=tkinter.Entry()
web_text.grid(row=1,column=1,columnspan=2,sticky="EW")

label2=tkinter.Label(text="Email/Username:")
label2.grid(row=2,column=0)
username_text=tkinter.Entry()
username_text.insert(index=0,string="dilshadkareemparambil@gmail.com")
username_text.grid(row=2,column=1,columnspan=2,sticky="EW")

label3=tkinter.Label(text="Password:")
label3.grid(row=3,column=0)
passwd_text=tkinter.Entry()
passwd_text.grid(row=3,column=1,sticky="EW")

gen_passwd=tkinter.Button(text="Generate Password",command=generate_passwd)
gen_passwd.grid(row=3,column=2,sticky="EW")

add_passwd=tkinter.Button(text="Add",command=save_pass)
add_passwd.grid(row=4,column=1,columnspan=2,sticky="EW")

scr.mainloop()