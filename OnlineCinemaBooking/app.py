import re
from flask import Flask, render_template, url_for, request
from Customer import Customer
app = Flask(__name__)
testing = {"myadmin": "abc123"}

@app.route('/', methods = ['GET', 'POST'])
def login():
    #login for admin
    if request.method == "POST":
        username = request.form['username']
        if username in testing:
            print("Username correct")
            password = request.form['password']
        
            if password == testing[username]:
                print('Password correct')
                return render_template('customer.html')

            else: return render_template('login.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
        

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('customer.html')

if __name__ == "__main__":
    app.run(debug=True)