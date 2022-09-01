#!/usr/bin/env python
# coding: utf-8

# # Modelos de datos
# 
# 
# 
# Referencias de este capítulo {cite}`silberschatEA2006,beaulieu2020`.

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
