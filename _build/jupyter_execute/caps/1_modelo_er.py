#!/usr/bin/env python
# coding: utf-8

# # Modelo entidad-relación
# 
# Referencias de este capítulo {cite}`silberschatEA2006,conclase2004`.
# 
# El modelo entidad-relación, también llamado modelo e-r, representa uno de los modelos de representación de bases de datos. Entre otros se halla el orientado a objetos o el relacional, que se verá en el siguiente capítulo.

# ## Conceptos fundamentales
# En el modelo e-r, se epresentan objetos únicos como **entidades** agrupadas en **conjuntos de entidades** que comparten las mismas característiticas generales, llamadas **atributos**. Los atributos no cambian con el tiempo, de modo que la edad no es un atributo, pero sí la fecha de nacimiento. Adicionalmente, los **atributos** tienen **dominios** que limitan los posibles valores que pueden tomar.
# 
# Las interacciones entre **conjuntos de entidades** se plasman con **relaciones**. El **grado** de las relaciones se mide por el número de **conjuntos de entidades** que intervienen en una misma relación. Una relación de grado 2 se llama **binaria**; una de grado 3, **ternaria**, etc.
# 
# Hasta aquí, podemos establecer un ejemplo con una familia formada por padre, madre, hijo e hija. Cada integrante es una entidad. Todos los integrantes forman un conjunto de entidades que podríamos llamar `persona`. Podría interesarnos de estas personas conocer el `nombre`, `apellido parterno`, `apellido materno`, su `fecha de nacimiento`. Se puede establecer una relación ternaria entre padre, madre y cada hijo, del tipo padre y madre `procrearon` a cada hijo.

# ## Cardinalidad
# Pese a que las relaciones pueden tener grado superior a 2, lo más común es encontrarse relaciones binarias entre conjuntos de entidades. Para estas relaciones binarias, se pueden establecer conjuntos de entidades llamadas **cardinalidades**. Las cardinalidades de las relaciones pueden ser **uno a uno**, **uno a mucho**, **muchos a uno** y **muchos a muchos**. 
# 
# Esto se puede representar en grafos y conjuntos entre entidades A y B a partir de relaciones binarias como arcos, como se ve en las figuras {numref}`%s<fig:cardinalidad:uno_uno>`, {numref}`%s<fig:cardinalidad:uno_muchos>`, {numref}`%s<fig:cardinalidad:muchos_uno>` y {numref}`%s<fig:cardinalidad:muchos_muchos>`.

# :::::{div} full-width
# ::::{grid}
# 
# :::{grid-item}
# ```{figure} ../imgs/card_uno_uno.svg
# :name: fig:cardinalidad:uno_uno
# 
# Uno a uno.
# ```
# :::
# 
# :::{grid-item}
# ```{figure} ../imgs/card_uno_muchos.svg
# :name: fig:cardinalidad:uno_muchos
# 
# Uno a muchos.
# ```
# :::
# 
# :::{grid-item}
# ```{figure} ../imgs/card_muchos_uno.svg
# :name: fig:cardinalidad:muchos_uno
# 
# Muchos a uno.
# ```
# :::
# 
# :::{grid-item}
# ```{figure} ../imgs/card_muchos_muchos.svg
# :name: fig:cardinalidad:muchos_muchos
# 
# Muchos a muchos.
# ```
# :::
# 
# ::::
# :::::

# ## Claves
# Las **claves** son atributos necesarios para diferencias inequívocamente las entidades. Puedes pensarlo como las huellas digitales que permitirían diferenciar incluso a personas con el mismo nombre y apariencia física (como el caso de [Will y William West](https://rarehistoricalphotos.com/will-william-west-case-fingerprints/)).
# 
# En este contexto, las **claves mínimas** son aquellos atributos que podrían utilizarse como claves y que dejarían de serlo si se modifican en alguna forma. Para un mayor de edad en México, serían sus huellas digitales y su [INE](https://www.ine.mx/credencial/), por ejemplo.
# 
# Cuando hay varios atrituvos que cumplen con los requisitos, se llama **claves candidatas**. Elegir una de estas claves para representar a un modelo la convierte en **clave principal o primaria**.
# 
# Por último, cuando se quieren establecer claves para relaciones de muchos a muchos, se suelen utilizar **claves múltiples o interrelacionadas**.

# ## Diagrama entidad-relación
# 

# 
# 
# ### Símbolos usados en la notación E-R
# 
# ### Conjunto de entidades débiles
# 
# ### Características del modelo E-R extendido
# 
# ### Especialización
# 
# ### Generalización
# 
# ### Herencia de atributos
# 
# ### Jerarquía y herencia múltiple
# 
# ### Restricciones sobre las generalizaciones
# 
# ### Agregación
# 
# ### Relaciones redundantes
# 
# ### Diseño de un esquema de base de datos E-R

# ## Tarea
# 
# ### Instrucciones
# 1. Convierte tu base de datos no estructurada en un modelo entidad-relación
# 1. Convierte tu base de datos no estructurada en un modelo relacional
# 
# Puntos extra
# - Describir relaciones entre modelos
# - Especificar cálculos entre atributos
# :::
# 
# ### Ejemplo
# Un cliente requiere una página web donde llevar un control de partidos de Lacrosse en un torneo. Los partidos se juegan en una en una fecha determinada entre dos equipos. Se requiere conocer el marcador global del partido. Para esto, es necesario registrar los equipos que participarán en el torneo con un nombre, su logo y color. Hay que saber cuáles son los jugadores de cada equipo con su nombre y número de camiseta. Además, al cliente le interesa conocer cuál es el jugador con más tantos anotados por partido y de manera global. Igualmente, saber qué jugador hizo la mayor cantidad de intercepciones por partido y de manera global. Por otro lado interesa saber cuáles son los tantos e intercepciones por jugador y partido.
# 
# - Equipo:
#     - nombre (texto),
#     - logo (imagen),
#     - color (texto).
# - Jugador:
#     - nombre (texto),
#     - número (entero),
#     - Equipo.
# - Partido:
#     - Equipo visitante,
#     - Equipo local,
#     - fecha (fecha y hora),
#     - resultado (texto).
# - Gol:
#     - Partido,
#     - Jugador,
#     - tiempo (hora).
# - Salvada:
#     - Partido,
#     - Jugador,
#     - tiempo (hora).
