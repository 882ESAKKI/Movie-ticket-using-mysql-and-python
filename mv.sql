CREATE TABLE Movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    duration INT NOT NULL,
    rating FLOAT NOT NULL
);

CREATE TABLE Tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);