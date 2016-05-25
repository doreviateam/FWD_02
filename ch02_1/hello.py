# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

doreviateam = Flask(__name__)

@doreviateam.route('/')
def index():
    return render_template('index.html')

@doreviateam.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

if __name__ == '__main__':
    doreviateam.run(debug=True)