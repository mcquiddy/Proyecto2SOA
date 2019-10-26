USE ORDENES;  
GO 

CREATE PROCEDURE MesVentas @Rid nchar(50), @Mes int
AS
SELECT ORDEN.idOrden,idCliente,idRestaurante,fecha,idProducto
FROM (ORDEN JOIN ORDEN_PRODUCTO ON ORDEN.idOrden=ORDEN_PRODUCTO.idOrden)
WHERE (MONTH(fecha) = @Mes) AND (idRestaurante = @Rid);