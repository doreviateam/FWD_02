from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('http://translate.google.com')
    # response = make_response('<p>This document carries a cookie!</p>')
    # response.set_cookie('answer', '42')
    # return response
#     user_agent = request.headers.get('user-agent')  # .get(User-Agent)
#     return '<h1>Bonjour tout le monde !</h1>' \
#            '<p>Your browser agent is {}</p>'.format(user_agent)

@app.route("/user/<name>")
def user(name):
    return '<h3>Hello, %s</h3>' % name

if __name__ == '__main__':
    app.run(debug=True)





