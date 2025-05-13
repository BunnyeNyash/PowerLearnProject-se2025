# Airbnb Database

## Project Title
Airbnb Database Management System

## Description
This project is a MySQL-based relational database designed for an Airbnb-like platform. It manages users (guests, hosts, admins), properties, bookings, payments, reviews, and messages. The database includes:
- Six tables with primary keys (UUIDs), foreign keys, and constraints (NOT NULL, UNIQUE, CHECK).
- One-to-many relationships: User to Property, User to Booking, Property to Booking, Booking to Payment, User to Review, Property to Review, User to Message (sender/recipient).
- Features to track property listings, reservations, payments, guest reviews, and user communications.

This project was developed as part of the Week 8 Assignment for a database management course.

## Folder Structure
The project files:
```
airbnb-database/
├── airbnb.sql
├── README.md
├── airbnb-database-ERD.drawio.png
```

## How to Run/Setup the Project
1. **Prerequisites**: Install MySQL (e.g., MySQL Community Server) on your system.
2. **Clone the Assignment Directory (Recommended)**:
   Use Git sparse checkout to clone only the `Database-Design-&-Programming-with-SQL/Week_8/assignment` directory:
   ```bash
   git clone --no-checkout https://github.com/BunnyeNyash/PowerLearnProject-se2025.git
   cd PowerLearnProject-se2025
   git sparse-checkout init --cone
   git sparse-checkout set Database-Design-&-Programming-with-SQL/Week_8/assignment
   git checkout main
   cd Database-Design-&-Programming-with-SQL/Week_8/assignment
   ```
   Alternatively, download `airbnb.sql`, `README.md`, and `erd.png` directly from the [GitHub repository](https://github.com/BunnyeNyash/PowerLearnProject-se2025/tree/main/Database-Design-%26-Programming-with-SQL/Week_8/assignment).
3. **Import the SQL File**:
   - Open MySQL Workbench or your preferred MySQL client.
   - Create a new database:
     ```sql
     CREATE DATABASE airbnb;
     ```
   - Select the database:
     ```sql
     USE airbnb;
     ```
   - Import the `airbnb.sql` file by specifying its full file path
     ```sql
     SOURCE path/to/airbnb.sql;
     ```
       e.g.,
         `C:/path/to/PowerLearnProject-se2025/Database-Design-&-Programming-with-SQL/Week_8/assignment/airbnb.sql` on Windows or `/path/to/PowerLearnProject-se2025/Database-Design-&-Programming-with-SQL/Week_8/assignment/airbnb.sql` on Linux/Mac

     replace the `/path/to` with the real path
     
   - Or via command line, replacing `<your_username>` with your MySQL username (e.g., `root` or a custom username):
     ```bash
     mysql -u your_username -p airbnb < airbnb.sql
     ```
       e.g.,
         `mysql -u <your_username> -p airbnb < /path/to/PowerLearnProject-se2025/Database-Design-&-Programming-with-SQL/Week_8/assignment/airbnb.sql`

     When prompted, enter your MySQL password.

     replace the `/path/to` with the real path

     
4. **Generate UUIDs**: Primary keys use UUIDs. Generate them using MySQL’s `UUID()` function with char(36) or (REPLACE(UUID(), '-', '') with char(32). (e.g., `INSERT INTO User (user_id, ...) VALUES (UUID(), ...)` to get the UUIDs with the hyphens or `INSERT INTO User (user_id, ...) VALUES (REPLACE(UUID(), '-', ''), ...);` to get the UUIDs without the hyphens). Ours opts for the one WITHOUT the hyphens; char(32).
   
5. **Verify**: Query the tables to ensure they were created (e.g., `SHOW TABLES;`).

## Entity-Relationship Diagram (ERD)
The ERD for this database is included as [airbnb-database-ERD.drawio.png](https://github.com/BunnyeNyash/PowerLearnProject-se2025/blob/123ebe02719f39b9b9b9c1430b74d3a4c3391592/Database-Design-%26-Programming-with-SQL/Week_8/assignment/airbnb-database-ERD.drawio.png). It visualizes the six tables, their attributes, primary/foreign keys, and one-to-many relationships.
