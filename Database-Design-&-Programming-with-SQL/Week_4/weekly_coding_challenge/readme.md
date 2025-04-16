# SQL Query to Summarize Payments by Date

## Assignment Overview  
In this assignment, I was tasked with writing a query to retrieve payment statistics from a database. The focus is on using **aggregate functions**, **sorting**, and **limiting results** effectively. The challenge consists of three main goals:

1. **Calculate the total amount paid** on each payment date from the `payments` table.
2. **Display the payment date and total amount** paid on that date.
3. **Sort and limit** the result to show only the top 5 most recent payment dates.

---

## Table Structure  

### **Payments Table 💳**
The **Payments** table stores transaction data including payment amounts and the dates they were made.

| Column       | Data Type | Description                            |
|--------------|-----------|----------------------------------------|
| payment_id   | INT       | Unique identifier for each payment 🧾 |
| customer_id  | INT       | ID of the customer who made the payment 🙋 |
| staff_id     | INT       | ID of the staff who processed it 👨‍💼 |
| rental_id    | INT       | Associated rental transaction ID 🎬 |
| amount       | DECIMAL   | The payment amount 💰 |
| payment_date | DATETIME  | The date and time of the payment 🗓️ |

> *Note: This table is part of the `sampleDB` database shared during Week 2 class.*

---

## 🛠️ Requirements

- Basic knowledge of SQL aggregate functions (e.g., `SUM`)
- Understanding of `GROUP BY`, `ORDER BY`, and `LIMIT`
- Access to an SQL environment (e.g., MySQL Workbench, DBeaver, SQLite)

---

## ▶️ How to Run

1. Open your SQL execution environment.
2. Connect to the `sampleDB` database used in class.
3. Paste and run the SQL query inside answers.sql

---

## 📂 Folder Structure
```
weekly_coding_challenge/
├── README.md
├── answers.sql
```


---

## 📌 Notes
- DATE(payment_date) is used to group payments by date only, ignoring the time.

- SUM(amount) helps calculate the total payment per date.

- ORDER BY payment_date DESC ensures the latest dates appear first.

- LIMIT 5 shows only the top 5 most recent payment dates.
