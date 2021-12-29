import os
from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///ideathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import participants, team

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
        tname=request.form.get('tname')
        tlname = request.form.get('tlname')
        tlemail = request.form.get('tlemail')
        tlphone = request.form.get('tlphone')
        organisation = request.form.get('organization')
        problem_statement = request.form.get('problemStatement')

        if teamType and members and tname and tlname and tlemail and tlphone and organisation and problem_statement:

            if participants.query.filter_by(email=tlemail).first():
                return("Email ID already Exists")
            else:
                db.session.add(team(team_name=tname, team_members=members, team_type=teamType, problem_statement=problem_statement))
                db.session.commit()
                teams=team.query.filter_by(team_name=tname).first()
                db.session.add(participants(name=tlname, email=tlemail, phone=tlphone, organization=organisation, team_name=tname,is_leader=True, team_id=teams.id))
                db.session.commit()
                return("Thank you for registering")
        else:
            return("Please fill all the fields")
    except Exception as e:
        print(e)
        return("Something went wrong")


if __name__ == '__main__':
    app.run(debug=True)