import os
from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sonakshi:sonakshi@localhost/ideathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# two decorators, same function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registration')
def register():
    return render_template("registrations.html")

if __name__ == '__main__':
    app.run(debug=True)