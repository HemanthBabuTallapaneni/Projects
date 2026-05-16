from flask import Flask
import random

random_number = random.randint(1, 10)
print(random_number)
app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1 style = "text-align: center">Guess a number between 1 and 10</h1>'
            '<img style = "align: center "src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzU4OHJuZGk2d2Q4ZGE5d242Y2o3M2kxY2c5ZjlwdjhiNzNibTNwZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tBvPFCFQHSpEI/giphy.gif">'
            )
@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return ("<h1 style='color: red'> Too high! </h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    elif guess < random_number:
        return ("<h1 style='color: green'> Too low! </h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    else:
        return ("<h1 style='color: blue'> You Found me!! </h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")

if __name__ == '__main__':
    app.run(debug=True)
