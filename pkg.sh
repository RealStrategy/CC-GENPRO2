#!bin/bash

#Descargando paquetes
#Cambiar pkg por apt para otros sistemas
apt update && apt upgrade -y

pkg install python2 -y
pkg install w3m
