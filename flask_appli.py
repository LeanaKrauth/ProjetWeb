from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/cavaliers.html')
def cavaliers(name=None):
    return render_template('cavaliers.html', name=name)

@app.route('/hello/pays.html')
def pays(name=None):
    return render_template('pays.html', name=name)

@app.route('/hello/chevaux.html')
def chevaux(name=None):
    return render_template('chevaux.html', name=name)

@app.route('/hello/couples.html')
def couples(name=None):
    return render_template('couples.html', name=name)



