SELECT DATE(paymentDate) AS payment_date, SUM(amount) AS total_amount
FROM payments
GROUP BY DATE(paymentDate)
ORDER BY DATE(paymentDate) DESC
LIMIT 5;



-- DATE(payment_date) is used to group payments by date only, ignoring the time. The DATE() function is used here to prevent the different timestamps in a single day to be treated as different groups. It strips the time, so you group by the full calendar date.
