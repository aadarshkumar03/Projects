from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
with open("config.json") as rp:
    params = json.load(rp)["params"]

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    mobile = db.Column(db.String(length=12), nullable=False, unique=True)
    msg = db.Column(db.String(length=256), nullable=False)
    dt = db.Column(db.String(length=100))


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', params=params)


@app.route('/#contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        msg = request.form.get('msg')
        data = Contact(name=name, email=email, mobile=mobile, msg=msg, dt=datetime.now())
        db.session.add(data)
        db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
