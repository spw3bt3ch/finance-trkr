from flask import Flask, render_template

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

@app.route("/register")
def register():
  return render_template(
    'register.html', 
    titlename = 'Register'
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

@app.route("/contact")
def contact():
  return render_template(
    'contact.html',
    titlename = 'Contact Us'
    )

@app.route("/about")
def about():
  return render_template(
    'about.html',
    titlename = 'About Us'
  )



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5500, debug=True)