from flask.ext.script import Manager
from flask import Flask


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>' \
           '<p>I am using a manager.</p> Yes we can!'


if __name__ == '__main__':
    manager.run()