'''Testing Customer class'''
from Customer import Customer
from Notification import Notification

customer_data = {}

customer_data['name'] = "SDSD"
customer_data['surname'] = "Sekhukhune"
customer_data['email'] = "sekhukhune056@gmail.com"
customer_data['contact_no'] = "+27660990075"
customer_data['password'] = 23243
customer_data['seats_booked'] = "5"
customer_data['movie_booked'] = "Dr Strange"
customer_data['is_booked'] = True

customer = Customer(
  customer_data['name'],
  customer_data['surname'],
  customer_data['email'],
  customer_data['password'],
  customer_data['contact_no'],
  customer_data['seats_booked'],
  customer_data['movie_booked']
)

notification = Notification(customer)
#customer.sms_notification()
notification.sms_notification()


