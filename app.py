import os
from flask import Flask, render_template, request, redirect,url_for
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sujal:sujal@localhost/ideathon'
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

@app.route('/registrations2/<idd>/<members>')
def register2(members,idd):
    return render_template("registrations2.html",members=members, id=idd)

@app.route('/add-user', methods = ['POST','GET'])
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
                return ("true")
        else:
            return("Please fill all the fields")
    except Exception as e:
        print(e)
        return("Something went wrong")

@app.route('/add-teamates', methods = ['POST','GET'])
def addteamates():
    try :
        members=int(request.form.get('members'))
        idd=request.form.get('id')
        team_member_name=[]
        team_member_email=[]
        team_member_phone=[]
        for i in range(members):
            x=request.form.get('member_name'+str(i))
            y=request.form.get('member_email'+str(i))
            z=request.form.get('member_phone'+str(i))
            team_member_name.append(x)
            team_member_email.append(y)
            team_member_phone.append(z)
        for i in range(len(team_member_name)):
            if team_member_name[i] and team_member_email[i] and team_member_phone[i]:

                if participants.query.filter_by(email=team_member_email[i]).first():
                    return("Email ID already Exists")
                else:
                    teams=team.query.filter_by(team_name=idd).first()
                    participant=participants.query.filter_by(team_name=idd).first()
                    db.session.add(participants(name=team_member_name[i], email=team_member_email[i], phone=team_member_phone[i], organization=participant.organization, team_name=teams.team_name,is_leader=False, team_id=teams.id))
                    db.session.commit()
                    return ("true")
            else:
                return("Please fill all the fields")
    except Exception as e:
        print(e)
        return("Something went wrong")

@app.route('/attendees')
def attendees():
    teams=team.query.all()
    participant=participants.query.all()
    usr_list = []

    for u in teams:
        usr = {
                    'id': u.id,
                    'team_name': u.team_name,
                    'team_members': u.team_members,
                    'team_type': u.team_type,
                    'problem_statement': u.problem_statement,
                    }
        i=1
        for v in participant:
            if u.id==v.team_id:
                usr['participant_name'+str(i)]=v.name
                usr['participant_email'+str(i)]=v.email
                usr['participant_phone'+str(i)]=v.phone
                usr['participant_organization'+str(i)]=v.organization
                usr['participant_is_leader'+str(i)]=v.is_leader
            i=i+1
        print(usr)
        usr_list.append(usr)
    return render_template("attendees.html",users=usr_list)

if __name__ == '__main__':
    app.run(debug=True)