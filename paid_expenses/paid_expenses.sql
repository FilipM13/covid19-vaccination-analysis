USE covid19;
SELECT country, MAX(total_vaccinations), MAX(total_vaccinations_per_hundred), vaccines
	FROM country_vaccines
    GROUP BY country
    ORDER BY MAX(total_vaccinations) DESC;