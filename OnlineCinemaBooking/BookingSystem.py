class BookingSystem:
    def __init__(self, customer):
        self.customer = customer
        self.movies = {
            "Movie-1" : {
                "seats_sold": 0,
                "seats_available": 20
            },
            "Movie-2" : {
                "seats_sold": 0,
                "seats_available": 20
            },
            "Movie-3" : {
                "seats_sold": 0,
                "seats_available": 20
            }
        }
        
    def book_movie(self):
        if self.movies[self.customer.movie_selected]['seats_available'] != 0:
            self.movies[self.customer.movie_selected]['seats_sold'] += self.customer.seats_booked
            self.movies[self.customer.movie_selected]['seats_available'] -= self.customer.seats_booked
            self.customer.is_booked = True
            return f"Tickets"
        else:
            return f"Sorry {self.movies[self.customer.movie_selected]} seats are sold."

    def customer_booking_info(self):
        

            




