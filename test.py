"""test Flask with this"""

from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def hello2():
    return "<h1>Page d'accueil</h1>"

@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'


#@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)
