from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)

db = MySQLdb.connect(host='localhost',user='root',passwd='539',db='websiteDB')
cursor = db.cursor()
cursor.execute('SELECT * FROM orders;')
orders = cursor.fetchall()

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
    return render_template('project.html',data=orders)

@app.route("/info")
def info():
    return render_template('aboutUs.html')

@app.route('/contact',methods=['POST'])
def submitContact():
    _firstname = request.form['firstname']
    _lastname = request.form['lastname']
    _message = request.form['Message']
