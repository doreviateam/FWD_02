# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap

doreviateam = Flask(__name__)
bootstrap = Bootstrap(doreviateam)

@doreviateam.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@doreviateam.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@doreviateam.route('/')
def index():
    return render_template('index.html')

@doreviateam.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

if __name__ == '__main__':
    doreviateam.run(debug=True)