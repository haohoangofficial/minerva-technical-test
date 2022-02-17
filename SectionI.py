""""
1. Student attendance data are kept in the following table:
SQL QUERY:

SELECT student_id, COUNT(checkin_date) AS number_of_absent_date
FROM `attendance`
WHERE absent_flag = 1
GROUP BY student_id
HAVING COUNT(checkin_date) > 3
"""