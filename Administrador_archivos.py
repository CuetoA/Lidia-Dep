# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:02:06 2021

@author: Andrés Cueto Estrada
Nombre: Administrador-archivos
Descripción: Gestionar documentos carpetas e historial
1.- Eligiremos el comportamiento entre: 
    1) Crear y verificar las carpetas
    2) Gestionar los archivos
    3) Gestionar el historial
    4) Opciones 1) y 2)
    5) Opciones 1) y 3)
    
Entradas: 
Salidas:
Comentarios:
"""
################### ATENCIÓN, ÁREA DE NO EDICIÓN EMPIEZA #########################
# Importando módulos
import os
import errno
from os import path
from Biblioteca_objetos import informacion


################### ATENCIÓN, ÁREA DE NO EDICIÓN TERMINA #########################





# Ingrese los siguientes datos para el correcto funcionamiento del programa
comportamiento = 1
carpeta_raiz = r'C:\Users\ADMIN\Documents\0 Professional Development\1 Trabajo y Negocios\1 Negocios\Automatizaciones\Margaleff\3 Lidia Dep\Codigo'
info = informacion(carpeta_raiz)










# Funciones que se usarán el el bloque principal
def crear_carpeta(carpeta_nombre, carpeta_ruta):
    print('... Creando carpeta {} ...'.format(carpeta_nombre))
    try:
        os.mkdir(carpeta_ruta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise





def crear_verificar_carpetas():
    print('Gestionando las carpetas')
    #Checando si la carpeta raiz existe
    cr_existe = path.exists(info.cr)
    
    if cr_existe:
        c_lidiadep_existe = path.exists(info.c_lidiadep.ruta)
        c_le_existe = path.exists(info.c_le.ruta)
        c_bd_existe = path.exists(info.c_bd.ruta)
        c_la_existe = path.exists(info.c_la.ruta)
        c_ra_existe = path.exists(info.c_ra.ruta)
        
        if not c_lidiadep_existe:
            aviso = 'Atención'.upper()
            aviso += '\nLa carpeta que contiene los archivos no ha sido posicionada en la carpeta raiz.'
            aviso += 'Por favor, posicione la carpeta {} en la carpeta raiz'.format(info.c_lidiadep)
            print('\n ', aviso)
            
        if not c_le_existe:
            crear_carpeta(info.c_le.nombre, info.c_le.ruta)
            
        if not c_bd_existe:
            crear_carpeta(info.c_bd.nombre, info.c_bd.ruta)
            
        if not c_la_existe:
            crear_carpeta(info.c_la.nombre, info.c_la.ruta)
            crear_carpeta(info.c_la_hoy.nombre, info.c_la_hoy.ruta)
            crear_carpeta(info.c_la_ayer.nombre, info.c_la_ayer.ruta)
        else:
             c_la_hoy_existe = path.exists(info.c_la_hoy.ruta)   
             c_la_ayer_existe = path.exists(info.c_la_ayer.ruta) 
             if not c_la_hoy_existe: crear_carpeta(info.c_la_hoy.nombre, info.c_la_hoy.ruta)
             if not c_la_ayer_existe: crear_carpeta(info.c_la_ayer.nombre, info.c_la_ayer.ruta)
        
        if not c_ra_existe:
            crear_carpeta(info.c_ra.nombre, info.c_ra.ruta)
            
        return True
    else:
        # Notificar error de carpeta
        print('La carpeta ingresada como carpeta no existe')
        return False
        
        
def verificar_archivos():
    
 

def gestionar_los_archivos(validacion):
    
    
    
    
def gestion_historial():
    print('Gestionando el historial')










# Aquí empieza el archivo main
if comportamiento == 1:
    # Gestionar las carpetas
    crear_verificar_carpetas()
elif comportamiento == 2:
    # Gestionar el historial
     gestion_historial()
elif comportamiento == 3:
    # Gestuionar ambos, el historial y carpetas
    validacion = crear_verificar_carpetas()
    gestion_historial()


    
