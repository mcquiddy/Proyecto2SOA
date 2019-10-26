USE ORDENES;  
GO  

CREATE PROCEDURE AnoVentas @Rid nchar(50), @Ano int
AS
SELECT ORDEN.idOrden,idCliente,idRestaurante,fecha,idProducto
FROM (ORDEN JOIN ORDEN_PRODUCTO ON ORDEN.idOrden=ORDEN_PRODUCTO.idOrden)
WHERE (YEAR(fecha) = @Ano) AND (idRestaurante = @Rid);