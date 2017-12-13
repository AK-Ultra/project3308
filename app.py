 # Command to Run: FLASK_APP=app.py flask run
from flask import Flask, render_template, flash, request, url_for , redirect, session
#Used for python connector
import pymysql.cursors
#For creating python decorators
from functools import wraps

#from flask_mail import Mail

app = Flask(__name__)

# allows the hardcoded login logic to work before sql
app.secret_key = 'password'

## Database Connection
conn = pymysql.connect(host='localhost',user='root',passwd='123',db='websiteDB')

app.static_folder = 'static'

# home
@app.route("/")
def main():
	# Query reviews
	with conn.cursor() as cursor:
		cursor.execute('SELECT t1.description, t3.firstName, LEFT(t3.lastName,1), t1.starCount FROM reviews t1 INNER JOIN orders t2 ON t1.orderID = t2.orderID INNER JOIN customers t3 ON t2.customerID = t3.customerID ORDER BY t1.starCount DESC LIMIT 4;')
		reviewData = cursor.fetchall()

	return render_template('index.html',data=reviewData)

# services
@app.route("/services/")
def services():
    return render_template('services.html')

#Login required decoratior. Verifys user has logged in as admin. Restricts pages.
def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
             if 'logged_in' in session :
                 return f(*args,**kwargs)
             else:
                 flash("Log in First")
                 return redirect(url_for('login'))
        return wrap


#---------Password Protected pages------------
#To password protect add the @login_required decorator under the @app.route()


# Projects
@app.route("/projects/", methods=["GET","POST"])
@login_required
def projects():
	try:
		with conn.cursor() as cursor:
			# Query orders
			cursor.execute('SELECT * FROM orders;')
			projectData = cursor.fetchall()

		# POST Function
		if request.method == "POST":
			
			# generate old status list
			oldStatus = []
			for row in projectData:
				oldStatus.append((row[3],row[0]))

			# generate updated status list
			updatedTable = request.form.getlist('status')
			newStatus = []
			for string in updatedTable:
				newStatus.append(str(string))

			# update DB
			order = 0
			status = ''
			for i in range(0,len(oldStatus)):
				if (oldStatus[i][0] != newStatus[i]):
					status = newStatus[i]
					order = oldStatus[i][1]
					print 'Updating:',order,'to status:',status

					# update status via query 
					try:
						with conn.cursor() as cursor:
							cursor.execute("UPDATE orders SET status = '{}' WHERE orderID = {};".format(status,order))
							conn.commit()
						print 'Commited'
					except Exception as e:
						print 'An error occured during UPDATE',e

			return redirect(url_for('projects'))

		# GET Function
		else:
			return render_template('admin/project.html',data=projectData)

	except Exception as e:
		return render_template('admin/project.html',data=projectData)

# customers
@app.route("/customers/", methods=['POST','GET'])
@login_required
def customers():
	# Query customers
	with conn.cursor() as cursor:
		cursor.execute('SELECT * FROM customers;')
		customerData = cursor.fetchall()
	return render_template('admin/customers.html',data=customerData)

# add customer
@app.route("/AddCustomerrequest/", methods=['POST','GET'])
@login_required
def AddCustomerrequest():
			FirstName=request.form['FirstName']
			LastName=request.form['LastName']
			Email=request.form['Email']
			Phone=request.form['Phone']
			Home=request.form['Address']
			City=request.form['City']
			Description=request.form['Description']
			cur = conn.cursor()
			#customerID auto_increments
			query="INSERT INTO customers (firstname,lastname,emailAddress,phoneNumber,address,city) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (FirstName,LastName,Email,Phone,Home,City)
			cur.execute(query)
			conn.commit()
			cur.execute('SELECT MAX(customerId) FROM customers;')
			ID = cur.fetchone()
			ID=ID[0]
			query="INSERT INTO orders (orderDate,description,status,customerId) VALUES (CURDATE(),'%s','Initial',%d);" % (Description,ID)
			cur.execute(query)
			conn.commit()
			flash("Customer Added.")
			return redirect(url_for('customers'))

@app.route("/AddCustomer/", methods=['POST','GET'])
@login_required
def AddCustomer():
    	return render_template('admin/AddCustomer.html')

#----------------------------------------------

@app.route("/about/")
def info():
    return render_template('aboutUs.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/review/", methods=["GET","POST"])
def reviews():
	try:
		# POST Function
		if request.method == "POST":

			try:
				formRating = request.form['rating']
			except:
				formRating = 5

			formOrder = request.form['orderID']
			formMessage = request.form['Message']

			print (formRating)

			# orderID check
			with conn.cursor() as cursor:
				cursor.execute("SELECT count(*) FROM orders WHERE orderID = '{}' AND orderID NOT IN (SELECT orderID FROM reviews);".format(formOrder))
				orderCheck = cursor.fetchone()[0]

			# Check passes
			if (orderCheck == 1):

				# Insert review
				with conn.cursor() as cursor:
					cursor.execute("INSERT INTO reviews VALUES (0,'{}','{}',{});".format(formOrder,formMessage,formRating))
					conn.commit()

				flash('Thank you! Your review has been posted!')

			# Check fails
			else:
				flash('Unable to post review: Invalid Order ID or review already exists.')

			redirect(url_for('review'))

		else:
			return render_template('reviews.html')

	except Exception as e:
		return render_template('reviews.html')

#close the logged_in session
@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect(url_for('main'))

@app.route("/login/", methods=["GET","POST"])
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

      if auth > 0:
          session['logged_in'] = True
          session['username'] = request.form['username']

          # admin redirect
          return redirect(url_for('projects'))

      #Not valid credentials
      else:
          flash("Invalid Credentials")
         # error = 'Invalid Credentials'
    return render_template('login.html',error = error)

  except Exception as e:
    #flash(e)
    return render_template('login.html',error = error)
