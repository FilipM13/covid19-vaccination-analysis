USE covid19;
SELECT country, MAX(total_vaccinations), vaccines
	FROM country_vaccines
    GROUP BY country
    ORDER BY MAX(total_vaccinations) DESC;