# Pomodoro Timer (GUI)
# download files inside Intermediate/d28/my_code

import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
check_mark=""
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer,reps,check_mark
    scr.after_cancel(timer)
    reps=0
    check_mark=""
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text=check_mark)
    label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps % 8 == 0:
        label.config(text="LONG_BREAK",fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps%2!=0:
        label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps%2==0:
        label.config(text="SHORT_BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_mark,timer

    minutes=count//60
    seconds=count%60
    if seconds<10:
        seconds=f'0{seconds}'

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count>0:
        timer=scr.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            check_mark+="✔"
            tick_label.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #
scr=tkinter.Tk()
scr.title("Pomodoro Timer")
scr.config(padx=100,pady=100,background=YELLOW)

tomato=tkinter.PhotoImage(file="./tomato.png")

label=tkinter.Label()
label.config(text="Timer",font=(FONT_NAME,50,'normal'),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

canvas=tkinter.Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,'bold'))
canvas.grid(column=1,row=1)

start_button=tkinter.Button()
start_button.config(text='start',highlightbackground=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=tkinter.Button()
reset_button.config(text='Reset',highlightbackground=YELLOW,command=reset_timer)
reset_button.grid(column=2,row=2)

tick_label=tkinter.Label()
tick_label.config(fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)




scr.mainloop()
