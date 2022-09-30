#!/usr/bin/python
#-*- coding: iso-8859-1 -*-
#SimpleScript 12/07/2018
#Mejorado 18/05/2022

import os
import time
# Version
os.system("clear")
print ("\033[1;33mCREATED BY: Real Strategy\033[0m")
print ("\033[1;32mVERSION: cc-genpro2.0 \033[0m")
print ("")
banner = '''                                                                                   
                                                                                
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            
     @@                                                        @@          
     @@                                          CREDIT CARD   @@          
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
     @@                                                        @@          
     @@                                                        @@         
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
     @@                                                        @@          
     @@                                                        @@          
     @@                                       @@@@@   @@@@     @@          
     @@     @@@@@@@@@@@@@@@@                @@     @@@    @@   @@       
     @@                                    @@       @@     @@  @@     
     @@     @@@@@@@@@@@@@@@@@@@             @@     @@     @@   @@        
     @@                                       @@@@@  @@@@@     @@          
     @@                                                        @@          
     @@                                                        @@          
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
                                                                                                                                                                                                                                             
'''
print banner
## Show menu ##
print (30 * '-') 
print ("\033[1;31mGENERADOR DE BIN MASTER v2.0\033[0m") 
print (30 * '-') 
print ("\033[1;33m1.\033[1;32mGenerador bin rapido\033[0m")
print ("\033[1;33m2.\033[1;32mGenerador bin normal\033[0m") 
print ("\033[1;33m3.\033[1;32mGuardar bins en texto\033[0m") 
print ("\033[1;33m4.\033[1;32mGenerador de correo temporal\033[0m")
print ("\033[1;33m5.\033[1;32mBin Checker\033[0m")
print ("\033[1;33m6.\033[1;32mVer bin guardados\033[0m")
print ("\033[1;33m7.\033[1;32mCreditos al creador\033[0m")
print ("\033[1;33m8.\033[1;32mInformacion\033[0m")
print ("\033[1;33m0.\033[1;31mSalir...!!\033[0m")
print (30 * '-')
 
## Get input ###
choice = raw_input('\033[1;33mingresa tu opcion: \033[0m')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("") 
        os.system("bash generador")
        time.sleep(3)

elif choice == 2:
    os.system("clear")
    os.system("python2 cc-genpro.py")
elif choice == 3:
    os.system("clear")
    os.system("bash guardar")
elif choice == 4:
        os.system("clear")
        print("Ingresando al generador de correo temporal")
        print("Inicie una nueva ventana para usar el generador")
        print("para salir del navegador digite [ Q ] ")
        time.sleep(5)
        os.system("w3m https://temp-mail.org/es/")
elif choice == 5:
         os.system("python2 checker")
elif choice == 6:
         os.system("cat binlist.txt")
         time.sleep(7)
         os.system("python2 cc-genpro2.0.py")
elif choice == 7:
         os.system("clear")
         os.system("python2 creditos")
elif choice == 8:
         print ("")
         print ("MENSAJE: Este es un programa creado en python y bash, basado del generador namso.")
         time.sleep(4)
         os.system("python2 cc-genpro2.0.py")
elif choice == 0:
          exit ()
else: 
## default ##
        print ("Opcion invalida...Sigue intentando")
        time.sleep(2)
        os.system("python2 cc-genpro2.0.py")
