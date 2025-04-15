# SQL Assignment: Creating and Managing Databases

## 📝 Assignment Description
This assignment involves working with basic SQL commands to create and manage databases. The two tasks include:

1. **Creating a Sales Database (`SalesDB`)**
2. **Creating and Dropping a School Database (`SchoolDB`)**

These tasks reinforce foundational SQL skills in database creation and deletion.

---

## 🚀 What I Did

### Task 1: Creating `SalesDB`
I wrote an SQL query to create a new database named `SalesDB`.

```sql
CREATE DATABASE SalesDB;
```

## Task 2: Creating and Dropping SchoolDB

I first created a test database called `SchoolDB`, then used the `DROP` command to delete it — simulating a scenario where a test database is removed after use.

```sql
CREATE DATABASE SchoolDB;
DROP DATABASE SchoolDB;
```

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
4. After executing:
   - `SalesDB` will be created
   - `SchoolDB` will be created and then deleted

---

## 📂 Folder Structure
```
SQL-Databases-Practice/
├── README.md
├── sales_school_databases.sql
```


---

## 📌 Notes

- The `DROP DATABASE` command permanently deletes the database — use it carefully
- No tables were created in this task; it focuses solely on syntax and basic database management for educational purposes
