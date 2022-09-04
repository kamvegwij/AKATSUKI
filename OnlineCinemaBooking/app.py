import re
<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Customer import Customer


app = Flask(__name__)
app.config['SECRET_KEY'] = '81V7SG471G6S7D'

# database creation and connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# the customer login table class
class CustomerLogin(db.Model):
    # the columns in the table
    email = db.Column(db.String(100), nullable = False, primary_key=True, unique=True)
    password = db.Column(db.String(50), nullable = False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f'{self.email} {self.password}'
    


# the customer booking table class
class CustomerBooking(db.Model):
    # the columns in the table
    ticket_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(50), nullable = False)
    customer_surname = db.Column(db.String(50), nullable = False)
    movie_selected = db.Column(db.String(50), nullable = False)
    date_of_purchase = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, ticket_id, customer_name, customer_surname, movie_selected, date_of_purchase):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.movie_selected = movie_selected
        self.date_of_purchase = date_of_purchase

    def __repr__(self):
        return f'{self.ticket_id} {self.customer_name} {self.customer_surname} {self.movie_selected} {self.date_of_purchase}'

=======
from flask import Flask, render_template, url_for, request, redirect
from Customer import Customer

app = Flask(__name__)
testing = {"username": "123"} #test user database

def setAuthority():
    pass
>>>>>>> ae4973355a23343ed640720903d70c550a913d65

@app.route('/', methods = ['GET', 'POST'])
def login():
    # login
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
<<<<<<< HEAD

        # look up of the details in the database 
        # and format them to a list [username, password]
        # !!! lookup exceptions??
        try:
            user_row = CustomerLogin.query.filter_by(email=username).all()

            user_row = str(user_row[0]).split()

            # password match??
            if password == user_row[1]:
            
                return render_template('customer.html')
            else:
                flash('Wrong password, Please try again!')
                return render_template('login.html');

        except:
            flash("You username doesn't exist, Please signup!")
            return render_template('login.html')

    
    return render_template('login.html');
        

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # new user signing up
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        password_conf = request.form['password_conf']

        # add to the db when there's input in the fields and the passwords match 
        # when conditions are not met, stay on the signin page
        if (password == password_conf) and (username != '') and (password != ''):
            customer_login = CustomerLogin(username, password)

            try:
                db.session.add(customer_login)
                db.session.commit()

                # redirect to the login page after signing up
                flash("Successfully signed up, Now login!")
                return redirect('/')
            except:
                flash("Username already exist!")
                render_template('signup.html')
        else:
            flash("Passwords are not matching, Try again!")
            render_template('signup.html')
    
    return render_template('signup.html')

    


@app.route('/home', methods=['GET', 'POST'])
def home():
=======
        if request.form.get("admin_btn"): #if the admin button is clicked:
            if username == "myadmin":
                print("Username correct")
                if password == "abc123":
                    print('Password correct')
                    return admin()
                else: return render_template('login.html')
            else:
                return render_template('login.html')

        elif request.form.get("cust_btn"):
            #customer button pressed. login
            if username in testing:
                if password == testing[username]:
                    return customer() #if details correct
                else: 
                    return render_template("login.html")
            else: return render_template('login.html')

        elif request.form.get("create_btn"):
            if username in testing:
                return render_template('login.html')#if username already exists then reload
            else: return render_template('customer.html')#change this to the create account page .html
            
    else:
        return render_template('login.html')
        

@app.route('/customer', methods=['GET', 'POST'])
def customer():
>>>>>>> ae4973355a23343ed640720903d70c550a913d65
    return render_template('customer.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)
