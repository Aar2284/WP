from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- GLOBAL STORAGE  ---
todos = []

@app.route('/')

def index():
    return render_template('tasks.html', todos=todos)

@app.route('/add', methods=['POST'])

def add_task():

    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')

def delete_task(index):

    if 0 <= index < len(todos):
        todos.pop(index) 
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)