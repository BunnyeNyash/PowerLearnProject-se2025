-- Build and query a simple database about movies, actors.
CREATE movieDB;
USE movieDB;

-- Tables `Movies` and `Actors  .
CREATE TABLE Movies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL
);


CREATE TABLE Actors (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL UNIQUE,
  year YEAR NOT NULL DEFAULT CURRENT_
);



-- queries
INSERT INTO Movies (id, name, age)
VALUES 
  (1, 'Robert Downey Jr.', 56),
  (2, 'Scarlett Johansson', 36),
  (3, 'Chris Hemsworth', 37);


INSERT INTO Actors (id, title, year)
VALUES
  (1, 'Iron Man', 2008),
  (2, 'The Avengers', 2012),
  (3, 'Thor: Ragnarok', 2017);
 
