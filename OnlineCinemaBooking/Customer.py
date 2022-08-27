
from marshmallow import Schema, fields, post_load, ValidationError, validates, validate
import phonenumbers

'''
Cinema Online booking Customer class
-Used to capture customer information
'''

class Customer:
    def __init__(self, name, surname, email, contactNo, noOfSeatsBooked, movieSelected):
        self.__name = name
        self.__surname = surname
        self.__contactNo = contactNo
        self.__email = email
        self.__noOfSeatsBooked = noOfSeatsBooked
        self.__movie = movieSelected
        self.__customerID = 0


    '''Getter functions'''
    def getCustName(self):
        return self.__name

    def getCustSurname(self):
        return self.__surname

    def getCustEmail(self):
        return self.__email

    def getCustContactNo(self):
        return self.__contactNo

    def getNoOfSeatsBooked(self):
        return self.__noOfSeatsBooked

    def getMovieSelected(self):
        return self.__movie

    def generateCustID(self):
        self.__customerID += 1
        return self.__customerID

    '''Setter functions'''
    def setCustName(self, name):
        self.__name = name

    def setCustSurname(self, surname):
        self.__surname = surname

    def setCustContact(self, contact):
        self.__contactNo = contact

    def setCustNoOfSeatsBooked(self, seats):
        self.__noOfSeatsBooked = seats

    def setCustIDe(self, ID):
        self.__customerID = ID

    def setMovieSelected(self, movie):
        self.__movie = movie


'''Customer Validation class
-Used to validate customer input
'''
class CustomerSchema(Schema):
    name = fields.String()
    surname = fields.String()
    contactNo = fields.String()
    noOfBookSeats = fields.Integer()
    email = fields.Email()
    movie = fields.String()

    @validates('contactNo')
    def validate_contactNo(self, contactNo):
        phone_number = phonenumbers.parse(contactNo)
        isContactNoPossible = phonenumbers.is_valid_number(phone_number)
        return isContactNoPossible

    @post_load
    def create_customer(self, data, **kwargs):
        return Customer(**data)



'''Testing class'''
customer_data = {}

customer_data['name'] = input("Enter your name: ")
customer_data['surname'] = input("Enter your surname: ")
customer_data['email'] = input("Enter your email: ")
customer_data['contact_no'] = input("Enter your phone numbers: ")
customer_data['noOfSeatsBooked'] = input("Number of seats booked: ")
customer_data['movie_selected'] = input("Enter movie: ")
customer_data['customer_id'] = input("Enter customer id: ")

try:
    schema = CustomerSchema()
    customer = schema.load(customer_data)

    results = schema.dump(customer)
    print(results)
except ValidationError as err:
    print(err)
    print(err.valid_data)






