from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date_created = db.Column('Created', db.Date)
    