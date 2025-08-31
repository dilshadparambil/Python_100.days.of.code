from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_label=Label(text='Score:0',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1,pady=20)

        self.canvas=Canvas(bg='White',height=250,width=300,highlightthickness=0)
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text='',
            fill=THEME_COLOR,
            font=('Arial',20,'italic')
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        right_img=PhotoImage(file="./images/true.png")
        self.right_bt=Button(image=right_img,highlightthickness=0,borderwidth=0,command=self.correct)
        self.right_bt.grid(row=2,column=0,pady=20)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_bt = Button(image=wrong_img, highlightthickness=0,borderwidth=0,command=self.incorrect)
        self.wrong_bt.grid(row=2, column=1,pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz finished")
            self.right_bt.config(state='disabled')
            self.wrong_bt.config(state='disabled')


    def correct(self):
        self.feedback(self.quiz.check_answer('True'))


    def incorrect(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self,is_true):
        if is_true:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)


