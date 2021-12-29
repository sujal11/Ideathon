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

@app.route('/registrations2')
def register2():
    return render_template("registrations2.html")

@app.route('/add-user', methods = ['POST'])
def addUser():
    try :
        teamType=request.form.get('teamType')
        members=request.form.get('members')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        education = request.form.get('education')
        state = request.form.get('state')

        if name and email and phone and age and education and state:

            if user.query.filter_by(email=email).first():
                return("Email ID already Exists")
            else:
                db.session.add(user(name=name, email=email, phone=phone, age=age, education=education, state=state, avatar_id=avatar))
                db.session.commit()
                return("Thank you for registering")
        else:
            return("Please fill all the fields")
    except Exception as e:
        print(e)
        return("Something went wrong")


if __name__ == '__main__':
    app.run(debug=True)