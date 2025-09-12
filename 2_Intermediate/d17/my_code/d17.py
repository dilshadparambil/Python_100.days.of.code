# Quiz Game
# You need to download question_model.py, data.py, quiz_brain.py from Intermediate/d17/my_code folder in order to run this file

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for item in question_data:
    question = Question(item["text"],item["answer"])
    question_bank.append(question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("\nYou have Completed The Quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_no}")