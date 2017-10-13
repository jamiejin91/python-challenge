USE sakila

# 1a
SELECT first_name, last_name FROM actor;

# 1b
SELECT upper(concat(first_name, ' ', last_name)) AS 'actor name'
FROM actor;

# 2a
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';

# 2b
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%gen%'

# 2c
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%li%'
ORDER BY last_name, first_name

# 2d
SELECT country_id, country
FROM country          
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

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
SET first_name = 'Harpo'
WHERE first_name = 'Groucho' AND last_name = 'Williams';

# 4d
UPDATE actor
SET first_name = CASE
   WHEN first_name = 'Harpo' THEN 'Groucho'
   ELSE 'Mucho Groucho'
END
WHERE (first_name = 'Harpo' OR first_name = 'Groucho' OR first_name = 'Mucho Groucho')
AND last_name = 'Williams';

# 5a
CREATE TABLE address (
  address_id SMALLINT NOT NULL,
  address VARCHAR(50),
  address2 VARCHAR(50),
  district VARCHAR(20),
  city_id SMALLINT,
  postal_code VARCHAR(10),
  phone VARCHAR(20),
  last_donate TIMESTAMP
  PRIMARY KEY (address_id)
);

# 6a
SELECT staff.first_name, staff.last_name, address.address
FROM staff
JOIN address
ON (staff.address_id = address.address_id);

# 6b
SELECT concat(staff.first_name, ' ', staff.last_name) AS 'full_name', sum(payment.amount) AS 'total_amount'
FROM staff
JOIN payment
ON (staff.staff_id = payment.staff_id)
WHERE payment.payment_date BETWEEN '2005-08-01 00:00:00' AND '2005-09-01 00:00:00'
GROUP BY full_name;

# 6c
SELECT film.title, sum(film_actor.actor_id) AS 'num_of_actors'
FROM film
INNER JOIN film_actor
ON (film.film_id = film_actor.film_id)
GROUP BY title;

# 6d
SELECT film.title, sum(inventory_id) AS 'num_of_copies'
FROM film
JOIN inventory
ON (film.film_id = inventory.film_id)
WHERE film.title = 'Hunchback Impossible'
GROUP BY film.title;

# 6e
SELECT customer.customer_id, customer.first_name, customer.last_name, sum(payment.amount) AS 'total_paid'
FROM customer
JOIN payment
ON (customer.customer_id = payment.customer_id)
GROUP BY customer.customer_id
ORDER BY customer.last_name;

# 7a
SELECT title
FROM film
where language_id IN
(
	SELECT language_id
    FROM language
    where name = 'English'
)
AND title LIKE 'k%'
OR title LIKE 'q%';

# 7b
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
(
	SELECT actor_id
    FROM film
    WHERE title = 'Alone Trip'
);

# 7c
SELECT first_name, last_name, email
FROM customer
WHERE address_id IN
(
	SELECT address_id
    FROM address
    WHERE city_id IN
    (
		SELECT city_id
        FROM city
        WHERE country_id IN
        (
			SELECT country_id
            FROM country
            WHERE country = 'Canada'
		)
	)
);

# 7d
SELECT *
FROM film
WHERE film_id IN
(
	SELECT film_id
    FROM film_category
    WHERE category_id IN
    (
		SELECT category_id
        FROM category
        WHERE name = 'Family'
	)
);

# 7e
SELECT film.title, count(rental.rental_date) AS 'num_of_rentals'
FROM film
JOIN inventory
ON (film.film_id = inventory.film_id)
JOIN rental
ON (inventory.inventory_id = rental.inventory_id)
GROUP BY film.title
ORDER BY num_of_rentals DESC;

# 7f
SELECT staff.store_id, sum(payment.amount) as 'total_earned'
FROM payment
JOIN staff
ON (payment.staff_id = staff.staff_id)
GROUP BY staff.store_id;

# 7g
SELECT store.store_id, city.city, country.country
FROM store
JOIN address
ON (store.address_id = address.address_id)
JOIN city
ON (address.city_id = city.city_id)
JOIN country
ON (city.country_id = country.country_id);

# 7h

# 8a

# 8b

# 8c