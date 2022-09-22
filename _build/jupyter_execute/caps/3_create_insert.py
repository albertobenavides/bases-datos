#!/usr/bin/env python
# coding: utf-8

# # Crear base de datos
# 
# Referencias de este capítulo {cite}`debarros2018,mysql`.
# 
# Este curso está orientado a SQL. De entre la variedad de SGBD, se opta por [MySQL](https://www.mysql.com/) por ser gratuito, de libre uso y gran distribución. Otra opción que me interesa es SQLite, principalmente porque nunca he usado directamente, pero sus tipos de datos están limitados. Por eso, MySQL me parece una opción más didáctica.
# 
# Todas las instrucciones y consultas de SQL se pueden ejecutar en un SGBD previamente instalado. Pero, para fines prácticos, recomiendo utilizar la página https://sqliteonline.com/ que tiene listos para usarse ambientes de SQLite, MariaDB, PostgreSQL, MS SQL y Docker con integreciones de servidor de estas herramientas. Puedes usar el que más te guste, pues aunque cada lenguaje tiene sus peculiaridades, todos parten del lenguaje estructurado estándar que representa SQL. [MariaDB](https://mariadb.org/) es totalmente compatible con MySQL.
# 
# ## Instrucciones para bases de datos
# Las instrucciones en MySQL (o MariaDB) usan `;` al final.
# 
# ### Crear
# 
# ```mysql
# CREATE DATABASE ejemplo;
# ```
# 
# ### Mostrar
# 
# ```mysql
# SHOW DATABASES;
# ```
# 
# ### Usar
# 
# ```mysql
# USE ejemplo;
# ```

# ## Tipos de datos
# 
# En SQL, los **tipos de datos** son equivalentes a los dominios de los modelos e-r y relacional.
# 
# ¿Por qué es importante elegir un tipo de datos correcto?
# 
# |Tipo de dato | Descripción |
# | --- | --- |
# | `CHAR` | Contiene `1` caracter. |
# | `CHAR(n)` | Contiene `n` caracteres, rellenados con espacios. |
# | `VARCHAR(n)` | Contiene `n` caracteres de longitud variable. |
# | `TINYINT` | Entero con valor 0 o 1. Equivalentes: `BIT`, `BOOL`, `BOOLEAN`. |
# | `TINYINT(n)` | Enteros con longitud `n`. Por defecto, entre -128 y 127. `UNSIGNED` entre 0 y 255. |
# | `SMALLINT(n)` | Enteros con longitud `n`. Por defecto, entre -32768 y 32767. `UNSIGNED` entre 0 y 65535. |
# | `MEDIUMINT(n)` | Enteros con longitud `n`. Por defecto, entre -8388608 y 8388607. `UNSIGNED` entre 0 y 16777215. |
# | `INT(n)` | Enteros con longitud `n`. Por defecto, entre -2147483648 y 2147483647. `UNSIGNED` entre 0 y 4294967295. |
# | `INTEGER(n)` | Enteros con longitud `n`. Por defecto, entre -2147483648 y 2147483647. `UNSIGNED` entre 0 y 4294967295. |
# | `BIGINT(n)` | Enteros con longitud `n`. Por defecto, entre -9223372036854775808 a 9223372036854775807. `UNSIGNED` entre 0 y 18446744073709551615. |
# | `FLOAT(n, m)` | Reales con longitud `n` y `m` posiciones decimales. Separa 4 bytes. |
# | `DOUBLE(n, m)` | Reales con longitud `n` y `m` posiciones decimales. Separa 8 bytes. |
# | `FLOAT(n)` | Reales con presición 0 a 53. Si se elige precisión 0 a 24, se trata de un FLOAT`, si se elige de 25 a 53, se trata de un `DOUBLE`. |
# | `DECIMAL(n, m)` | Reales con longitud `n` y `m` posiciones decimales. Tienen longitud fija, como las monedas. Equivalentes: `DEC`, `NUMERIC`, `FIXED`. |
# | `DATE` | Fechas con formato `AAAA-MM-DD` entre `1000-01-01` y `9999-12-31`. Se puede usar cadenas de texto. |
# | `TIME` | Fechas con formato `HH:MM:SS` entre `00:00:00` y `23:59:59`. Se puede usar cadenas de texto. |
# | `DATETIME` | Fechas con formato `AAAA-MM-DD HH:MM:SS` entre `1000-01-01 00:00:00` y `9999-12-31 23:59:59`. Se puede usar cadenas de texto. |
# | `TIMESTAMP` | Fechas con formato `AAAA-MM-DD HH:MM:SS.000000` entre `1000-01-01 00:00:00.000000` y `9999-12-31 23:59:59.999999`. Se puede usar cadenas de texto. |
# | `YEAR(n)` | Años entre 1901 y 2155 para `n = 4`. Entre 0 y 99 para `n = 2`; al usar este formato, 0 a 69 corresponden de 2000 a 2069, 70 a 99 van de 1970 a 1999.|
# | `BLOB` | Siglas de _binary large object_ (o gran objeto binario en español). Equivalente a una cadena de texto binaria. Longitud de 65535 caracteres. Equivalente `TEXT` como cadena de texto no binaria.|
# | `TINYBLOB` | Cadena de texto binaria. Longitud de 255 caracteres. Equivalente `TINYTEXT` como cadena de texto no binaria.|
# | `MEDIUMBLOB` | Cadena de texto binaria. Longitud de 16777215 caracteres. Equivalente `MEDIUMTEXT` como cadena de texto no binaria.|
# | `LONGBLOB` | Cadena de texto binaria. Longitud de 4294967298 caracteres. Equivalente `LONGTEXT` como cadena de texto no binaria.|
# | `ENUM('valor1', 'valor2', ...)` | Lista de hasta 65535 valores. Cada uno asociado a un valor entero empezando en 0. `NULL` para valor `NULL`|
# | `ENUM('valor1', 'valor2', ...)` | Conjunto de hasta 64 valores. Valor vacío permitido. Las diferentes combinaciones de valores activados y desactivados se definen por números binarios.|

# ## Crear tabla
# ```mysql
# CREATE TABLE tabla1 ( # Crea la tabla tabla1
#     variable1 TIPODATO1, -- Aquí se crea la variable1 con un tipo de dato específico
#     variable2 TIPODATO2, /* No sé qué más decir, pero esto es otro comentario */
#     ...
# );
# ```
# 
# ### Valores nulos
# ```mysql
# CREATE TABLE tabla1 (
#     variable1 TIPODATO1 NULL, # Permite valores nulos
#     variable2 TIPODATO2 NOT NULL, # No permite valores nulos
#     ...
# );
# ```
# 
# ### Valores por defecto
# ```mysql
# CREATE TABLE tabla1 (
#     variable1 TIPODATO1 DEFAULT valor1, # variable1 toma por defecto valor1 si no se le pasan datos
#     ...
# );
# ```
# 

# ### Primary keys
# 

# 
# ### autoincrement

# ### Unique

# ### Check

# 
# ## Estándares de diseño de tablas
# 

# 
# ## INSERT
# 

# ## Tarea
# 
# ### Instrucciones
# 1. [2 punto] Elegir entre SQLite, MySQL (MariaDB), PostgreSQL o MS SQL para trabajar a partir de aquí. Justificar la decisión.
# 1. [6 puntos] Escribir las instrucciones para crear una base de datos a partir del modelo e-r o relacional. 
#     - Guarda estas instrucciones en un archivo de texto con una extensión adecuada al SGBD que elegiste. 
#     - Asegúrate de que tus instrucciones se puedan ejecutar desde https://sqliteonline.com/
# 1. [2 puntos] Detallar las modificaciones o cambios no contempladas en los modelos, que surgieron tras crear la base de datos y las tablas.
# 
# ### Ejemplo
# 
