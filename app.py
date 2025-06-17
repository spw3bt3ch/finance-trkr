from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  return render_template(
    'home.html', 
    titlename = 'Homepage'
    )

@app.route("/login")
def login():
  return render_template(
    'login.html', 
    titlename = 'Login'
    )

# def init_db():
#   conn = sqlite3.connect('users.db')
#   cur = conn.cursor()
#   cur.execute()


@app.route("/register", methods=['POST', 'GET'])
def register():
  if request.method == 'POST':
    fullname = request.form['fullname']
    email = request.form['email']
    mobile = request.form['mobile']
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO registration (fullname, email_address, mobile_number, username, password) 
                VALUES ('{fullname}', '{email}', {mobile}, '{username}', '{password}')
""")

    conn.commit()

    return render_template('success.html')

  return render_template(
    'register.html', 
    titlename = 'Register',
    message = 'Check your email address provided to confirm your registration.',
    # redirect_url = '/login'
    )

@app.route("/forgot-password")
def forgot_password():
  return render_template(
    'forgot-password.html', 
    titlename = 'Reset Password'
    )

@app.route("/dashboard")
def dashboard():
  return render_template(
    'dashboard.html', 
    titlename = 'User Dashboard'
    )

@app.route("/contact", methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO contact(fullname, email, phone, message)
                  VALUES ('{fullname}', '{email}', {phone}, '{message}')
""")
    conn.commit()
    return "Form successfully submitted! <a href='/contact'>Go back to Contact form</a>"
  return render_template('contact.html', titlename = 'Contact Us')

# def contact():
#   return render_template(
#     'contact.html',
#     titlename = 'Contact Us'
#     )

@app.route("/about")
def about():
  return render_template(
    'about.html',
    titlename = 'About Us'
  )


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5500, debug=True)