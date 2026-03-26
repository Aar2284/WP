from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def start():

    res_code = 0
    return render_template('jinja3.html', res_code=res_code)

@app.route('/loop')
def loop():

    l1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    return render_template('loop.html', l1=l1)

app.run(debug=True)