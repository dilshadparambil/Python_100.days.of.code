# Mile to Km Converter (GUI) 
from tkinter import *

scr=Tk()
scr.title("Mile To Km Converter")

scr.config(padx=20,pady=20)

textbox=Entry()
textbox.config(width=8)
textbox.insert(END,string="0")
textbox.grid(column=1,row=0)

label1=Label()
label1.config(text="Miles")
label1.grid(column=2,row=0)

label2=Label()
label2.config(text="is equal to")
label2.grid(column=0,row=1)

label3=Label()
label3.config(text="0")
label3.grid(column=1,row=1)

label4=Label()
label4.config(text="Km")
label4.grid(column=2,row=1)



def button_click():

    usr_input=float(textbox.get())
    mile_2_km=round(usr_input*1.609,2)
    label3.config(text=mile_2_km)



button1=Button()
button1.config(text="Calculate",width=4,command=button_click)
button1.grid(column=1,row=2)




scr.mainloop()
