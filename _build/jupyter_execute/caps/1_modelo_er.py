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
# Cuando hay varios atrituvos que cumplen con los requisitos, se llama **claves candidatas**. Elegir una de estas claves para representar a una entidad la convierte en **clave principal o primaria**.
# 
# Por último, cuando se quieren establecer claves para relaciones de muchos a muchos, se suelen utilizar **claves múltiples o interrelacionadas**.

# ## Fuerza de entidades
# Las entidades pueden ser clasificadas como **fuertes** o **débiles**. Las fuertes son aquellas que tienen su propia clave primaria, mientras que las débiles son aquellas que usan la clave privada de otra entidad al lado de otros atributos.

# ## Generalización
# Técnica usada cuando diferentes entidades tienen atributos en común, lo cual amerita reunirlas bajo el mismo conjunto de entidades. En un restaurante, por ejemplo, los cocineros, meseros, cajeros y lavalozas son agrupados bajo la entidad `empleados` por compartir los atributos `nombre`, `salario`, `hora entrada`, `hora salida`, `días de trabajo`.

# ## Especialización
# Se trata de generar entidades subordinadas a partir de otras que comparten característicias generales. En el restaurante se podrían subordinar de `empleados` las entidades entidades `cocinero`, `mesero`, `cajero`, `lava lozas`, cada uno con atritutos específicos, tal que el `cocinero` podría tener `especialidad`, el `mesero` un `área asignada`, etc.

# ## Diagrama entidad-relación
# Los modelos entidad-relación pueden representarse mediante diagramas que usan
# - **rectángulos** para **entidades**,
# - **elipses** para **atributos**,
# - **elipses subrayados** para **claves primarias**,
# - **rombos** para **relaciones,** 
# - **líneas** para unir **relaciones** y **entidades**,
# - **números** `1` para relaciones uno, y `N` para muchos,
# - **hexágonos** para **dominios**, 
# - **triángulos** para **generalizaciones** y **especializaciones**.
# 
# %flowchart TB
# %  d1{{Dominio1}} --- a1
# %  d2{{Dominio2}} --- a2
# %  d3{{Dominio3}} --- a3
# %  d4{{Dominio4}} --- a4
# %
# %  a1([Atributo1]) --- EntidadA
# %  a2([Atributo2]) --- EntidadA
# %
# %  EntidadA -- 1 --- r{Relación}
# %  EntidadB -- N --- r{Relación}
# %
# %  a3([Atributo3]) --- EntidadB
# %  a4([Atributo4]) --- EntidadB
# 
# Una representación meramente didáctica con estos elementos puede verse en la {numref}`fig:e-r:grafico`.
# 
# ```{figure} ../imgs/er_graf.svg
# :name: fig:e-r:grafico
# 
# Representación gráfica mínima de un modelo e-r.
# ```

# %## Agregación

# ## Tarea
# 
# ### Instrucciones
# 1. [8 puntos] Convierte tu base de datos no estructurada en un modelo entidad-relación, representándolo con un diagrama entidad-relación. Usa nodos con figuras correctas y aristas claramente señaladas con los números correspondientes para las relaciones.
# 1. [2 punto] Muestra el dominio de los atributos.
# 1. Subir esta descripción en un archivo `markdown` o `PDF` nombrado claramente (tarea 1 o algo por el estilo).
# 
# ### Ejemplo
# 
# Aquí se puede ver el diagrama e-r del ejemplo de lacrosse.
# 
# :::{div} full-width
# ```{figure} ../imgs/er_ejemplo.svg
# :name: fig:e-r:ejemplo
# 
# Modelo e-r de torneos de lacrosse.
# ```
# :::
# 
# %flowchart TB
# %  aT0([Id]) --- Torneo
# %  aT1([Nombre]) --- Torneo
# %  aT2([Inicio]) --- Torneo
# %  aT3([Fin]) --- Torneo
# %  aT4([Calle]) --- Torneo
# %  aT5([Número]) --- Torneo
# %  aT6([Colonia]) --- Torneo
# %  aT7([Municipio]) --- Torneo
# %  aT8([Estado]) --- Torneo
# %  aT9([País]) --- Torneo
# %
# %  Torneo --- rTP{Tiene}
# %  rTP{Tiene} --- Partido
# %
# %  aP1([Id Equipo visitante]) --- Partido
# %  aP2([Id Equipo local]) --- Partido
# %  aP3([Fecha y hora]) --- Partido
# %  aP4([Resultado]) --- Partido
# %  
# %  Partido --- r3{Tiene}
# %  r3{Tiene} --- Gol
# %
# %  aE0([Id]) --- Equipo
# %  aE1([Nombre]) --- Equipo
# %  aE2([Logo]) --- Equipo
# %  aE3([Color]) --- Equipo
# %
# %  Partido --- rPE{Recibe}
# %  rPE{Recibe} ---  Equipo
# %
# %  Partido --- rPE2{Visita}
# %  rPE2{Visita} ---  Equipo
# %
# %  aJ0([Id]) --- Jugador
# %  aJ1([Nombre]) --- Jugador
# %  aJ2([Número]) --- Jugador
# %  aJ3([Id Equipo]) --- Jugador
# %
# %  Equipo --- rEJ{Juega}
# %  rEJ{Juega} --- Jugador
# %
# %  aG1([Id Jugador]) --- Gol
# %  aG2([Id Partido]) --- Gol
# %
# %  aG3([Tiempo]) --- rJG
# %  Jugador --- rJG{Mete}
# %  rJG{Mete} --- Gol
# %
# %  Jugador --- rJG2{Ataja}
# %  rJG2{Ataja} --- Gol
# %
# %  aG4([Tiempo]) --- rJG2
