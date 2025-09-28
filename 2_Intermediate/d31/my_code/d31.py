# Flash Card App
# download files inside Intermediate/d31/my_code

from operator import index
from tkinter import *
import pandas
from random import *

try:
    data=pandas.read_csv('./data/words_to_learn.csv')
except pandas.errors.EmptyDataError:
    data = pandas.read_csv('./data/french_words.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')


data=data.to_dict(orient='records')
print(data)
current_card={}

def click_yes():
    try:
        data.remove(current_card)
    except ValueError:
        pass
    else:
        df=pandas.DataFrame(data)
        df.to_csv("./data/words_to_learn.csv", mode="w", index=False)
        random_word()

def random_word():
    global current_card,timer
    window.after_cancel(timer)
    try:
        current_card = choice(data)
    except IndexError:
        card_canvas.itemconfig(img, image=card_front)
        card_canvas.itemconfig(title, text='')
        card_canvas.itemconfig(word, text="You Have finished", fill='black')
    else:
        card_canvas.itemconfig(img, image=card_front)
        card_canvas.itemconfig(title, text='French',fill='black')
        card_canvas.itemconfig(word,text=current_card['French'],fill='black')
        timer=window.after(3000, func=random_word_eng)

def random_word_eng():
    global current_card
    card_canvas.itemconfig(img, image=card_back)
    card_canvas.itemconfig(title, text='English',fill='white')
    card_canvas.itemconfig(word, text=current_card['English'],fill='white')



BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer=window.after(3000, func=random_word_eng)


card_front=PhotoImage(file='./images/card_front.png')
card_back=PhotoImage(file='./images/card_back.png')
right_bt_image=PhotoImage(file='./images/right.png')
wrong_bt_image=PhotoImage(file='./images/wrong.png')

card_canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
img=card_canvas.create_image(400,263,image=card_front)
card_canvas.grid(row=0,column=0,columnspan=2)
title=card_canvas.create_text(400,150,font=("Ariel",40,"italic"))
word=card_canvas.create_text(400,263,font=("Ariel",60,"bold"))

right_button=Button(image=right_bt_image,borderwidth=0,highlightthickness=0,command=click_yes)
right_button.grid(row=1,column=1)

wrong_button=Button(image=wrong_bt_image,borderwidth=0,highlightthickness=0,command=random_word)
wrong_button.grid(row=1,column=0)

random_word()

window.mainloop()