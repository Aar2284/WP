from flask import Flask, redirect, request, url_for, session, Response

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['POST','GET'])

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '12345678':
            session['user'] = username
            return redirect(url_for('WELCOME!!'))
        else:
            return Response('Invalid credentials. Please try again.', status=401)
        
    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''