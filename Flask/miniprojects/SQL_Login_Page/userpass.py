from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('index.html', users=users)

    hashed_password = bcrypt.generator_password_hash(password).decade('utf-8')
    


@app.route('/update_password', methods=['POST'])
def update_password():
    username = request.form['username']
    new_password = request.form['new_password']

    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found"
    user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']

    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found"

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

    """
    @app.route('/update', methods = ["GET", "POST"])
    def update():
        if request.method == 'POST':
            sno = request.form['sno']
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(sn0 = sno).first()
            if user:
                user.username = username
                user.password = password
                db.session.add(user)
                db.session.commit()
        return render_template("Update.html")
        
    """

if __name__ == '__main__':
    app.run(debug=True)