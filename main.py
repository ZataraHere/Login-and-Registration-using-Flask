from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)
cursor = conn.cursor()

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
         return render_template('home.html')
    else:
        return redirect('/')

@app.route('/login_validation', methods = ['POST'])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    query  = "SELECT * FROM users WHERE email LIKE %s AND password LIKE %s"
    values = (f"%{email}%", f"%{password}%")
    cursor.execute(query, values)
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/add_user', methods = ['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('password')

    query = "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)"
    values = (name, email, password)

    cursor.execute(query, values)
    conn.commit()

    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)