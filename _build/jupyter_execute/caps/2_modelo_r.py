#!/usr/bin/env python
# coding: utf-8

# # Modelo relacional

# Referencias de este capítulo {cite}`silberschatEA2006,conclase2004`.

# Otro de los modelos para bases de datos es el **modelo relacional** que usa tablas, llamadas **relaciones**. Estas relaciones almacenan registros en forma de filas, llamados **tuplas**, cuya combinación de **atributos** (dados por columnas y sus encabezados) son únicos. Es posible que los valores de los atributos de una tupla estén vacíos, lo que se representa con la palabra clave `NULL`. Análogamente al modelo e-r, se considera que cada tabla del modelo relacional corresponde a un conjunto de entidades, cada fila a una entidad y cada encabezado de la tabla sería un atributo. 
# 
# A partir de ahora, se usarán nombres de variables para denotar encabezados, relaciones, etc. Es decir, en lugar de escribir `fecha de nacimiento`, se usara `fecha_nacimiento`, `nacimiento`, `birthday` o equivalentes que no usen espacios o caracteres especiales (como la ñ). En la {numref}`rel:ejemplo` aparece un ejemplo de un modelo relacional para una libreta de direcciones.
# 
# ```{table} Ejemplo de tabla de modelo relacional.
# :name: rel:ejemplo
# 
# | `name`    | `lastname`    | `phone`   | `mail`    | `birthday`|
# |---        |---            |---        |---        |---        |
# | Fulano | de Tal | 8111111111 | fulano@correo.com | 1987-01-01 |
# | ... | ... | ... | ... | ... |
# | Mengana | de Cual | 8123456789 | mengana@correo.com | 1988-12-31 |
# ```

# ## Dominios
# 
# Para cada tabla del modelo relacional, existen atributos que tienen asociados **dominios**. Cada uno de estos dominios supone un conjunto de valores posibles, denotados por $D$, que pueden tomar sus posibles valores $v$. 
# 
# Siguiendo esta lógica, si una tienda de _sandwiches_ ofrece "armar tu propio _sandwich_' con diferentes tipos de pan, carne y queso, su traducción al modelo relacional partiría de la relación `sandwich` con atributos `pan`, `carne` y `queso` y sus correspondientes dominios $D_{\texttt{pan}}$, $D_{\texttt{carne}}$, $D_{\texttt{queso}}$, de donde se pueden formar $v$ sandwiches incluidos en el subconjunto de la combinación de esos dominios, denotada **producto cartesiano**, tal que
# 
# $$
# D_\texttt{pan} \times D_{\texttt{carne}} \times D_{\texttt{queso}}.
# $$

# ## Claves
# Para diferenciar tuplas, es necesario que en las relaciones haya atributos que las identifican de manera inequívoca. A estos atributos se les llama **claves**. Existen diferentes tipos de claves en el modelo relacional, pero las más importantes son
# - Primaria: Uno o más atributos usados para identificar las tuplas, motivo por el cual no pueden ser `NULL`.
# - Foránea: Atributo que almacena la clave primaria de una relación (puede ser consigo misma).

# ## Interrelaciones
# Para evitar confusiones, se llaman **interrelaciones** a las relaciones de tablas (llamadas formalmente **relaciones**) en el modelo relacional. Similar al modelo e-r, se pueden interrelacionar relaciones de modo **uno a uno**, **uno a muchos** y **muchos a muchos**.

# ## Representación
# En el modelo relacional se pueden representar las bases de datos como **esquemas**, tal como el que aparece a continuación.
# <pre>
# Relación1(<u>clave_primaria1</u> atributo1, atributo2, ..., clave_foránea_relación3)
# Relación2(<u>clave_primaria2</u>, atributo3, ..., clave_foránea_relación1)
# Relación3(<u>clave_primaria3</u>, atributo4, ..., clave_foránea_relación1)
# Relación1_relación2(<u>clave_foránea_relación1</u>, <u>clave_foránea_relación1</u>, atributo5, ...)
# </pre>
# 
# Nótese que
# 1. las relaciones se escriben con mayúscula inicial,
# 1. seguidas por un paréntesis con todos sus atributos,
# 1. las claves primarias van subrayadas, 
# 1. las claves foráneas se escriben, generalmente, al final,
# 1. las interrelaciones 
#     - llevan la unión de nombres de las relaciones que las forman, mediante un guión bajo,
#     - se escriben con mayúscula inicial,
# 1. se establecen por las claves foráneas de las relaciones. O sea,
#     - la `relación1` con la `relación2` forman una interrelación **uno a muchos**; 
#     - la `relación1` con la `relación3` de **uno a uno**; 
#     - y la `relación1` con la `relación4` de **muchos a muchos**. 
#     
# Esto mismo puede representarse gráficamente como se muestra en la {numref}`fig:rel:diagrama`. Prestar atención a los símbolos para denotar la cardinalidad de las interrelaciones.
# % https://mermaid.live/edit#pako:eNqFkk1OwzAQha9izbpdNEk32VXQBRICCXaVpWqIBxg1tqOpg1QlORVH4GLUhUQEQruc5-fvaX4aKLwhyIHkmvFF0Gqn1MP6dnV1c3-3UG07n3d-EBKVKw3sAolQiQV_vDsN4y9NLJUy3rJjr4oS32hbCVsUxsX4EYPwUx38P3IS5e4nPjmPT6Y56R_OV2dtOwjpxc7S89HpdHQ2Ee2b0VCzi9HZ7-ievjzRYQaWxCKb4yJPTg3hlSxpiGSDsou86Ksrg4HWhoMXyJ-x3NMM8Eh6PLgC8iA19abvexhcFbqN933dfQL2OL0V
# ````{div} full-width
# ```{figure} ../imgs/rel_diagrama.svg
# :name: fig:rel:diagrama
# 
# Representación gráfica de un modelo relacional.
# ```
# ````

# ## Álgebra relacional
# 
# El **álgebra relacional** es un lenguaje por el que se consultan o manipulan las relaciones en el modelo relacional. Al tratarse de un lenguaje algebraico, supone una serie de operadores. 
# 
# Para entender estos operadores, se partirá de un ejemplo obtenido de una base de datos de _soccer_ europeo compartida en [Kaggle](https://www.kaggle.com/code/dimarudov/data-analysis-using-sql/data). Hay muchos ejemplos de bases de datos que se pueden usar, como [éste](https://github.com/kite1988/nus-sms-corpus), [este otro](https://www.kaggle.com/datasets/kaggle/meta-kaggle), o los presentes [aquí](https://www.sqlskills.com/sql-server-resources/sql-server-demos/). 
# 
# En fin, de la base de datos de _soccer_ nos quedaremos con las siguientes relaciones:
# <pre>
# Country (<u>id</u>, name)
# League (<u>id</u>, name, country_id)
# Team (<u>id</u>, team_long_name, team_short_name)
# Player (<u>id</u>, player_name, birthday, height, weight)
# Match (<u>id</u>, home_team_goal, away_team_goal, country_id, league_id, home_team_id, away_team_id)
# </pre>
# 
# Hay un par de maneras de representar estas manipulaciones definidas por el álgebra relacional. Se presenta primero una matemática y luego otra computacional a partir de ejemplos.

# ### Proyección
# Devuelve tuplas de los atributos especificados de una relación. Si hay tuplas repetidas, sólo se conserva la primera aparición.
# 
# $$
# \Pi_{\texttt{atributo1, atributo2, \ldots}}(\texttt{relación})
# $$
# 
# ```
# relación[atributo1, atributo2, ...]
# ```
# 
# ````{admonition} Ejercicio
# Qué hace esta proyección.
# 
# $$
# \sigma_{\texttt{player_name, birthday}}(\texttt{Player})
# $$
# 
# ```
# Player[player_name, birthday]
# ```
# ````

# ### Selección
# 
# Selecciona tuplas que cumplan con una condición.
# 
# `````{margin}
# ````{note}
# Para ver las columnas en SQLite se usa
# ```
# PRAGMA table_info(Relación)
# ```
# ````
# `````
# 
# $$
# \sigma_{\texttt{atributo * valor}}(\texttt{relación})
# $$
# 
# ```
# relación[atributo * valor]
# ```
# Donde `*` es un operador lógico ($=, \neq, <, >, \leq, \geq$) con proposiones que pueden relacionarse con los operadores lógicos $\land$, $\lor$, $\neg$.
# 
# ````{admonition} Ejercicio
# ¿Qué hace esta selección?
# 
# $$
# \sigma_{(\texttt{home_team_goal} > 4) \lor (\texttt{away_team_goal} > 4)}(\texttt{Match})
# $$
# 
# ```
# Match[(home_team_goal > 4) | (away_team_goal > 4)]
# ```
# ````

# ### Producto cartesiano
# 
# El **producto cartesiano** es la combinación de todas las tuplas de un par de relaciones.
# 
# $$
# \texttt{relación1} \times \texttt{relación2}
# $$
# 
# ```
# relación1 × relación2
# ```
# 
# ````{admonition} Ejercicio
# ¿Qué hace este producto cartesiano?
# 
# $$
# \texttt{Team} \times \texttt{Team}
# $$
# 
# ```
# Team × Team
# ```
# ````

# ### Composición
# Una **composición** consiste en utilizar resultados de operaciones de álgebra relacional para crear expresiones más complejas. Por ejemplo,
# 
# $$
# \Pi_{\texttt{atributo1, atributo2}, \ldots}(\sigma_{\texttt{atributo * valor}}(\texttt{relación})).
# $$
# 
# De entre las composiciones más utilizadas, hay un tipo en el que se crea una relación a partir de dos relaciones en las que se igualan atributos de una con los de otra. A esto se le llama _join_ (que suele ser traducido como composición, justamente). Esta composición depende del producto cartesiano de las relaciones involucradas.
# 
# $$
# \sigma_{\texttt{relación1.atributo1} = \texttt{relación2.atributo2}}(\texttt{relación1} \times \texttt{relación2})
# $$
# 
# ```
# relación1[relación1.atributo1 = relación2.atributo2]relación2
# ```

# ### Unión
# 
# Suma las tuplas de dos relaciones con el mismo número de atributos y dominios asociados.
# 
# $$
# \texttt{relación1} \cup \texttt{relación2}
# $$
# 
# ```
# relación1 × relación2
# ```
# 
# ````{admonition} Ejercicio
# ¿Qué hace este producto cartesiano?
# 
# $$
# \texttt{Team} \times \texttt{Team}
# $$
# 
# ```
# Team × Team
# ```
# ````

# ## Tarea
# 
# ### Instrucciones
# 1. [8 puntos] Crea un diagrama relacional de tu base de datos a partir del modelo e-r de la tarea anterior.
# 
# Puntos extra
# - 
# 
# ### Ejemplo
# 
