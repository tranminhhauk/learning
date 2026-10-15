SELECT first_name, last_name FROM person;
SELECT first_name FROM person WHERE gender = 'MALE';
SELECT first_name, date_of_birth FROM person WHERE date_of_birth >= '2003-01-01';
SELECT first_name, email FROM person WHERE email IS NULL;
SELECT first_name, last_name FROM person WHERE LOWER(last_name) IN ('tran', 'le');

SELECT * FROM person ORDER BY last_name DESC;
SELECT first_name, date_of_birth FROM person ORDER BY date_of_birth ASC LIMIT 3;
SELECT * FROM person WHERE gender = 'FEMALE' ORDER BY date_of_birth DESC LIMIT 2;
SELECT * FROM person ORDER BY first_name ASC OFFSET 2 LIMIT 3;

SELECT * FROM person WHERE email ILIKE '%@gmail.com';
SELECT * FROM person WHERE first_name ILIKE 'K%' OR first_name ILIKE 'L%';
SELECT * FROM person WHERE first_name ILIKE '___';
SELECT * FROM person WHERE gender = 'Male' and date_of_birth < '2001-01-01' AND email IS NOT NULL;
SElECT * FROM person WHERE first_name ILIKE '%a%';
SELECT COUNT(*) FROM person; 
SELECT COUNT(email) FROM person;
SELECT MIN(date_of_birth), MAX(date_of_birth) FROM person;
SELECT gender, COUNT(*) FROM person GROUP BY gender;

SELECT EXTRACT(YEAR FROM date_of_birth) AS nam_sinh, COUNT(*) FROM person GROUP by nam_sinh HAVING COUNT(*)>2;

SELECT gender, COUNT(*) as so_luong FROM person GROUP BY gender HAVING COUNT(*) >2;

SELECT gender AS gioi_tinh, COUNT(*) AS so_luong FROM person GROUP BY gender;

SELECT gender,
       EXTRACT(YEAR FROM date_of_birth) AS nam_sinh,
       COUNT(*) AS so_luong
FROM person
GROUP BY gender, nam_sinh
HAVING COUNT(*) > 1;