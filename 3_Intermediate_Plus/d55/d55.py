# Higher Lower URLs (Flask Project)

import random
from flask import Flask

app= Flask(__name__)

@app.route('/')
def question():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTE2dWJ2NnFjZ2hiYTloeGhyYmVhZmVraDdzdWppenpqNDgzMzB5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif" width=500>')


guess_num=random.randint(0,9)

@app.route('/<int:num>')
def answer(num):
    if num>guess_num:
        text=('<h1 style="color: red;">Too High,Try Again<h1>'
              '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500>')
    elif num<guess_num:
        text=('<h1 style="color: blue;">Too low,Try Again<h1>'
              '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500>')
    else:
        text=('<h1 style="color: green;">You Found Me<h1>'
              '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500>')

    return text




if __name__=='__main__':
    app.run(debug=True)