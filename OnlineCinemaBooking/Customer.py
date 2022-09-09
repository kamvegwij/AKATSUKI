

'''
Cinema Online booking Customer class
-Used to capture customer information
'''

class Customer:
    def __init__(self, name, surname, email, movie_selected):
        # personal details
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__movie = movie_selected



    '''Getter functions'''
    @property
    def get_cust_name(self):
        return self.__name

    @property
    def get_cust_surname(self):
        return self.__surname

    @property
    def get_cust_email(self):
        return self.__email

    @property
    def get_cust_contact_no(self):
        return self.__contact_no

    @property
    def get_password(self):
        return self.__password

    @property
    def get_no_of_seats_booked(self):
        return self.__no_seats_booked

    @property
    def get_movie_selected(self):
        return self.__movie

    @property
    def generate_cust_ID(self):
        self.__customer_id += 1
        return self.__customer_id

    @property
    def get_booking_status(self):
        return self.__is_booked

    '''Setter functions'''
    def set_cust_name(self, name):
        self.__name = name

    def set_cust_surname(self, surname):
        self.__surname = surname

    def set_cust_contact(self, contact):
        self.__contact_no = contact

    def set_password(self, password):
        self.__password = password

    def set_seats_booked(self, seats):
        self.__no_seats_booked = seats

    def set_cust_id(self, ID):
        self.__customer_id = ID

    def set_movie_selected(self, movie):
        self.__movie = movie


    '''This function will enable customer to view and receive provided
       the customer has booked.
    '''



    '''
    def email_notification(self):
        if self.__is_booked:
            with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
                connection.starttls()
                connection.login(
                    user="akatsukiakatsuki241@yahoo.com",
                    password="CSC312_Term3_Mini_Project_2022"
                )
                connection.sendmail(
                    from_addr="akatsukiakatsuki241@yahoo.com",
                    to_addrs=f"{self.__email}",
                    msg="Show will be ready in x time o clock"
                )
    '''







