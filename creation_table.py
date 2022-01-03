from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chevaux.sqlite3'

db = SQLAlchemy(app)

class cheval(db.Model):
    Id = db.Column('cheval_id', db.Integer, primary_key = True)
    Nom = db.Column(db.String(50))
    Race = db.Column(db.String(50))
    Dicipline = db.Column(db.String(20))
#    PaysId = db.Column(db.Integere)   cle etrangere

    def __init__(self, name, city, addr,pin):
       self.Id = Id
       self.Nom = nom
       self.Race = Race
       self.Dicipline = Dicipline
db.create_all()