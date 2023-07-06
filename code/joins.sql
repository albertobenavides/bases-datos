-- Producto cartesiano

DROP TABLE IF EXISTS pan;
DROP TABLE IF EXISTS queso;
DROP TABLE IF EXISTS carne;

CREATE TABLE pan(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(20)
);

INSERT INTO pan (nombre) VALUES
	('Blanco'), 
	('Integral'),
	('Centeno'),
	('Orégano parmesano');
	
SELECT * from pan;


CREATE TABLE queso(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(20)
);

INSERT INTO queso (nombre) VALUES
	('Chihuahua'), 
	('Oaxaca'),
	('Asadero'),
	('Panela'),
	('Suizo'),
	('Chedar');
	
SELECT * from queso;


CREATE TABLE carne(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(20)
);

INSERT INTO carne (nombre) VALUES
	('Jamón de cerdo'), 
	('Jamón de pavo'),
	('Peperoni'),
	('Pastrami'),
	('Salami');
	
SELECT * FROM pan, queso, carne;


-- Composición
DROP TABLE IF EXISTS izquierda;
DROP TABLE IF EXISTS derecha;

CREATE TABLE izquierda (
	id INT,
	nombre VARCHAR(6)
);

INSERT INTO izquierda (id, nombre) VALUES
	(1, 'uno'),
	(2, 'dos'),
	(3, 'tres'),
	(4, 'cuatro'),
	(5, 'cinco');
	
CREATE TABLE derecha (
	id INT,
	nombre VARCHAR(6)
);

INSERT INTO derecha (id, nombre) VALUES
	(1, 'uno'),
	(3, 'tres'),
	(5, 'cinco'),
	(7, 'siete');
	
SELECT * FROM izquierda
	JOIN derecha
	ON izquierda.id = derecha.id;

SELECT * FROM izquierda
	INNER JOIN derecha
	ON izquierda.id = derecha.id;
	
SELECT * FROM izquierda
	LEFT JOIN derecha
	ON izquierda.id = derecha.id;

SELECT * FROM izquierda
	RIGHT JOIN derecha
	ON izquierda.id = derecha.id;

SELECT * FROM izquierda
	LEFT JOIN derecha
	ON izquierda.id = derecha.id
	UNION
SELECT * FROM izquierda
	RIGHT JOIN derecha
	ON izquierda.id = derecha.id;

-- Equivalentes
SELECT * FROM izquierda, derecha
  WHERE izquierda.id = derecha.id;

SELECT * FROM izquierda 
  JOIN derecha
    ON izquierda.id = derecha.id;

SELECT * FROM izquierda 
  INNER JOIN derecha
    ON (izquierda.id = derecha.id);

SELECT * FROM izquierda 
  CROSS JOIN derecha
    USING (id);
    
-- Selección, renombramiento
SELECT i.nombre, d.nombre
  FROM izquierda AS i 
  JOIN derecha AS d
    ON i.id = d.id;
