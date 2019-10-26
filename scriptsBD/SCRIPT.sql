
USE ORDENES;  
GO  
EXEC dbo.AnoVentas @Rid = 'Burger King' , @Ano = 2019;  
GO 

USE ORDENES;  
GO  
EXEC dbo.MesVentas @Rid = 'Burger King' , @Mes = 02;  
GO  

USE ORDENES;  
GO  
EXEC dbo.DiaVentas @Rid = 'McDonald' , @Dia = 02;  
GO  


USE ORDENES;  
GO  
EXEC dbo.MejorCliente @date1 = '2010-02-13' , @date2 = '2017-06-05';  
GO 