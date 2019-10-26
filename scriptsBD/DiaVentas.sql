USE ORDENES;  
GO 

CREATE PROCEDURE DiaVentas @Rid nchar(50), @Dia int
AS
SELECT ORDEN.idOrden,idCliente,idRestaurante,fecha,idProducto
FROM (ORDEN JOIN ORDEN_PRODUCTO ON ORDEN.idOrden=ORDEN_PRODUCTO.idOrden)
WHERE (DAY(fecha) = @Dia) AND (idRestaurante = @Rid);