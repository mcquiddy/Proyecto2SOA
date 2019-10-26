from flask import Flask
from flask import request
import pypyodbc  
from flask_graphql import GraphQLView

app = Flask(__name__)

# creating connection Object which will contain SQL Server Connection  
connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-OV13LMGE;Database=ORDENES;uid=service;pwd=pin1234')

# Creating Cursor  

cursor = connection.cursor()  


@app.route("/")
def home():
    return "HOLA MUNDO PYTHON CON SQL"

#get all sales by year   
@app.route("/YearSold/")
def YearSold():

    restaurante = request.args.get('rest', default = 'Burger King', type = str)
    ano = request.args.get('ano', default = 2019, type = int)
    cursor.execute("EXEC dbo.AnoVentas @Rid = '" + restaurante + "'" + ", @Ano = "+ str(ano) + ";") 
    for row in cursor: 
        print(str(row)) 
     
    return "REPORTE AÑO VENTAS"

#get all sales by month
@app.route("/MonthSold/")
def MonthSold():

    restaurante = request.args.get('rest', default = 'Burger King', type = str)
    mes = request.args.get('mes', default = 2, type = int)
    cursor.execute("EXEC dbo.MesVentas @Rid = '" + restaurante + "'" + ", @Mes = "+ str(mes) + ";") 
    for row in cursor: 
        print(str(row)) 
     
    return "REPORTE MES VENTAS"

#get all sales by day 
@app.route("/DaySold/")
def DaySold():

    restaurante = request.args.get('rest', default = 'Burger King', type = str)
    dia = request.args.get('dia', default = 2, type = int)
    cursor.execute("EXEC dbo.DiaVentas @Rid = '" + restaurante + "'" + ", @Dia = " + str(dia) + ";") 
    for row in cursor: 
        print(str(row)) 
     
    return "REPORTE DIA VENTAS"

#get all best client between 2 dates
@app.route("/BestClient/")
def BestClient():

    fecha1 = request.args.get('date1', default = '2010-02-13', type = str)
    fecha2 = request.args.get('date2', default = '2019-06-05', type = str)
    cursor.execute("EXEC dbo.MejorCliente @date1 = '" + fecha1 + "'" + ", @date2 = '" + fecha2 + "';") 
    for row in cursor: 
        print(str(row)) 
     
    return "REPORTE POR FECHAS"

if __name__ == "__main__":
    app.run(debug=True)