from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registration')
def register():
    return render_template("registrations.html")

if __name__ == '__main__':
    app.run(debug=True)