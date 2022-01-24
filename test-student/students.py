from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'e' #os.urandom(12).hex()

db = SQLAlchemy(app)
class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
    def __repr__(self):
        return '<User %r>' % self.name

'''
for i in range(11,15):
    me = Student('bob', 'paris', '5 rue de paris', str(i))
    db.session.add(me)
'''

db.session.commit()

db.create_all()

@app.route('/')
def show_all():
   return render_template('show_all.html', students = Student.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = Student(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')