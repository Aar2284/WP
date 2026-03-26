from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_NAME = "college.db"

courses_list = [
    "Computer Science",
    "Information Technology",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Business Administration",
    "Graphic Design"
]

def init_db():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')

        if not name or not email or not course:
            error = "Error: All fields are required!"

        elif '@gmail.com' not in email:
            error = "Error: Only @gmail.com addresses are accepted!"

        else:
            try:
                # 1. Connect to DB
                conn = sqlite3.connect(DB_NAME)
                c = conn.cursor()
                
                # 2. Insert Data (Use ? placeholders for security)
                c.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)", 
                          (name, email, course))
                
                # 3. Save (Commit) and Close
                conn.commit()
                conn.close()
                
                return redirect('/students')
            except Exception as e:
                error = f"Database Error: {e}"

    return render_template('register.html', error=error, courses=courses_list)

@app.route('/students')
def show_students():
    
    conn = sqlite3.connect(DB_NAME)
    
    conn.row_factory = sqlite3.Row 
    
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    
    students_data = c.fetchall()
    
    conn.close()
    
    return render_template('students.html', students=students_data)

@app.route('/delete/<int:id>')

def delete_student(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute("DELETE FROM students WHERE id = ?", (id,))
    
    conn.commit()
    conn.close()
    
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)