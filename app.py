import sqlite3
import os
from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask import g

DATABASE = 'ideathon.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    
app = Flask(__name__)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
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