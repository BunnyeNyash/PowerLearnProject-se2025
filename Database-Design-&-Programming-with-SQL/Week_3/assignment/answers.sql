-- QUESTION 1
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- QUESTION 2
INSERT INTO student (id, fullName, age)
VALUES 
    (1, "Jane Doe", 20),
    (2, "John Doe", 25),
    (3, "Winter Joe", 19);

-- QUESTION 3
UPDATE student
SET age = 20
WHERE id = 2;
