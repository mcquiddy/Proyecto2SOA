const express = require("express");
const app = express();
const port = 3000;

const neo4j = require('neo4j-driver').v1;

const driver = neo4j.driver('bolt://localhost', neo4j.auth.basic('neo4j', 'catalog1234'));
const session = driver.session();

app.get("/report/:id", function(req, res) { 
    session
        .run('MATCH (rest:Restaurante)-->(ord:Orden)-[r:PRODUCTO]-(p:Producto) ' +
        'WHERE rest.nombre = {nameParam}' + 
        'WITH distinct p.nombre as name ,count(*) as ordersAmount ' +
        'RETURN name ' + 
        'ORDER BY ordersAmount DESC ' +
        'LIMIT(5)',{nameParam:req.params.id})
        .then(function(result){
            result.records.forEach(function(record) {
                console.log(record);
            });
        })
        .catch(function(err){
            console.log(err);
        });

    res.send("REPORTE")
});

app.get("/order/:id", function(req, res) { 
    session
        .run('CREATE ({nameParam}) ' + ' ' ,{nameParam:req.params.id})
        .then(function(result){
            result.records.forEach(function(record) {
                console.log(record);
            });
        })
        .catch(function(err){
            console.log(err);
        });

    res.send("ORDEN CREADA")
});

app.get("/order/relation/product/:id", function(req, res) { 

    session
        .run('MATCH (n:Orden),(d:Producto) ' + 
        'WHERE {nameParam} ' +
        'CREATE ' +
        '(n)-[r:PRODUCTO]->(d) ' + 
        'RETURN r,n,d;',{nameParam:req.params.id})
        .then(function(result){
            result.records.forEach(function(record) {
                console.log(record);
            });
        })
        .catch(function(err){
            console.log(err);
        });

    res.send("RELACION CREADA ORDEN-PRODUCTO")
});

app.get("/order/relation/restaurant/:id", function(req, res) { 

    session
        .run('MATCH (n:Restaurante),(d:Orden) ' + 
        'WHERE {nameParam} ' +
        'CREATE ' +
        '(n)-[r:PRODUCTO]->(d) ' + 
        'RETURN r,n,d;',{nameParam:req.params.id})
        .then(function(result){
            result.records.forEach(function(record) {
                console.log(record);
            });
        })
        .catch(function(err){
            console.log(err);
        });

    res.send("RELACION CREADA ORDEN-PRODUCTO")
});

app.get("/", function(req, res) { 
    res.send("HOLA MUNDO NODE JS Y NEO 4J")
});
app.listen(port, () => console.log(`Listening on port ${port}`));