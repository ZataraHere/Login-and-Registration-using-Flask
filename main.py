from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

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
    return render_template('home.html')

@app.route('/login_validation', methods = ['POST'])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    query  = "SELECT * FROM users WHERE email LIKE %s AND password LIKE %s"
    values = (f"%{email}%", f"%{password}%")
    cursor.execute(query, values)
    users = cursor.fetchall()

    return users

if __name__ == "__main__":
    app.run(debug=True)