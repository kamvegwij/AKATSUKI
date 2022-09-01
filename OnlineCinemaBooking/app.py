import re
from flask import Flask, render_template, url_for, request, redirect
from Customer import Customer

app = Flask(__name__)
testing = {"username": "123"} #test user database

def setAuthority():
    pass

@app.route('/', methods = ['GET', 'POST'])
def login():
    #login for admin
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
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
    return render_template('customer.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)