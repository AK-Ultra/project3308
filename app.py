from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)

# Command to Run: FLASK_APP=app.py flask run

# Database Connection
db = MySQLdb.connect(host='localhost',user='root',passwd='539',db='websiteDB')

# Query orders
cursor = db.cursor()
cursor.execute('SELECT * FROM orders;')
projectData = cursor.fetchall()
cursor.close()

# Query reviews
cursor = db.cursor()
cursor.execute('SELECT t1.description, t3.firstName, LEFT(t3.lastName,1), t1.starCount FROM reviews t1 INNER JOIN orders t2 ON t1.orderID = t2.orderID INNER JOIN customers t3 ON t2.customerID = t3.customerID;')
reviewData = cursor.fetchall()
cursor.close()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

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
