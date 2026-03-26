from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])

def result():

    name = request.form.get('student_name')
    score = int(request.form.get('score'))

    if score >= 50:
        status = "PASSED"
        next_steps = ["Download Certificate", "Enroll in Advanced Course", "Update Resume"]

    else:
        status = "FAILED"
        next_steps = ["Review Chapters 1-4", "Watch Tutorial Videos", "Retake Exam in 7 days"]

    return render_template('result.html', name=name, score=score, status=status, steps=next_steps)

if __name__ == '__main__':
    app.run(debug=True)