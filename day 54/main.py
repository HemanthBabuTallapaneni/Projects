import time
current_time = time.time()
print(current_time)
def speed_calc_decorator():
    pass

def fast_function():
    for i in range(10000000):
        i * i

def slow_function():
    for i in range(100000000):
        i * i
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
