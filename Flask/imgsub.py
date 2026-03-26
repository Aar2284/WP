from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.LargeBinary, nullable=True) 

with app.app_context():
    db.create_all()

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == "POST":
        username = request.form.get('username')
        image_file = request.files.get('image')

        image_data = image_file.read() if image_file else None

        new_user = User(
            username=username, 
            image=image_data
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("database"))
    return render_template("imgsub.html")

@app.route("/database")

def database():

    users = User.query.all()

    for user in users:  
        if user.image:
            user.image = base64.b64encode(user.image).decode('utf-8')
        
        else:
            user.image = None

    return render_template("database.html", user=users)

if __name__ == "__main__":
    app.run(debug=True)