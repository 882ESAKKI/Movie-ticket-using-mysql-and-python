import mysql.connector

def connect_to_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MovieBook"
    )

# --- Administrator Functions ---
def add_movie(title, genre, duration, rating):
    """Add a movie to the database."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        sql = "INSERT INTO Movies (title, genre, duration, rating) VALUES (%s, %s, %s, %s)"
        values = (title, genre, int(duration), float(rating))
        cursor.execute(sql, values)
        db.commit()
        print(f"Movie '{title}' added successfully.")
        db.close()
    except Exception as e:
        print(f"Failed to add movie: {e}")

def update_movie(movie_id, title=None, genre=None, duration=None, rating=None):
    """Update an existing movie in the database."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        updates = []
        values = []

        if title:
            updates.append("title = %s")
            values.append(title)
        if genre:
            updates.append("genre = %s")
            values.append(genre)
        if duration:
            updates.append("duration = %s")
            values.append(int(duration))
        if rating:
            updates.append("rating = %s")
            values.append(float(rating))

        if updates:
            values.append(int(movie_id))
            sql = f"UPDATE Movies SET {', '.join(updates)} WHERE movie_id = %s"
            cursor.execute(sql, tuple(values))
            db.commit()
            print(f"Movie with ID {movie_id} updated successfully.")
            db.close()
        else:
            print("No updates provided.")
    except Exception as e:
        print(f"Failed to update movie: {e}")

def delete_movie(movie_id):
    """Delete a movie from the database."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        sql = "DELETE FROM Movies WHERE movie_id = %s"
        cursor.execute(sql, (int(movie_id),))
        db.commit()
        print(f"Movie with ID {movie_id} deleted successfully.")
        db.close()
    except Exception as e:
        print(f"Failed to delete movie: {e}")

def list_movies_admin():
    """List all movies in the database for Admin."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Movies")
        movies = cursor.fetchall()
        db.close()

        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Duration: {movie[3]} min, Rating: {movie[4]}/10")
    except Exception as e:
        print(f"Failed to retrieve movies: {e}")

def list_bookings_admin():
    """List all ticket bookings in the database for Admin."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT T.ticket_id, T.customer_name, M.title FROM Tickets T JOIN Movies M ON T.movie_id = M.movie_id")
        bookings = cursor.fetchall()
        db.close()

        if bookings:
            for booking in bookings:
                print(f"Ticket ID: {booking[0]}, Customer: {booking[1]}, Movie: {booking[2]}")
        else:
            print("No bookings available.")
    except Exception as e:
        print(f"Failed to retrieve bookings: {e}")

# --- User Functions ---
def book_ticket(movie_id, customer_name):
    """Book a ticket for the selected movie."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        
        # Check if the movie exists
        cursor.execute("SELECT * FROM Movies WHERE movie_id = %s", (int(movie_id),))
        movie = cursor.fetchone()
        
        if movie:
            sql = "INSERT INTO Tickets (movie_id, customer_name) VALUES (%s, %s)"
            cursor.execute(sql, (int(movie_id), customer_name))
            db.commit()
            print(f"Ticket booked for {customer_name} for movie '{movie[1]}' successfully.")
            db.close()
        else:
            print("Movie ID not found.")
    except Exception as e:
        print(f"Failed to book ticket: {e}")

def list_movies_user():
    """List all available movies for booking."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Movies")
        movies = cursor.fetchall()
        db.close()

        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Duration: {movie[3]} min, Rating: {movie[4]}/10")
    except Exception as e:
        print(f"Failed to retrieve movies: {e}")

def list_bookings_user(customer_name):
    """List all ticket bookings for the user."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT T.ticket_id, M.title FROM Tickets T JOIN Movies M ON T.movie_id = M.movie_id WHERE T.customer_name = %s", (customer_name,))
        bookings = cursor.fetchall()
        db.close()

        if bookings:
            for booking in bookings:
                print(f"Ticket ID: {booking[0]}, Movie: {booking[1]}")
        else:
            print("No bookings available.")
    except Exception as e:
        print(f"Failed to retrieve bookings: {e}")

def cancel_booking(ticket_id):
    """Cancel a ticket booking."""
    try:
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Tickets WHERE ticket_id = %s", (int(ticket_id),))
        db.commit()
        print(f"Ticket with ID {ticket_id} cancelled successfully.")
        db.close()
    except Exception as e:
        print(f"Failed to cancel ticket: {e}")

# Main program
while True:
    print("\nMovie Booking System")
    print("1. Administrator Functions")
    print("2. User Functions")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nAdministrator Functions")
        print("1. Add Movie")
        print("2. Update Movie")
        print("3. Delete Movie")
        print("4. List Movies")
        print("5. List Bookings")
        
        admin_choice = input("Enter your choice: ")
        
        if admin_choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            duration = input("Enter movie duration (in minutes): ")
            rating = input("Enter movie rating (out of 10): ")
            add_movie(title, genre, duration, rating)
        elif admin_choice == "2":
            movie_id = input("Enter movie ID: ")
            title = input("Enter new title (optional): ")
            genre = input("Enter new genre (optional): ")
            duration = input("Enter new duration (optional): ")
            rating = input("Enter new rating (optional): ")
            update_movie(movie_id, title, genre, duration, rating)
        elif admin_choice == "3":
            movie_id = input("Enter movie ID: ")
            delete_movie(movie_id)
        elif admin_choice == "4":
            list_movies_admin()
        elif admin_choice == "5":
            list_bookings_admin()
        else:
            print("Invalid choice. Please try again.")
            
    elif choice == "2":
        print("\nUser Functions")
        print("1. Book Ticket")
        print("2. List Movies")
        print("3. List Bookings")
        print("4. Cancel Booking")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            movie_id = input("Enter movie ID: ")
            customer_name = input("Enter your name: ")
            book_ticket(movie_id, customer_name)
        elif user_choice == "2":
            list_movies_user()
        elif user_choice == "3":
            customer_name = input("Enter your name: ")
            list_bookings_user(customer_name)
        elif user_choice == "4":
            ticket_id = input("Enter ticket ID: ")
            cancel_booking(ticket_id)
        else:
            print("Invalid choice. Please try again.")
            
    elif choice == "3":
        print("Exiting the system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")