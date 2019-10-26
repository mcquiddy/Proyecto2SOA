
# generate random integer values
from random import seed
from random import randint

# seed random number generator
seed(1)
f = open("OrdenesGrafo.txt", "w+")
d = open("OrdenesRelProductsGrafo.txt", "w+")
s = open("OrdenesRelRestaurantesGrafo.txt", "w+")
oSql = open("OrdenesSQL.txt", "w+")
opSql = open("OrdenesRelProductsSQL.txt", "w+")

i=1
n=0
p=1
end=150

oSql.write("INSERT INTO ORDEN (idOrden, idCliente,idRestaurante,fecha) VALUES")
oSql.write("\n")

opSql.write("INSERT INTO ORDEN_PRODUCTO(idOP, idOrden,idProducto) VALUES")
opSql.write("\n")

f.write("CREATE")
f.write("\n")
restaurantes=["KFC","McDonald","Subway","Taco Bell","Pizza Hut","Comida China",
              "Burger King","Cuchara de Aurora","Comedor Institucional","Restaurante el Lago"]

productos=[["Chifrijo","Casado Pollo","Casado Carne"],["Sopa","Papas","Cocacola"],
           ["Chifrijo","Sopa","Papas","Cocacola"],["Pizza Suprema","Pizza Peperoni"],
           ["Helado"],["Sopa","Papas","Cocacola"],["Chifrijo","Casado Pollo","Casado Carne"],
           ["Sopa","Papas","Cocacola"],
           ["Taco Suprema","Casado Pollo","Casado Pescado","Sopa","Papas","Cocacola",
            "Pizza Suprema","Limonada","Muslo de Pollo"],
           ["Helado","Papas","Pechuga de Pollo","Sopa","Papas","Cantones"]]


while(i < end):
    ano=str(2019)
    mes=str(randint(1, 12))
    dia=str(randint(1, 28))
    id=str(randint(1, 3))
    f.write("(orden"+str(i)+":Orden{"+"nombre:\""+"Orden "+str(i)+"\""+",idCliente:\""+id+
            "\""+",fecha:\""+ano+"-"+mes+"-"+dia+"\"}),")
    f.write("\n")

    

    restNumber=randint(0, 9)
    prodNumber=randint(0, len(productos[restNumber]))
    n=0
    data=""
    while(n < prodNumber):
        data=data+"d.nombre =\""
        produSelect=randint(0, len(productos[restNumber])-1)
        data=data+str(productos[restNumber][produSelect])
        data=data+"\" OR "

        opSql.write("("+str(p)+","+str(i)+",'"+str(productos[restNumber][produSelect])+"'),")
        opSql.write("\n")
        p=p+1
        n=n+1
        
    data=data+"d.nombre =\""
    produSelect=randint(0, len(productos[restNumber])-1)
    data=data+str(productos[restNumber][produSelect])
    data=data+"\""

    opSql.write("("+str(p)+","+str(i)+",'"+str(productos[restNumber][produSelect])+"'),")
    opSql.write("\n")
    p=p+1
    
    d.write("MATCH (n:Orden),(d:Producto)")
    d.write("\n")
    d.write("WHERE n.nombre = \"Orden "+str(i)+"\" AND ("+data+")")
    d.write("\n")
    d.write("CREATE")
    d.write("\n")
    d.write("(n)-[r:PRODUCTO]->(d)")
    d.write("\n")
    d.write("RETURN r,n,d;")
    d.write("\n")
    d.write("\n")

    
    
    s.write("MATCH (n:Restaurante),(d:Orden)")
    s.write("\n")
    s.write("WHERE n.nombre = \""+restaurantes[restNumber]+"\" AND d.nombre =\"Orden "+str(i)+"\"")
    s.write("\n")
    s.write("CREATE")
    s.write("\n")
    s.write("(n)-[r:ORDEN]->(d)")
    s.write("\n")
    s.write("RETURN r,n,d;")
    s.write("\n")
    s.write("\n")

    oSql.write("("+str(i)+","+id+",'"+restaurantes[restNumber]+"','"+ano+"-"+mes+"-"+dia+"'),")
    oSql.write("\n")


    i=i+1

ano=str(2019)
mes=str(randint(1, 12))
dia=str(randint(1, 28))
id=str(randint(1, 3))
f.write("(orden"+str(i)+":Orden{"+"nombre:\""+"Orden "+str(i)+"\""+",idCliente:\""+id+
        "\""+",fecha:\""+ano+"-"+mes+"-"+dia+"\"})")
f.write("\n")


restNumber=randint(0, 9)
prodNumber=randint(0, len(productos[restNumber]))
data=""

while(n < prodNumber):
    data=data+"d.nombre =\""
    produSelect=randint(0, len(productos[restNumber])-1)
    data=data+str(productos[restNumber][produSelect])
    data=data+"\" OR "

    opSql.write("("+str(p)+","+str(i)+",'"+str(productos[restNumber][produSelect])+"'),")
    opSql.write("\n")
    p=p+1
        
    n=n+1
        
data=data+"d.nombre =\""
produSelect=randint(0, len(productos[restNumber])-1)
data=data+str(productos[restNumber][produSelect])
data=data+"\""

opSql.write("("+str(p)+","+str(i)+",'"+str(productos[restNumber][produSelect])+"');")
opSql.write("\n")
p=p+1
    
d.write("MATCH (n:Orden),(d:Producto)")
d.write("\n")
d.write("WHERE n.nombre = \"Orden "+str(i)+"\" AND ("+data+")")
d.write("\n")
d.write("CREATE")
d.write("\n")
d.write("(n)-[r:PRODUCTO]->(d)")
d.write("\n")
d.write("RETURN r,n,d;")
d.write("\n")
d.write("\n")


s.write("MATCH (n:Restaurante),(d:Orden)")
s.write("\n")
s.write("WHERE n.nombre = \""+restaurantes[restNumber]+"\" AND d.nombre =\"Orden "+str(i)+"\"")
s.write("\n")
s.write("CREATE")
s.write("\n")
s.write("(n)-[r:ORDEN]->(d)")
s.write("\n")
s.write("RETURN r,n,d;")
s.write("\n")
s.write("\n")

oSql.write("("+str(i)+","+id+",'"+restaurantes[restNumber]+"','"+ano+"-"+mes+"-"+dia+"');")
oSql.write("\n")
    
f.close()
d.close()
s.close()
oSql.close()
opSql.close()
