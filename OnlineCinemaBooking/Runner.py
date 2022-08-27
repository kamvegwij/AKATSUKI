'''Testing Customer class'''
from Customer import Customer

customer_data = {}

customer_data['name'] = input("Please enter your name: ")
customer_data['surname'] = input("Please enter your surname: ")
customer_data['email'] = input("Please enter your email: ")
customer_data['contact_no'] = input("Please enter your contact no: ")
customer_data['seats_booked'] = input("Number of seats: ")
customer_data['movie_booked'] = input("Enter the movie booked: ")
customer_data['is_booked'] = True

customer = Customer(
  customer_data['name'],
  customer_data['surname'],
  customer_data['email'],
  customer_data['contact_no'],
  customer_data['seats_booked'],
  customer_data['movie_booked']
)

print(customer.getCustName)
print(customer.getCustSurname)
print(customer.getCustEmail)
print(customer.getCustContactNo)
print(customer.getNoOfSeatsBooked)
print(customer.getMovieSelected)
print(customer.generateCustID)
print(customer.generateCustID)


