from flask import Flask, render_template
app = Flask(__name__)

# mysql = MySQL()
# # MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'user'
# app.config['MYSQL_DATABASE_DB'] = 'websiteDB'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

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
    return render_template('project.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route('/contact',methods=['POST'])
def submitContact():
    _firstname = request.form['firstname']
    _lastname = request.form['lastname']
    _message = request.form['Message']
