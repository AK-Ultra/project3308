 # Command to Run: FLASK_APP=app.py flask run
from flask import Flask, render_template, flash, request, url_for , redirect, session
import pymysql.cursors
app = Flask(__name__)

 # allows the hardcoded login logic to work before sql
app.secret_key = 'password'

## Database Connection
conn = pymysql.connect(host='localhost',user='root',passwd='123',db='websiteDB')

## Query tables
with conn.cursor() as cursor:

  # Query orders
  cursor.execute('SELECT * FROM orders;')
  projectData = cursor.fetchall()

with conn.cursor() as cursor:
  
  #Query Customers Info
cursor = db.cursor()
cursor.execute('SELECT * FROM customers;')
customerData = cursor.fetchall()
cursor.close()
 
  # Query reviews
  cursor.execute('SELECT t1.description, t3.firstName, LEFT(t3.lastName,1), t1.starCount FROM reviews t1 INNER JOIN orders t2 ON t1.orderID = t2.orderID INNER JOIN customers t3 ON t2.customerID = t3.customerID ORDER BY t1.starCount DESC LIMIT 4;')
  reviewData = cursor.fetchall()



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
@app.route("/customers")
def customers():
    return render_template('customers.html',data=customerData)
 
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
  error = ''
  try:
    #They have submitted a login
    if request.method == "POST":
      attempted_username = request.form['username']
      attempted_password = request.form['password']

      ## Query users
      with conn.cursor() as cursor:
        cursor.execute("SELECT count(*) from users WHERE BINARY username = '{}' and password = '{}';".format(attempted_username,attempted_password))
        auth = cursor.fetchone()[0]

      flash(auth)
      flash(attempted_username)
      flash(attempted_password)
      #Basic for debugging  Sql imp here.
      if auth > 0:
         #Then we redirect to projects which will be admin only
          return redirect(url_for('projects'))
      else:
          error = 'Invalid Credentials'
    return render_template('login.html',error = error)

  except Exception as e:
    flash(e)
    return render_template('login.html',error = error)
