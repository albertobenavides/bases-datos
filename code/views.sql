-- Vista de los salarios por jugador

DROP VIEW IF EXISTS player_salary_year;
DROP VIEW IF EXISTS overweight_batters;

SELECT p.nameFirst, p.nameLast, s.salary, s.yearID
	FROM people AS p
	LEFT JOIN salaries AS s
	ON p.playerID = s.playerID;

SELECT p.nameFirst, p.nameLast, s.salary, s.yearID
	FROM people AS p
	RIGHT JOIN salaries AS s
	ON p.playerID = s.playerID;


CREATE VIEW player_salary_year AS
	SELECT p.nameFirst, p.nameLast, s.salary, s.yearID
		FROM people AS p
		RIGHT JOIN salaries AS s
		ON p.playerID = s.playerID;
		
SELECT * FROM player_salary_year;

SHOW FULL TABLES;

-- Vista de los jugadores con sobrepeso II que tras batear llegaron a 3a base o hicieron HR
-- https://www.blessyouboys.com/2019/1/8/18171919/baseball-stats-for-beginners-batting-average-on-base-percentage-explained


CREATE VIEW overweight_batters AS
	SELECT p.playerID, p.nameFirst, p.nameLast, 
		p.birthYear, YEAR(p.debut_date) AS debut_year, 
		(p.weight * 0.453592) / pow(p.height * 0.0254, 2) AS imc,
		b.3B, b.HR, b.yearID
	  FROM people as p
	  RIGHT JOIN batting AS b
	  	USING(playerID)
	  WHERE b.3B > 0 or b.HR > 0
	  HAVING imc > 35
		ORDER BY imc;

SELECT * FROM overweight_batters;

-- Revisa qué vistas son actualizables
SELECT 
    table_name as tabla, 
    is_updatable as puede_actualizarse
FROM
    information_schema.views
WHERE
    table_schema = 'lahmansbaseballdb';


