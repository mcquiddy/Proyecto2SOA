USE ORDENES;  
GO 

CREATE PROCEDURE MejorCliente @date1 date, @date2 date
AS
SELECT O1.idOrden,O1.idCliente,idRestaurante,fecha,idProducto
FROM ORDEN AS O1, ORDEN_PRODUCTO AS OP1,
	(SELECT TOP 5 O2.idCliente,COUNT(O2.idCliente) AS Count_cliente
		FROM ORDEN AS O2,ORDEN_PRODUCTO AS OP2
		WHERE O2.idOrden=OP2.idOrden
		GROUP BY O2.idCliente
		ORDER BY Count_cliente DESC) AS CLIENTES
WHERE O1.idOrden=OP1.idOrden AND O1.idCliente=CLIENTES.idCliente AND (O1.fecha>=@date1 AND O1.fecha<=@date2)
ORDER BY CLIENTES.Count_cliente DESC;