# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:58:58 2021

@author: Andrés Cueto Estrada
Nombre: Generador_Reporte
Descripción: Este será el script principal con el que se ejecutarán todos los demás
Entradas: Ninguna
Salidas: Objetos
Comentarios: 
"""
import os
import shutil
from os import path
from Biblioteca_objetos import informacion
from Lectura_archivos import lectura_documentos
from Administrador_archivos import administrador_archivos_main
from Escritura_archivos import escribiendo_excel
from Funciones_recurrentes import comparar_diccionarios
from Generador_Base_Datos import verificar_existencia_del_archivo


    
def leer_analizar_datos(archivo, bandera_reporte):
    archivo.renglones.actual = 2
    bandera, diccionario = lectura_documentos(bandera_reporte, archivo)
    print()
    
    for elemento in diccionario:
        trabajador = diccionario[elemento]
        b_esquema_entrada = trabajador.aplicar_esuqema_general_entrada
        b_esquema_salida = trabajador.aplicar_esuqema_general_salida
        esquema_entrada = trabajador.esquema_gral_entrada
        esquema_salida = trabajador.esquema_gral_salida
        superior = trabajador.superior
        
        print('{} \t {} \t {} \t {} \t {} \t {}'.format(elemento, superior,b_esquema_entrada,esquema_entrada, b_esquema_salida, esquema_salida))

#from Biblioteca_objetos import trabajador



##############################     MAIN     ###############################
def generador_reporte_main(info):
    # Verificar la existencia de los recursos
    bandera_reporte = verificar_existencia_del_archivo(info.la1, False)
    
    # Leer y analizar los datos
    leer_analizar_datos(info.la1, bandera_reporte)
    
    # Generar el documento
    print()





    
    
    
    
    
    
    
    
    