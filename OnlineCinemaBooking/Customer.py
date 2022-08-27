
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
        self.__isBooked = False



    '''Getter functions'''
    @property
    def getCustName(self):
        return self.__name

    @property
    def getCustSurname(self):
        return self.__surname

    @property
    def getCustEmail(self):
        return self.__email

    @property
    def getCustContactNo(self):
        return self.__contactNo

    @property
    def getNoOfSeatsBooked(self):
        return self.__noOfSeatsBooked

    @property
    def getMovieSelected(self):
        return self.__movie

    @property
    def generateCustID(self):
        self.__customerID += 1
        return self.__customerID

    @property
    def getBookingStatus(self):
        return self.__isBooked

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


    '''This function will enable customer to view and receive provided
       the customer has booked.
    '''

    def viewBookingInfo(self):
        pass




