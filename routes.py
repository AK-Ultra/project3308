from flask import Flask, render_template, flash , request, url_for

app = Flask(__name__)

#Links to the home page#
@app.route('/')
def home():
    return render_template('index.html')

#Links to the about page#
@app.route('/about/')
def about():
    return render_template('about.html')


# Handles the login requests if valid then redirects to the Admin dashboard #
@app.route('/login/', methods=["GET","POST"])
def login_page():
#    error = None
#    try:
#       if request.method == "POST":
#            attempted_username = request.form['username']
#            attempted_password = request.form['password']
#
#            flash(attempted_username)
#            flash(attempted_password)
#            
#            if attempted_username == "admin" and attempted_password == "password":
#                return redirect(url_for('dashboard'))
#            else:
#                error = "Invalid Try Again" 
#            
#    except Exception as e:
#        flash(e)
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)
