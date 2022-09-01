#!/usr/bin/env python
# coding: utf-8

# # Preliminares
# 
# Este capítulo tiene los conceptos fundamentales de las bases de datos. Son generalidades, pero conviene tenerlos a mano. 
# 
# Referencias de este capítulo {cite}`silberschatEA2006,beaulieu2020`.

# ## Base de datos
# Las **bases de datos**, abreviadas BD, son estructuras que contienen un conjunto de datos relacionados, como una libreta de direcciones.
# 
# :::{admonition} Ejemplo
# Libreta de direcciones
# ```
# Fulano 811 1234 5678
# Mengana 644 0987 65463
# ...
# ```
# :::

# ## Sistema gestor de bases de datos
# Los **sistemas gestores de bases de datos**, abreviados SGBD, son conjuntos de aplicaciones y BD.

# ## Representaciones de datos
# Para ejemplificar, pensemos en un blog en el que `usuarios` puedan escribir `publicaciones` a las que se les pueda agregar `comentarios`. 

# ### Datos no estructurados
# Esta descripción textual de datos se llama **no estructurada** porque carece de estructuras (o etiquedas) con que diferenciar los datos. Otro tipo de representaciones no estrucutradas son los **esquemas**, que permiten una vista más detallada del sistema de un blog. De esta manera, se puede definir que el blog permite a
# - `usuarios`,
#   - con `nombre de usuario`,
#   - `correo`, y
#   - `contraseña`;
# - crear `publicaciones`,
#   - con `título`, y
#   - `contenido`;
# - a las que pueden agregar `comentarios`
#   - con un `mensaje`.
#   
# ### Datos estructurados
# Asímismo, cada nivel principal (`usuarios`, `publicaciones` y `comentarios`) puede trasladarse a tablas donde cada subnivel representa el encabezado de una columna. Se agregan ejemplos de `usuarios`, `publicaciones` y `comentarios` como filas o renglones de cada tabla. Este tipo de representación se llama **datos estructurados** en los que a cada columna le corresponde un dato específico. Aquí, como puede observarse en las tablas de `publicaciones` y `comentarios`, aparecen columnas que se relacionan con otras tablas, como la de `usuario`.
# 
# **Usuario**
# | `Nombre de usuario` | `Correo` | `Contraseña` |
# | -- | -- | -- |
# | fulano | fulano@correo.com | 1234 |
# | mengana | mengana@correo.com | asdf |
# 
# **Publicaciones**
# | `Título` | `Contenido` | `Usuario` |
# | -- | -- | -- |
# | Base de datos | Una base de datos... | fulano |
# | Modelo relacional | El Modelo relacional... | mengana |
# 
# **Comentarios**
# | `Mensaje` | `Usuario` | `Publicación` |
# | -- | -- | -- |
# | Buena publicación... | fulano | Modelo relacional |
# | No estoy de acuerdo con... | mengana | Base de datos |
# 
# Estas tablas suelen escribirse en archivos `CSV` (siglas en inglés de _comma separated values_, o valores separados por comas) . Por ejemplo, la tabla de `usuarios` quedaría
# 
# ```csv
# nombre_usuario,correo,contraseña
# fulano,fulano@correo.com,1234
# mengana,mengana@correo.com,asdf
# ```
#   
# ### Datos semiestructurados
#   
# Si llamamos a cada primer nivel del esquema (`usuario`, `publicaciones`, `comentarios`) **entidad** y a cada característica (como el `nombre de usuario`, el `título` de la `publicación`) **atributo**, pasamos de un modelo no estructurado a uno **semiestructurado** en el que hay elementos opcionales (como los `comentarios` en las `publicaciones`). Un ejemplo de notación que usa este tipo de datos son los archivos `JSON` que utilizan llaves `{}` y pares `clave : valor` para almacenar esta información. Nuevamente, el `JSON` de `usuarios` sería
# 
# ```json
# {
#   nombre_usuario : 'fulano',
#   correo : 'fulano@correo.com',
#   contraseña : 1234
# },
# {
#   nombre_usuario : 'mengana',
#   correo : 'mengana@correo.com',
#   contraseña : asdf
# }
# ```
# 
# Esta misma información puede representarse con un **grafo** en el que cada nodo sea una entidad y las relaciones entre ellos las aristas.
# 
# <center>
# 
# ```{mermaid}
# flowchart LR
#     Usuario --- Publicación
#     Usuario --- Comentario
#     Publicación --- Comentario
# ```
# 
# </center>

# ## SQL
# **SQL** son las siglas de _Structured Query Language_ o lenguaje de consultas estructuradas. Así, una consulta a Alexa u OK Google del tipo "Cuál es el teléfono de Fulano" se traduciría en la siguiente estructura SQL
# ```sql
# SELECT teléfono FROM contactos WHERE nombre = 'Fulano';
# ```

# ## Tipos de datos
# Tanto para los datos estructurados como los semiestructurados, la información de los atributos puede ser de diferentes tipos. En el caso del blog, el `nombre de usuario`, `correo`, `mensaje`, etc. son datos **textuales**, mas las BD pueden guardar otros tipos de datos, como **enteros**, **decimales**, **fecha**, **hora**, hasta datos multimedia tales como **documentos**, **imágenes**. Incluso es posible almacenar **estructuras de datos** como listas, conjuntos, entre otros.

# ## Tarea
# 
# :::{admonition} Instrucciones
# 1. Crear un repositorio público de Github
# 1. Compartir el repositorio en el Teams correspondiente
# 1. Describir una base de datos y sus relaciones de manera no estructurada (puede ser un párrafo, lista, esquema...) con la que trabajar durante el semestre. Agrega el tipo de dato que supones tendrá cada uno de tus atributos. Subir esta descripción en un archivo `markdown` o `PDF` nombrado claramente (tarea 1 o algo por el estilo).
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
