from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Bonjour tout le monde !</h1>'

@app.route("/user/<name>")
def user(name):
    return '<h3>Hello, %s</h3>' % name

if __name__ == '__main__':
    app.run(debug=True)