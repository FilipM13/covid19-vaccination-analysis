USE covid19;
SELECT country, ROUND(AVG(daily_vaccinations_per_million)/10000, 2)
	FROM country_vaccines
    GROUP BY country
    ORDER BY AVG(daily_vaccinations_per_million) DESC;
