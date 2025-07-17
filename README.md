
<body>

  <h1>🔐 Flask Login & Registration System</h1>

  <p>This project is a simple <strong>user login and registration system</strong> built with <strong>Flask</strong> and <strong>MySQL</strong>. It allows users to register, log in, and access a protected home page after authentication.</p>

  <div class="section">
    <h2>🚀 Features</h2>
    <ul>
      <li>User registration</li>
      <li>User login with session</li>
      <li>Protected home page</li>
      <li>Logout functionality</li>
      <li>Uses MySQL for storing user credentials</li>
    </ul>
  </div>

  <div class="section">
    <h2>🛠️ Requirements</h2>
    <ul>
      <li>Python 3.x</li>
      <li>Flask</li>
      <li>MySQL Server</li>
      <li><code>mysql-connector-python</code> module</li>
    </ul>
    <pre><code>pip install flask mysql-connector-python</code></pre>
  </div>

  <div class="section">
    <h2>🧱 Database Setup</h2>
    <pre><code>CREATE DATABASE mydb;

USE mydb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);</code></pre>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre><code>project/
├── app.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── home.html
└── README.md</code></pre>
  </div>

  <div class="section">
    <h2>🧾 Usage</h2>
    <p><strong>1. Start the Flask app:</strong></p>
    <pre><code>python app.py</code></pre>
    <p><strong>2. Open in your browser:</strong></p>
    <pre><code>http://127.0.0.1:5000/</code></pre>
    <p><strong>3. Available Routes:</strong></p>
    <ul>
      <li><code>/</code> → Login page</li>
      <li><code>/register</code> → Registration page</li>
      <li><code>/home</code> → Home (protected route)</li>
      <li><code>/login_validation</code> → Validates login credentials</li>
      <li><code>/add_user</code> → Adds a new user</li>
      <li><code>/logout</code> → Logs the user out</li>
    </ul>
  </div>

  <div class="section">
    <h2>🔐 Session Handling</h2>
    <ul>
      <li>A secret key is generated using <code>os.urandom(24)</code></li>
      <li><code>session['user_id']</code> is used to track logged-in users</li>
    </ul>
  </div>

  <div class="section">
    <h2>📦 Note</h2>
    <ul>
      <li>This is a basic authentication system</li>
      <li>⚠️ Passwords are stored in plain text for demonstration purposes</li>
      <li><strong>Use password hashing (e.g., bcrypt) for production</strong></li>
    </ul>
  </div>

  <div class="section">
    <h2>👨‍💻 Author</h2>
    <p>Developed with ❤️ using Flask & MySQL.</p>
  </div>

</body>
</html>
