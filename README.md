This is a Python script that implements a movie booking system. It has two main categories of users: administrators and regular users. Administrators can add, update, delete movies, and list all movies and bookings. Regular users can book tickets, list available movies, list their bookings, and cancel bookings.

The script uses a MySQL database to store movie and booking information. It uses the mysql.connector library to connect to the database.

The script has several functions to perform different tasks:

Administrator functions:
add_movie: Adds a new movie to the database.
update_movie: Updates an existing movie in the database.
delete_movie: Deletes a movie from the database.
list_movies_admin: Lists all movies in the database for administrators.
list_bookings_admin: Lists all bookings in the database for administrators.
User functions:
book_ticket: Books a ticket for a selected movie.
list_movies_user: Lists all available movies for booking.
list_bookings_user: Lists all bookings for a specific user.
cancel_booking: Cancels a ticket booking.
The script uses a simple text-based menu system to allow users to select different options.

To use this script, you need to have Python and MySQL installed on your system. You also need to create a MySQL database and grant privileges to a user. You can then update the connect_to_db function in the script with your database credentials.

