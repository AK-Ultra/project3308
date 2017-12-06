from flask import Flask, render_template, flash, request, url_for , redirect, session
# import MySQLdb
app = Flask(__name__)
# #allows the hardcoded login logic to work before sql
# app.secret_key = 'password'
# # Command to Run: FLASK_APP=app.py flask run
#
# # Database Connection
# db = MySQLdb.connect(host='localhost',user='root',passwd='539',db='websiteDB')
#
# # Query orders
# cursor = db.cursor()
# cursor.execute('SELECT * FROM orders;')
# projectData = cursor.fetchall()
# cursor.close()
#
# # Query reviews
# cursor = db.cursor()
# cursor.execute('SELECT t1.description, t3.firstName, LEFT(t3.lastName,1), t1.starCount FROM reviews t1 INNER JOIN orders t2 ON t1.orderID = t2.orderID INNER JOIN customers t3 ON t2.customerID = t3.customerID;')
# reviewData = cursor.fetchall()
# cursor.close()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
#Remove to be password protected. 
@app.route("/projects")
def projects():
    return render_template('project.html',data=projectData)

@app.route("/info")
def info():
    return render_template('aboutUs.html')

@app.route('/contact',methods=['POST'])
def submitContact():
    _firstname = request.form['firstname']
    _lastname = request.form['lastname']
    _message = request.form['Message']

@app.route("/reviews")
def reviews():
    return render_template('reviews.html',data=reviewData)
#Under-Construction Login logic
@app.route('/login/', methods=["GET","POST"])
def login():
     error = None
     try:
            #They have submitted a login
         if request.method == "POST":
              attempted_username = request.form['username']
              attempted_password = request.form['password']
              cursor = db.cursor()
              cursor.execute('SELECT * FROM orders;')
              projectData = cursor.fetchall()
              cursor.close()

              flash(attempted_username)
              flash(attempted_password)
              #Basic for debugging  Sql imp here.
              if attempted_username == "admin" and attempted_password == "password":
                 #Then we redirect to projects which will be admin only
                  return redirect(url_for('projects'))
              else:
                  error = "Invalid Try Again"
         return render_template('login.html',error = error)
     except Exception as e:
         flash(e)
         return render_template('login.html',error = error)
