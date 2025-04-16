# SQL Table Creation and Insertion

## Assignment Overview
In this assignment, I was tasked with creating a table and inserting records using SQL commands. The challenge consists of two main tasks:

1. **Create a `student` table** with specified columns and constraints.
2. **Insert at least three records** into the table with unique data.

---


## Table Structure

### **Student Table 🌟**
The **Student** table will store details about each student.

| Column | Data Type | Description |
|--------|-----------|-------------|
| name    | VARCHAR(100)   | A unique ID for each student 🎟️ |
| age     | INT            | The student's age 🎭 |
| gender  | VARCHAR(10)    | The student's gender 🌟 |


- `name` – a string (VARCHAR) with a maximum length of 100 characters.
- `age` – an integer representing the student's age.
- `gender` – a string (VARCHAR) with a maximum length of 10 characters.


---
## 🛠️ Requirements

- Basic SQL knowledge
- An SQL-compatible database system (e.g., MySQL, PostgreSQL, SQLite, SQL Server)
- A query execution environment (e.g., MySQL Workbench, DBeaver, pgAdmin, or terminal)

---

## ▶️ How to Run

1. Open an SQL environment (e.g., MySQL Workbench, pgAdmin, SQLite, etc.)
2. Copy and paste each query
3. Run the queries one by one to see the results
   - CREATE TABLE statement to define the structure.
   - INSERT INTO commands to populate the table.

---


## 📂 Folder Structure
```
weekly_coding_challenge/
├── README.md
├── student.sql
```


---

## 📌 Notes
- The VARCHAR data types allow flexibility for text input while maintaining reasonable size limits.
- Gender is kept flexible with a 10-character limit to support inclusive values.

