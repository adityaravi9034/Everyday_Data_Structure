"""Question:
You are developing a movie ticket booking system. The system allows users to book movie tickets for a theater. 
Each theater has multiple screens, and each screen shows a specific movie at different showtimes.
Users can select a movie, choose a showtime, and book tickets for a desired number of seats.

Design a data structure and implement the necessary functions to support the movie ticket booking system.
The data structure should store information about theaters, movies, screens, showtimes, and available seats.
Additionally, the functions should include the ability to check seat availability, book seats, and retrieve booking details.

Write a class MovieTicketBookingSystem that represents the movie ticket booking system. The class should include the following methods:

add_theater(theater_name): Adds a new theater to the system with the given name.
add_movie(theater_name, movie_name): Adds a new movie to the specified theater.
add_screen(theater_name, screen_name): Adds a new screen to the specified theater.
add_showtime(theater_name, screen_name, movie_name, showtime): Adds a showtime for the specified movie and screen in the given theater.
get_available_seats(theater_name, screen_name, movie_name, showtime): Returns the list of available seats for the specified movie, screen, and showtime.
book_tickets(theater_name, screen_name, movie_name, showtime, num_seats): Books the specified number of seats for the given movie, screen, and showtime.
get_booking_details(theater_name, screen_name, movie_name, showtime): Returns the booking details for the specified movie, screen, and showtime.
You can assume that the theater names, movie names, and screen names are unique within the system."""

class MovieTicketBookingSystem:
    def __init__(self):
        self.theaters = {}

    def add_theater(self, theater_name):
        self.theaters[theater_name] = {}

    def add_movie(self, theater_name, movie_name):
        self.theaters[theater_name][movie_name] = {}

    def add_screen(self, theater_name, screen_name):
        self.theaters[theater_name][screen_name] = {}

    def add_showtime(self, theater_name, screen_name, movie_name, showtime):
        self.theaters[theater_name][screen_name][movie_name] = {showtime: []}

    def get_available_seats(self, theater_name, screen_name, movie_name, showtime):
        return self.theaters[theater_name][screen_name][movie_name][showtime]

    def book_tickets(self, theater_name, screen_name, movie_name, showtime, num_seats):
        available_seats = self.get_available_seats(theater_name, screen_name, movie_name, showtime)
        if len(available_seats) >= num_seats:
            booked_seats = available_seats[:num_seats]
            self.theaters[theater_name][screen_name][movie_name][showtime] = available_seats[num_seats:]
            return booked_seats
        else:
            return []

    def get_booking_details(self, theater_name, screen_name, movie_name, showtime):
        available_seats = self.get_available_seats(theater_name, screen_name, movie_name, showtime)
        booked_seats = [seat for seat in self.the```python
class MovieTicketBookingSystem:
    def __init__(self):
        self.theaters = {}

    def add_theater(self, theater_name):
        self.theaters[theater_name] = {}

    def add_movie(self, theater_name, movie_name):
        self.theaters[theater_name][movie_name] = {}

    def add_screen(self, theater_name, screen_name):
        self.theaters[theater_name][screen_name] = {}

    def add_showtime(self, theater_name, screen_name, movie_name, showtime):
        self.theaters[theater_name][screen_name][movie_name] = {showtime: []}

    def get_available_seats(self, theater_name, screen_name, movie_name, showtime):
        return self.theaters[theater_name][screen_name][movie_name][showtime]

    def book_tickets(self, theater_name, screen_name, movie_name, showtime, num_seats):
        available_seats = self.get_available_seats(theater_name, screen_name, movie_name, showtime)
        if len(available_seats) >= num_seats:
            booked_seats = available_seats[:num_seats]
            self.theaters[theater_name][screen_name][movie_name][showtime] = available_seats[num_seats:]
            return booked_seats
        else:
            return []

    def get_booking_details(self, theater_name, screen_name, movie_name, showtime):
        available_seats = self.get_available_seats(theater_name, screen_name, movie_name, showtime)
        booked_seats = [seat for seat in available_seats]
        return booked_seats


# Example usage:
booking_system = MovieTicketBookingSystem()

# Add a theater
booking_system.add_theater("Theater A")

# Add a movie to the theater
booking_system.add_movie("Theater A", "Movie 1")

# Add a screen to the theater
booking_system.add_screen("Theater A", "Screen 1")

# Add a showtime for the movie on the screen in the theater
booking_system.add_showtime("Theater A", "Screen 1", "Movie 1", "9:00 AM")

# Get available seats for the showtime
available_seats = booking_system.get_available_seats("Theater A", "Screen 1", "Movie 1", "9:00 AM")
print("Available seats:", available_seats)

# Book 2 seats for the showtime
booked_seats = booking_system.book_tickets("Theater A", "Screen 1", "Movie 1", "9:00 AM", 2)
print("Booked seats:", booked_seats)

# Get booking details for the showtime
booking_details = booking_system.get_booking_details("Theater A", "Screen 1", "Movie 1", "9:00 AM")
print("Booking details:", booking_details)
# Example usage (continued):
# Book 2 seats for the showtime
booked_seats = booking_system.book_tickets("Theater A", "Screen 1", "Movie 1", "9:00 AM", 2)
print("Booked seats:", booked_seats)

# Get booking details for the showtime
booking_details = booking_system.get_booking_details("Theater A", "Screen 1", "Movie 1", "9:00 AM")
print("Booking details:", booking_details)
