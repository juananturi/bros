DROP DATABASE IF EXISTS pedidos_entregas_db;
CREATE DATABASE pedidos_entregas_db;

USE pedidos_entregas_db;

-- Crear la tabla 'categoria'
CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(255) NOT NULL
);

-- Crear la tabla 'marca'
CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla 'producto' relacionado con 'marca' y 'categoria'
CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    id_marca INT,
    id_categoria INT,
    cantidad_disponible INT,
    habilitado BOOLEAN,
    cantidad_ventas INT,
    iva DECIMAL(10, 2),
    precio DECIMAL(10, 2),
    FOREIGN KEY (id_marca) REFERENCES marca(id),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);
-- Crear la tabla 'rol'
CREATE TABLE rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL

);
-- Crear la tabla 'usuario'
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_rol INT ,
    usuario VARCHAR(50) NOT NULL,
    contraseña VARCHAR(50) NOT NULL,
    fecha_registro DATE NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES rol(id)
);

-- Crear la tabla 'departamento' 
CREATE TABLE departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear la tabla 'municipio' municipio asociado con departamento  
CREATE TABLE municipio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);


-- Crear la tabla 'tipo_empleado'
CREATE TABLE tipo_empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    codigo VARCHAR(50) NOT NULL
);


-- Crear la tabla 'empleado'
CREATE TABLE empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    cedula VARCHAR(50) NOT NULL,
    direccion VARCHAR(255),
    departamento INT,
    municipio INT,
    barrio VARCHAR(255),
    tipo_empleado INT,
    salario DECIMAL(10, 2),
    FOREIGN KEY (departamento) REFERENCES departamento(id),
    FOREIGN KEY (municipio) REFERENCES municipio(id),
    FOREIGN KEY (tipo_empleado) REFERENCES tipo_empleado(id)
);

-- Crear la tabla 'cliente' 
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    codigo VARCHAR(50) NOT NULL,
    departamento INT,
    municipio INT,
    FOREIGN KEY (municipio) REFERENCES municipio(id),
    FOREIGN KEY (departamento) REFERENCES departamento(id)
);
-- Crear la tabla 'pedido'
CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numeroOrden VARCHAR(50) NOT NULL,
    fechaRegistro DATE NOT NULL,
    totalPrecio DECIMAL(10, 2) NOT NULL,
    totalIva DECIMAL(10, 2) NOT NULL,
    barrio VARCHAR(50),
    direccionEntrega VARCHAR(192),
    cliente INT ,
    empleado VARCHAR(55) NOT NULL,
    entregador VARCHAR(55) NOT NULL,
    observacion TEXT,
    departamento INT,
    municipio INT,
    FOREIGN KEY (departamento) REFERENCES departamento(id),
    FOREIGN KEY (municipio) REFERENCES municipio(id),
    FOREIGN KEY (cliente) REFERENCES cliente(id) 
);



-- Crear la tabla 'detalle_pedidos'
CREATE TABLE detalle_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedidoId INT NOT NULL,
    nombreProducto VARCHAR(55) NOT NULL,
    descripcionProducto TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    iva DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL,
    codigoProducto VARCHAR(55),
    marca VARCHAR(55),
    categoria VARCHAR(55),
    FOREIGN KEY (pedidoId) REFERENCES pedido(Id) -- Relación 1 a 1 con pedido
);

-- Crear la tabla para la relación muchos a muchos entre pedido y empleados
CREATE TABLE pedido_empleados (
    pedidoId INT NOT NULL,
    empleadoId INT NOT NULL,
    PRIMARY KEY (pedidoId, empleadoId),
    FOREIGN KEY (pedidoId) REFERENCES pedido(Id),
    FOREIGN KEY (empleadoId) REFERENCES empleado(Id) -- Asume que existe una tabla llamada empleados
);

-- Crear la tabla para la relación muchos a muchos entre pedido y empleados
CREATE TABLE detalle_producto (
    detalle_id INT NOT NULL,
    producto_id INT NOT NULL,
    PRIMARY KEY (detalle_id, producto_id),
    FOREIGN KEY (detalle_id) REFERENCES detalle_pedidos(Id),
    FOREIGN KEY (producto_id) REFERENCES producto(Id) -- Asume que existe una tabla llamada empleados
); 