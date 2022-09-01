# Preliminares

Este capítulo tiene los conceptos fundamentales de las bases de datos. Son generalidades, pero conviene tenerlos a mano. Referencias de este capítulo de {cite}`silberschatEA2006,beaulieu2020`.

## Base de datos
Las *bases de datos*, abreviadas DB por _database_ en inglés, son estructuras que contiene un conjunto de datos relacionados.

## Sistema gestor de bases de datos
- Abreviado DBMS (por _database management systems_ en inglés).
- Conjunto de aplicaciones y DB.

## Representaciones
Para ejemplificar, pensemos en un blog en el que `usuarios` puedan escribir `publicaciones` a las que se les pueda agregar `comentarios`. 

### Datos no estructurados

Esta descripción textual de datos se llama **no estructurada** porque carece de estructuras (o etiquedas) con que diferenciar los datos. Otro tipo de representaciones no estrucutradas son los **esquemas**, que permiten una vista más detallada del sistema de un blog. De esta manera, se puede definir que el blog permite a
- `usuarios`,
  - con `nombre de usuario`,
  - `correo`, y
  - `contraseña`;
- crear `publicaciones`,
  - con `título`, y
  - `contenido`;
- a las que pueden agregar `comentarios`
  - con un `mensaje`.
  
### Datos estructurados
Asímismo, cada nivel principal (`usuarios`, `publicaciones` y `comentarios`) puede trasladarse a tablas donde cada subnivel representa el encabezado de una columna. Se agregan ejemplos de `usuarios`, `publicaciones` y `comentarios` como filas o renglones de cada tabla. Este tipo de representación se llama **datos estructurados** en los que a cada columna le corresponde un dato específico. Aquí, como puede observarse en las tablas de `publicaciones` y `comentarios`, aparecen columnas que se relacionan con otras tablas, como la de `usuario`.

**Usuario**
| `Nombre de usuario` | `Correo` | `Contraseña` |
| -- | -- | -- |
| fulano | fulano@correo.com | 1234 |
| mengana | mengana@correo.com | asdf |

**Publicaciones**
| `Título` | `Contenido` | `Usuario` |
| -- | -- | -- |
| Base de datos | Una base de datos... | fulano |
| Modelo relacional | El Modelo relacional... | mengana |

**Comentarios**
| `Mensaje` | `Usuario` | `Publicación` |
| -- | -- | -- |
| Buena publicación... | fulano | Modelo relacional |
| No estoy de acuerdo con... | mengana | Base de datos |

Estas tablas suelen escribirse en archivos `CSV` (siglas en inglés de _comma separated values_, o valores separados por comas) . Por ejemplo, la tabla de `usuarios` quedaría

```csv
nombre_usuario,correo,contraseña
fulano,fulano@correo.com,1234
mengana,mengana@correo.com,asdf
```
  
### Datos semiestructurados
  
Si llamamos a cada primer nivel del esquema (`usuario`, `publicaciones`, `comentarios`) **entidad** y a cada característica (como el `nombre de usuario`, el `título` de la `publicación`) **atributo**, pasamos de un modelo no estructurado a uno **semiestructurado** en el que hay elementos opcionales (como los `comentarios` en las `publicaciones`). Un ejemplo de notación que usa este tipo de datos son los archivos `JSON` que utilizan llaves `{}` y pares `clave : valor` para almacenar esta información. Nuevamente, el `JSON` de `usuarios` sería

```json
{
  nombre_usuario : 'fulano',
  correo : 'fulano@correo.com',
  contraseña : 1234
},
{
  nombre_usuario : 'mengana',
  correo : 'mengana@correo.com',
  contraseña : asdf
}
```

Esta misma información puede representarse con un **grafo** en el que cada nodo sea una entidad y las relaciones entre ellos las aristas.


```{mermaid}
flowchart LR
    Usuario --- Publicación
    Usuario --- Comentario
    Publicación --- Comentario
```

## Tipos de datos
Tanto para los datos estructurados como los semiestructurados, la información de los atributos puede ser de diferentes tipos. Por ejemplo, el 