-- student table with columns (name, age, gender)
  CREATE TABLE student (
    name VARCHAR(100) NOT NULL UNIQUE,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL
  );


-- Insert at least 3 records into the student table. Each record should have a unique name, age, and gender.
INSERT INTO student (name, age, gender) 
VALUES
  ('Alice Johnson', 20, 'Female'),
  ('Brian Smith', 22, 'Male'),
  ('Charlie Kim', 19, 'Non-binary');
