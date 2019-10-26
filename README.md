
# Tecnológico de Costa Rica

Ing. Computadores.

Desarrolladores: Cristian Castillo McQuiddy. Jairo Ortega Calderón.

Septiembre, 2019.

Infraestructura de Software

Segundo proyecto de SOA4ID.

## Dependencias

Node 
Ruby
Goolang
Python 

Kubernetes
Docker

Neo4j
Sql Server

## Configuración

Para configurar el clúster se puede seguir el siguiente tutorial, en el mismo se encuentra como instalar lo necesario:
https://www.linuxtechi.com/install-configure-kubernetes-ubuntu-18-04-ubuntu-18-10/
En el hay tener presente que las direcciones ip de los nodos que se agregan en el archivo /etc/hosts
deben ser las pertenecientes a cada máquina. Para ver cual tiene su computadora puede ejecutar el comando "$ ifconfig".

Además, es muy importante cuando se inicialice kubernetes en el nodo master ($ sudo kubeadm init --pod-network-cidr=<ip>) definir 
la ip como 10.244.0.0/16 ya que está se relaciona con Flannel que se utilizará como pod network.
