<?php

$url = "localhost";
$usuario = "root";
$clave = "";
$base_datos = "prueba";

// CREAR CONEXIÓN
$conn = new mysqli($url, $usuario, $clave);
// REVISAR CONEXIÓN
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// CREAR BASE DE DATOS
$sql = "DROP DATABASE IF EXISTS $base_datos";
$conn->query($sql);

// CREAR BASE DE DATOS
$sql = "CREATE DATABASE $base_datos";
$conn->query($sql);

// CERRAR CONEXIÓN
$conn->close();


// CREAR CONEXIÓN A BASE DE DATOS
$conn = new mysqli($url, $usuario, $clave, $base_datos);
// REVISAR CONEXIÓN
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}


// CREAR TABLA
$consulta = "CREATE TABLE usuarios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    correo VARCHAR(50),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";
$conn->query($consulta);


// INSERTAR FILAS
$consulta = "INSERT INTO usuarios (nombre, apellido, correo) VALUES 
    ('Alberto', 'Benavides', 'alberto@correo.com'),
    ('Brenda', 'Cázares', 'brenda@correo.com')";
$conn->query($consulta);


// SELECCIONAR
$consulta = "SELECT id, nombre, creado_en FROM usuarios";

$resultado = $conn->query($consulta);

if ($resultado->num_rows > 0) {
    echo "
    <table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>F. Creación</th>
        </tr>
    </thead>
    <tbody>
    ";

    while ($row = $resultado->fetch_assoc()) {
        echo "<tr>";
        $id = $row['id'];
        $nombre = $row['nombre'];
        $creado = $row['creado_en'];
        echo "<td>$id</td> <td>$nombre</td>  <td>$creado</td>";
        echo "<tr>";
    }
    echo "
    </tbody>
    </table>
    ";
} else {
    echo "0 results";
}

$conn->close();