import random
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from Customer import Customer
from flask_session import Session


app = Flask(__name__)
app.config['SECRET_KEY'] = '81V7SG471G6S7D'

# sessions for moving variables between pages
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# database creation and connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# the customer login table class
class CustomerLogin(db.Model):
    # the columns in the table
    email = db.Column(db.String(100), nullable = False, primary_key=True, unique=True) #username
    password = db.Column(db.String(50), nullable = False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f'{self.email}~{self.password}'


# movies table
class Movies(db.Model):
    name = db.Column(db.String(100), nullable=False, primary_key=True, unique=True)
    seats_available = db.Column(db.Integer, nullable=False)
    seats_sold = db.Column(db.Integer, nullable=False)
    total_seats = db.Column(db.Integer, nullable=False, default=32)

    def __init__(self, name, seats_available, seats_sold, total_seats):
        self.name = name
        self.seats_available = seats_available
        self.seats_sold = seats_sold
        self.total_seats = total_seats

    def __repr__(self):
        return f'{self.name}~{self.seats_available}~{self.seats_sold}~{self.total_seats}'
    
# seats for movie 1
class SeatsM1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c1 = db.Column(db.Integer, nullable=False)
    c2 = db.Column(db.Integer, nullable=False)
    c3 = db.Column(db.Integer, nullable=False)
    c4 = db.Column(db.Integer, nullable=False)
    c5 = db.Column(db.Integer, nullable=False)
    c6 = db.Column(db.Integer, nullable=False)
    c7 = db.Column(db.Integer, nullable=False)
    c8 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}~{self.c1}~{self.c2}~{self.c3}~{self.c4}~{self.c5}~{self.c6}~{self.c7}~{self.c8}'



# seats for movie 2
class SeatsM2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c1 = db.Column(db.Integer, nullable=False)
    c2 = db.Column(db.Integer, nullable=False)
    c3 = db.Column(db.Integer, nullable=False)
    c4 = db.Column(db.Integer, nullable=False)
    c5 = db.Column(db.Integer, nullable=False)
    c6 = db.Column(db.Integer, nullable=False)
    c7 = db.Column(db.Integer, nullable=False)
    c8 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}~{self.c1}~{self.c2}~{self.c3}~{self.c4}~{self.c5}~{self.c6}~{self.c7}~{self.c8}'



# seats for movie 3
class SeatsM3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c1 = db.Column(db.Integer, nullable=False)
    c2 = db.Column(db.Integer, nullable=False)
    c3 = db.Column(db.Integer, nullable=False)
    c4 = db.Column(db.Integer, nullable=False)
    c5 = db.Column(db.Integer, nullable=False)
    c6 = db.Column(db.Integer, nullable=False)
    c7 = db.Column(db.Integer, nullable=False)
    c8 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}~{self.c1}~{self.c2}~{self.c3}~{self.c4}~{self.c5}~{self.c6}~{self.c7}~{self.c8}'


# the customer booking table class
class CustomerBooking(db.Model):
    # the columns in the table
    ticket_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(50), nullable = False)
    customer_surname = db.Column(db.String(50), nullable = False)
    movie_selected = db.Column(db.String(50), nullable = False)
    seat_selected = db.Column(db.String(10), nullable = False)

    def __init__(self, ticket_id, customer_name, customer_surname, movie_selected, seat_selected):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.movie_selected = movie_selected
        self.seat_selected = seat_selected

    def __repr__(self):
        return f'{self.ticket_id}~{self.customer_name}~{self.customer_surname}~{self.movie_selected}~{self.seat_selected}'


# login page
@app.route('/', methods = ['GET', 'POST'])
def login():
    # login
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # look up of the details in the database 
        # and format them to a list [username, password]
        try:
            user_row = CustomerLogin.query.filter_by(email=username).all()

            user_row = str(user_row[0]).split('~')

            # check if password match?? before redirecting to home page
            if password == user_row[1]:
            
                return redirect('/home')
                
            else:
                flash('Wrong password, Please try again!')
                return render_template('login.html');

        except:
            flash("You username doesn't exist, Please signup!")
            return render_template('login.html')

    
    return render_template('login.html');
        

# signup page
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


# home page 
@app.route('/home', methods=['GET', 'POST'])
def index():

    # query the movies database to render the no. of seat booked/available 
    try:
        movies = Movies.query.all()
    except:
        return "There was an error with reading the database"


    # render template with the variables for no. of seats booked/available
    return render_template('index.html',  movie1 = str(movies[0]).split('~'), movie2 = str(movies[1]).split('~'), movie3 = str(movies[2]).split('~'))


# after selecting movie 1
@app.route('/home/seatselection/jkz', methods=['GET', 'POST'])
def select():

    # formating seat number for easier usability e.g C5 --> [2, 5] meaning row_3 col_5
    if request.method == 'POST':
        selected_seat = str(request.form['seat'])

        if selected_seat[0] == 'A':
            selected_seat = [0, int(selected_seat[1])]
        elif selected_seat[0] == 'B':
            selected_seat = [1, int(selected_seat[1])]
        elif selected_seat[0] == 'C':
            selected_seat = [2, int(selected_seat[1])]
        elif selected_seat[0] == 'D':
            selected_seat = [3, int(selected_seat[1])]

        # session for moving between pages with the seat variable/list
        session['seat'] = selected_seat

        # seat selection (user cannot select a seat that is already selected)
        try:
            movie_seats = SeatsM1.query.all()
            movie_seats = [str(movie_seats[0]).split('~'), str(movie_seats[1]).split('~'), str(movie_seats[2]).split('~'), str(movie_seats[3]).split('~')]

            if movie_seats[selected_seat[0]][selected_seat[1]] == '1':
                flash("The seat is already taken.")
                flash("Please choose another one!")
                return render_template('seatselection.html')
            else:
                return redirect('/home/seatselection/jkz/checkout')
        except:
            return 'There was an error with reading the database'

    return render_template('seatselection.html')


# for movie 2
@app.route('/home/seatselection/bnh', methods=['GET', 'POST'])
def select2():

    # formating seat number for easier usability e.g C5 --> [2, 5] meaning row_3 col_5
    if request.method == 'POST':
        selected_seat = str(request.form['seat'])

        if selected_seat[0] == 'A':
            selected_seat = [0, int(selected_seat[1])]
        elif selected_seat[0] == 'B':
            selected_seat = [1, int(selected_seat[1])]
        elif selected_seat[0] == 'C':
            selected_seat = [2, int(selected_seat[1])]
        elif selected_seat[0] == 'D':
            selected_seat = [3, int(selected_seat[1])]

        # session for moving between pages with the seat variable/list
        session['seat'] = selected_seat
        

        # seat selection (user cannot select a seat that is already selected)
        try:
            movie_seats = SeatsM2.query.all()
            movie_seats = [str(movie_seats[0]).split('~'), str(movie_seats[1]).split('~'), str(movie_seats[2]).split('~'), str(movie_seats[3]).split('~')]

            if movie_seats[selected_seat[0]][selected_seat[1]] == '1':
                flash("The seat is already taken.")
                flash("Please choose another one!")
                return render_template('seatselection.html')
            else:
                return redirect('/home/seatselection/bnh/checkout')
        except:
            return 'There was an error with reading the database'

    return render_template('seatselection.html')



# for movie 3
@app.route('/home/seatselection/dbs', methods=['GET', 'POST'])
def select3():

    # formating seat number for easier usability e.g C5 --> [2, 5] meaning row_3 col_5
    if request.method == 'POST':
        selected_seat = str(request.form['seat'])

        if selected_seat[0] == 'A':
            selected_seat = [0, int(selected_seat[1])]
        elif selected_seat[0] == 'B':
            selected_seat = [1, int(selected_seat[1])]
        elif selected_seat[0] == 'C':
            selected_seat = [2, int(selected_seat[1])]
        elif selected_seat[0] == 'D':
            selected_seat = [3, int(selected_seat[1])]

        # session for moving between pages with the seat variable/list
        session['seat'] = selected_seat

        # seat selection (user cannot select a seat that is already selected)
        try:
            movie_seats = SeatsM3.query.all()
            movie_seats = [str(movie_seats[0]).split('~'), str(movie_seats[1]).split('~'), str(movie_seats[2]).split('~'), str(movie_seats[3]).split('~')]

            if movie_seats[selected_seat[0]][selected_seat[1]] == '1':
                flash("The seat is already taken.")
                flash("Please choose another one!")
                return render_template('seatselection.html')
            else:
                return redirect('/home/seatselection/dbs/checkout')
        except:
            return 'There was an error with reading the database'

    return render_template('seatselection.html')


# first checkout route (movie1)
@app.route('/home/seatselection/jkz/checkout', methods=['GET', 'POST'])
def checkout():
    movie_selected = "Jujutsu Kaisen: Zero"
    seat = session.get('seat')

    # generate a random number for the ticket id
    ticket_id = random.randint(10000,99999)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']

        # Customer instance
        customer = Customer(name, surname, email, movie_selected)

        # CustomerBooking instance to add to the database
        cus_details = CustomerBooking(ticket_id, customer.get_cust_name, customer.get_cust_surname, customer.get_movie_selected, str(seat[0])+str(seat[1]))

        # get the row to mark the seat selected with 1
        seats = SeatsM1.query.get_or_404(seat[0] + 1)
        
        # get the column and mark the selected seat with 1
        if seat[1] == 1:
            seats.c1 = 1
        elif seat[1] == 2:
            seats.c2 = 1
        elif seat[1] == 3:
            seats.c3 = 1
        elif seat[1] == 4:
            seats.c4 = 1
        elif seat[1] == 5:
            seats.c5 = 1
        elif seat[1] == 6:
            seats.c6 = 1
        elif seat[1] == 7:
            seats.c7 = 1
        elif seat[1] == 8:
            seats.c8 = 1

        # query and update the number of seats sold/available for this movie
        seat_numbers = Movies.query.get_or_404(movie_selected)
        arr_seat_numbers = str(seat_numbers).split('~')
        add_s = int(arr_seat_numbers[2]) + 1
        sub_s = int(arr_seat_numbers[1]) - 1

        seat_numbers.seats_available = sub_s
        seat_numbers.seats_sold = add_s

        # add to the database and commit
        try:
            db.session.add(cus_details)

            db.session.commit()

            return render_template('thankyou.html', ticket_id=ticket_id)
        except:
            return "Error adding to the database"
        


    return render_template('checkout.html')



# 2nd checkout route (movie2)
@app.route('/home/seatselection/bnh/checkout', methods=['GET', 'POST'])
def checkout2():
    movie_selected = "Boku no Hero: World Hero's Mission"
    seat = session.get('seat')

    # generate a random number for the ticket id
    ticket_id = random.randint(10000,99999)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']

        # Customer instance
        customer = Customer(name, surname, email, movie_selected)

        # # CustomerBooking instance to add to the database
        cus_details = CustomerBooking(ticket_id, customer.get_cust_name, customer.get_cust_surname, customer.get_movie_selected, str(seat[0])+str(seat[1]))


        # get the row to mark the seat selected with 1
        seats = SeatsM2.query.get_or_404(seat[0] + 1)
        
        # # get the column and mark the selected seat with 1
        if seat[1] == 1:
            seats.c1 = 1
        elif seat[1] == 2:
            seats.c2 = 1
        elif seat[1] == 3:
            seats.c3 = 1
        elif seat[1] == 4:
            seats.c4 = 1
        elif seat[1] == 5:
            seats.c5 = 1
        elif seat[1] == 6:
            seats.c6 = 1
        elif seat[1] == 7:
            seats.c7 = 1
        elif seat[1] == 8:
            seats.c8 = 1

        # query and update the number of seats sold/available for this movie
        seat_numbers = Movies.query.get_or_404(movie_selected)
        arr_seat_numbers = str(seat_numbers).split('~')
        add_s = int(arr_seat_numbers[2]) + 1
        sub_s = int(arr_seat_numbers[1]) - 1

        seat_numbers.seats_available = sub_s
        seat_numbers.seats_sold = add_s


        # add to the database and commit
        try:
            db.session.add(cus_details)

            db.session.commit()

            return render_template('thankyou.html', ticket_id=ticket_id)
        except:
            return "Error adding to the database"

    return render_template('checkout.html')



# 3rd checkout route (movie3)
@app.route('/home/seatselection/dbs/checkout', methods=['GET', 'POST'])
def checkout3():
    movie_selected = "Dragon Ball Super Movie"
    seat = session.get('seat')

    # generate a random number for the ticket id
    ticket_id = random.randint(10000,99999)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']

        # Customer instance
        customer = Customer(name, surname, email, movie_selected)

        # CustomerBooking instance to add to the database
        cus_details = CustomerBooking(ticket_id, customer.get_cust_name, customer.get_cust_surname, customer.get_movie_selected, str(seat[0])+str(seat[1]))

        # get the row to mark the seat selected with 1
        seats = SeatsM3.query.get_or_404(seat[0] + 1)
        
        # get the column and mark the selected seat with 1
        if seat[1] == 1:
            seats.c1 = 1
        elif seat[1] == 2:
            seats.c2 = 1
        elif seat[1] == 3:
            seats.c3 = 1
        elif seat[1] == 4:
            seats.c4 = 1
        elif seat[1] == 5:
            seats.c5 = 1
        elif seat[1] == 6:
            seats.c6 = 1
        elif seat[1] == 7:
            seats.c7 = 1
        elif seat[1] == 8:
            seats.c8 = 1


        # query and update the number of seats sold/available for this movie
        seat_numbers = Movies.query.get_or_404(movie_selected)
        arr_seat_numbers = str(seat_numbers).split('~')
        add_s = int(arr_seat_numbers[2]) + 1
        sub_s = int(arr_seat_numbers[1]) - 1

        seat_numbers.seats_available = sub_s
        seat_numbers.seats_sold = add_s


        # add to the database and commit
        try:
            db.session.add(cus_details)

            db.session.commit()

            return render_template('thankyou.html', ticket_id=ticket_id)
        except:
            return "Error adding to the database"

    return render_template('checkout.html')


# cancelling a tickect using ticket_id
@app.route('/home/cancel', methods=['POST', 'GET'])
def cancel():
    if request.method == 'POST':
        ticket_id = request.form['cancel']

        
        try:
            # select the row to be deleted using the ticket id
            delete = CustomerBooking.query.get_or_404(ticket_id)

            # and select which movie is being deleted (helps with getting the seat to mark as available)
            seat_indx = str(delete).split('~')[4]
            movie = str(delete).split('~')[3]

            seat = [int(seat_indx[0]), int(seat_indx[1])]

            # update the seats
            # use row and column to mark the available seat with 1 (the one that's being deleted)
            if movie == "Jujutsu Kaisen: Zero":
                seats = SeatsM1.query.get_or_404(seat[0] + 1)
        
                if seat[1] == 1:
                    seats.c1 = 0
                elif seat[1] == 2:
                    seats.c2 = 0
                elif seat[1] == 3:
                    seats.c3 = 0
                elif seat[1] == 4:
                    seats.c4 = 0
                elif seat[1] == 5:
                    seats.c5 = 0
                elif seat[1] == 6:
                    seats.c6 = 0
                elif seat[1] == 7:
                    seats.c7 = 0
                elif seat[1] == 8:
                    seats.c8 = 0

                # query and update the number of seats sold/available for this movie
                seat_numbers = Movies.query.get_or_404(movie)
                arr_seat_numbers = str(seat_numbers).split('~')
                add_s = int(arr_seat_numbers[1]) + 1
                sub_s = int(arr_seat_numbers[2]) - 1

                seat_numbers.seats_available = add_s
                seat_numbers.seats_sold = sub_s

            elif movie == "Boku no Hero: World Hero's Mission":
                seats = SeatsM2.query.get_or_404(seat[0] + 1)
        
                if seat[1] == 1:
                    seats.c1 = 0
                elif seat[1] == 2:
                    seats.c2 = 0
                elif seat[1] == 3:
                    seats.c3 = 0
                elif seat[1] == 4:
                    seats.c4 = 0
                elif seat[1] == 5:
                    seats.c5 = 0
                elif seat[1] == 6:
                    seats.c6 = 0
                elif seat[1] == 7:
                    seats.c7 = 0
                elif seat[1] == 8:
                    seats.c8 = 0

                # query and update the number of seats sold/available for this movie
                seat_numbers = Movies.query.get_or_404(movie)
                arr_seat_numbers = str(seat_numbers).split('~')
                add_s = int(arr_seat_numbers[1]) + 1
                sub_s = int(arr_seat_numbers[2]) - 1

                seat_numbers.seats_available = add_s
                seat_numbers.seats_sold = sub_s

            elif movie == "Dragon Ball Super Movie":
                seats = SeatsM3.query.get_or_404(seat[0] + 1)
        
                if seat[1] == 1:
                    seats.c1 = 0
                elif seat[1] == 2:
                    seats.c2 = 0
                elif seat[1] == 3:
                    seats.c3 = 0
                elif seat[1] == 4:
                    seats.c4 = 0
                elif seat[1] == 5:
                    seats.c5 = 0
                elif seat[1] == 6:
                    seats.c6 = 0
                elif seat[1] == 7:
                    seats.c7 = 0
                elif seat[1] == 8:
                    seats.c8 = 0

                # query and update the number of seats sold/available for this movie
                seat_numbers = Movies.query.get_or_404(movie)
                arr_seat_numbers = str(seat_numbers).split('~')
                add_s = int(arr_seat_numbers[1]) + 1
                sub_s = int(arr_seat_numbers[2]) - 1

                seat_numbers.seats_available = add_s
                seat_numbers.seats_sold = sub_s
            

            # delete from the table and commit
            db.session.delete(delete)
            db.session.commit()


            return render_template('aftercancel.html')

        except:
            flash('The ticket id you have entered does not exist!')
            return render_template('cancel.html')
    

    return render_template('cancel.html')

# logout
@app.route('/logout', methods=['GET'])
def logout():

    session.clear()

    return render_template('logout.html')

if __name__ == "__main__":
    app.run(debug=True)
