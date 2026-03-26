from flask import Flask, render_template, redirect, session, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Blog', backref='author', lazy=True)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    posts = Blog.query.all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = user.username
            session['user_id'] = user.id  # Store ID to link blogs later
            flash("Login Successful ! Welcome.", "success")
            return redirect('/')
        
        flash("Wrong Credentials. Try Again !!", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(username=email).first():
            flash("User already exists", "danger")
            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registration Successful! Please Login.", "success")
        return redirect('/login')
    return render_template('register.html')

@app.route('/create', methods=['GET', 'POST'])
def create_blog():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        post = Blog(title=title, content=content, user_id=session['user_id'])
        db.session.add(post)
        db.session.commit()
        flash('Blog Created Successfully!', 'success')
        return redirect('/')

    return render_template('create_blog.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    if 'user' not in session:
        return redirect('/login')
        
    post = Blog.query.get_or_404(post_id)

    if post.author.id != session.get('user_id'):
        flash("You cannot edit this post!", "danger")
        return redirect(url_for('post', post_id=post.id))

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Post Updated!', 'success')
        return redirect(url_for('post', post_id=post.id))

    return render_template('edit_blog.html', post=post)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    flash("You have been logged out.", "success")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)