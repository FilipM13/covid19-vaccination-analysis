USE covid19;
SELECT country, MAX(total_vaccinations), MAX(people_vaccinated), MAX(people_fully_vaccinated)
	FROM country_vaccines
    GROUP BY country
    ORDER BY MAX(total_vaccinations) DESC,
    MAX(people_vaccinated) DESC,
    MAX(people_fully_vaccinated) DESC;
