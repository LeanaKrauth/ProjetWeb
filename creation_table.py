from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chevaux.sqlite3'

db = SQLAlchemy(app)



class cheval(db.Model):
    Id = db.Column('ChevalId', db.Integer, primary_key = True)
    Nom = db.Column(db.String(50))
    Race = db.Column(db.String(50))
    PaysId = db.Column(db.Integer)

    def __init__(self, Id, Nom, Race):
       self.Id = Id
       self.Nom = Nom
       self.Race = Race



class pays(db.Model):
    Id = db.Column('PaysId', db.Integer, primary_key = True)
    Nom = db.Column(db.String(50))
    Palmares = db.Column(db.String(50))

    def __init__(self, Id, Nom, Palmares):
       self.Id = Id
       self.Nom = Nom
       self.Palmares = Palmares



class Cavalier(db.Model):
    Id = db.Column('CavalierId', db.Integer, primary_key = True)
    Nom = db.Column(db.String(50))
    Prenom = db.Column(db.String(50))
    PaysId = db.Column(db.Integer)

    def __init__(self, Id, Nom, Prenom, Pays):
       self.Id = Id
       self.Nom = Nom
       self.Prenom = Prenom
       self.PaysId = PaysId



class couple(db.Model):
    Id = db.Column('CoupleId', db.Integer, primary_key = True)
    CavalierId = db.Column(db.Integer)
    ChevalId = db.Column(db.Integer)
    Palmares = db.Column(db.String(50))
    Dicipline = db.Column(db.String(20))

    def __init__(self, Id, Cavalier, Cheval,Dicipline):
       self.Id = Id
       self.Cavalier = Cavalier
       self.Cheval = Cheval
       self.Palmares = Palmares
       self.Dicipline = Dicipline

db.create_all()

@app.route('/')
def show_all():
   return render_template('show_all.html', chevaux = cheval.query.all() )
