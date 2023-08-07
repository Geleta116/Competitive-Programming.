# Write your MySQL query statement below
SELECT email from Person
Group By email HAVING Count(email) > 1;