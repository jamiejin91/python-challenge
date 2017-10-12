# 1a
SELECT first_name, last_name FROM actor;

# 1b
SELECT upper(concat(firt_name, ' ', last_name)) AS actor name FROM actor;

# 2a
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = "Joe";

# 2b
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name = "%gen%"

# 2c
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name = "%li%"
ORDER BY last_name, first_name

# 2d
SELECT country_id, country
FROM country          
WHERE country IN (Afghanistan, Bangladesh, China);

# 3a
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(45) NOT NULL AFTER first_name;

# 3b
ALTER TABLE actor
MODIFY middle_name blob;

# 3c
ALTER TABLE actor
DROP COLUMN middle_name;

# 4a
SELECT last_name, count(last_name)
FROM actor
GROUP BY last_name;

# 4b
SELECT last_name, count(last_name)
FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;

# 4c
UPDATE actor
SET first_name = "Harpo"
WHERE first_name = "Groucho" AND last_name = "Williams";

# 4d
UPDATE actor
SET first_name = "Mucho Groucho"
WHERE first_name = "Harpo" AND last_name = "Williams";

# 5a

# 6a
SELECT staff.first_name, staff.last_name, address.address
FROM address
INNER JOIN staff ON staff.address_id = address.address_id;

# 6b
SELECT staff.first_name, staff.last_name,payment.amount
FROM payment
INNER JOIN staff ON 

# 6c

# 6d

# 6e

# 7a

# 7b

# 7c

# 7d

# 7e

# 7f

# 7g

# 7h

# 8a

# 8b

# 8c