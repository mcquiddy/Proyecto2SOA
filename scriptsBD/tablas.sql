CREATE DATABASE ORDENES
GO

USE ORDENES
GO

CREATE TABLE CLIENTE(
	idCliente int NOT NULL,
	nombre nchar(20) NOT NULL,
	clave nchar(20) NOT NULL,
	PRIMARY KEY (idCliente)
);

CREATE TABLE ORDEN(
	idOrden int NOT NULL,
	idCliente int,
	idRestaurante nchar(50),
	fecha date,
	PRIMARY KEY (idOrden),
	FOREIGN KEY (idCliente) REFERENCES CLIENTE(idCliente)
);

CREATE TABLE ORDEN_PRODUCTO(
	idOP int NOT NULL,
	idOrden int,
	idProducto nchar(50),
	PRIMARY KEY (idOP),
	FOREIGN KEY (idOrden) REFERENCES ORDEN(idOrden)
);