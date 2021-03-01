USE covid19;
SELECT country, MAX(total_vaccinations), MAX(people_fully_vaccinated_per_hundred), vaccines
	FROM country_vaccines
    GROUP BY country
    ORDER BY MAX(people_fully_vaccinated_per_hundred) DESC;