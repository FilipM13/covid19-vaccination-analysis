USE covid19;
SELECT country, MAX(people_vaccinated_per_hundred)
	FROM country_vaccines
    GROUP BY country
    ORDER BY MAX(people_vaccinated_per_hundred) DESC;
