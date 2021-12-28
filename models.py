from app import db
 

class team(db.Model):
    __tablename__="team"
    id=db.Column(db.Integer,primary_key=True)
    team_name=db.Column(db.String,null=False)
    team_members=db.Column(db.Integer,null=False)
    team_type=db.Column(db.String,null=False)
    problem_statement=db.Column(db.String,null=False)
    
    def __init__(self,team_name,team_members,team_type,problem_statement):
        self.team_name=team_name
        self.team_members=team_members
        self.team_type=team_type
        self.problem_statement=problem_statement

class participants(db.Model):
    __tablename__="participants"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, null=False)
    email=db.Column(db.String, null=False)
    phone=db.Column(db.String, null=False)
    organization=db.Column(db.String, null=False)
    state=db.Column(db.String, null=False)
    is_leader=Column(db.Boolean, null=False)
    team_id=db.Column(db.Integer, db.ForeignKey('team.id'))
    

    def __init__(self, name, email, phone, age, education, state, avatar_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.education = education
        self.state = state
        self.avatar_id = avatar_id
