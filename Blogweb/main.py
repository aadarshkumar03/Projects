from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
with open('config.json') as rp:
    params = json.load(rp)['params']

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
db = SQLAlchemy(app)


class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=20), nullable=False)
    author = db.Column(db.String(length=25), nullable=False)
    posts = db.Column(db.Text, nullable=False)
    dt = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Blog Post-{id}"


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', params=params)


@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        posts = request.form.get('posts')
        data = Blogs(title=title, author=author, posts=posts, dt=datetime.now())
        db.session.add(data)
        db.session.commit()
        return redirect('/posts')
    return render_template('new_post.html', params=params)


@app.route('/posts')
def posts():
    data = Blogs.query.order_by(Blogs.dt).all()
    return render_template('posts.html', data=data, params=params)


@app.route('/posts/delete/<int:no>')
def delete(no):
    data = Blogs.query.get_or_404(no)
    db.session.delete(data)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts/edit/<int:no>', methods=["GET", "POST"])
def edit(no):
    data = Blogs.query.get_or_404(no)
    if request.method == "POST":
        data.title = request.form.get('title')
        data.author = request.form.get('author')
        data.posts = request.form.get('posts')
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', data=data, params=params)


if __name__ == "__main__":
    app.run(debug=True)
