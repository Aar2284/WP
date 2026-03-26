from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    user ={
        "name": 'Aaryan Kalia',
        "logged_in": True,
        "emotions": ["Happy", "Sad", "Exited", "Angry", "Anxious", 
                     "Relaxed", "Bored", "Confused", "Grateful", "Frustrated"],
    }

    return render_template('emotion.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)