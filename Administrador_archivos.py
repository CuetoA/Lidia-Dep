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
    6) Opciones 1), 2) y 3)
    
Entradas: 
Salidas:
Comentarios:
"""
################### ATENCIÓN, ÁREA DE NO EDICIÓN EMPIEZA #########################
# Importando módulos
import os
import errno
import time
import shutil
from os import path
import datetime as dt
from datetime import datetime
from Biblioteca_objetos import informacion


################### ATENCIÓN, ÁREA DE NO EDICIÓN TERMINA #########################





# Ingrese los siguientes datos para el correcto funcionamiento del programa
#comportamiento = 1
#carpeta_raiz = r'C:\Users\ADMIN\Documents\0 Professional Development\1 Trabajo y Negocios\1 Negocios\Automatizaciones\Margaleff\3 Lidia Dep\Codigo'
#info = informacion(carpeta_raiz)










# Funciones que se usarán el el bloque principal
def crear_carpeta(carpeta_nombre, carpeta_ruta):
    print('\t...Creando carpeta {}...'.format(carpeta_nombre))
    try:
        os.mkdir(carpeta_ruta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# Función para verificar la existencia de carpetas y, si no existen, las crea
def crear_verificar_carpetas(info):
    print('...Gestionando las carpetas...')
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
             if not c_la_hoy_existe: 
                 crear_carpeta(info.c_la_hoy.nombre, info.c_la_hoy.ruta)
             if not c_la_ayer_existe: 
                 crear_carpeta(info.c_la_ayer.nombre, info.c_la_ayer.ruta)
        
        if not c_ra_existe:
            crear_carpeta(info.c_ra.nombre, info.c_ra.ruta)
            crear_carpeta(info.c_ra_actual.nombre, info.c_ra_actual.ruta)
            crear_carpeta(info.c_ra_historial.nombre, info.c_ra_historial.ruta)
        else:
            c_ra_actual_existe = path.exists(info.c_ra_actual.ruta)
            c_ra_historial_existe = path.exists(info.c_ra_historial.ruta)
            if not c_ra_actual_existe:
                crear_carpeta(info.c_ra_actual.nombre, info.c_ra_actual.ruta)
            if not c_ra_historial_existe:
                crear_carpeta(info.c_ra_historial.nombre, info.c_ra_historial.ruta)
            
        return True
    else:
        # Notificar error de carpeta
        print('La carpeta ingresada como carpeta no existe')
        return False
        
    
    
 
# Función que mueve los archivos de un lado a otro
def gestionar_los_archivos(info):
    print('...Gestionando los archivos...')
    # Verificando la existencia de los archivos a gestionar
    bandera_la1 = path.exists(info.la1.ruta)
    bandera_la2 = path.exists(info.la2.ruta)
    bandera_ra_e = path.exists(info.ra_e.ruta)
    bandera_ra_pdf = path.exists(info.ra_pdf.ruta)
    # Mensaje de fallo
    mensaje = '\t No se encontró el archivo: {}{}'
    
    # Gestión:
    if bandera_la2:
        os.remove(info.la2.ruta)
    else:
        print(mensaje.format(info.la2.nombre, info.la2.extension))
        
    if bandera_la1:
        nueva_ruta = info.la2.ubicacion + '\\' + info.la1.nombre + info.la1.extension
        shutil.move(info.la1.ruta, nueva_ruta)
    else:
        print(mensaje.format(info.la1.nombre, info.la1.extension))
        
    if bandera_ra_e:
        tiempo_c = time.gmtime( path.getctime(info.ra_e.ruta) )
        tiempo_formato = time.strftime('%d-%m-%y', tiempo_c)
        nuevo_nombre = info.ra_e.nombre + ' ' + tiempo_formato + info.ra_e.extension
        nueva_ruta = info.c_ra_historial.ruta + '\\' + nuevo_nombre
        shutil.move(info.ra_e.ruta, nueva_ruta)
    else:
        print(mensaje.format(info.ra_e.nombre, info.ra_e.extension))
        
    if bandera_ra_pdf:
        tiempo_c = time.gtime( path.getctime(info.ra_pdf.ruta) )
        tiempo_formato = time.strftime('%d-%m-%y', tiempo_c)
        nuevo_nombre = info.ra_pdf.nombre + ' ' + tiempo_formato + info.ra_pdf.extension
        nueva_ruta = info.c_ra_historial + '\\' + nuevo_nombre
        shutil.move(info.ra_pdf.ruta, nueva_ruta)
    else:
        print(mensaje.format(info.ra_pdf.nombre, info.ra_pdf.extension))
        
    
    
    
    
def gestion_historial(info):
    print('Gestionando el historial')
    # Listando los archivos
    lista_archivos = os.listdir( info.c_ra_historial.ruta )
    
    # Futuras listas a ocupar
    fechas_eliminar = []
    fechas_archivos = []
    
    # Generando lista de fechas
    for archivo in lista_archivos:
        # Obteniendo unicamente la fecha
        if info.ra_e.nombre in archivo:
            auxiliar = archivo.replace(info.ra_e.nombre,'')
            auxiliar = auxiliar.strip()
            lugar_punto_extension = auxiliar.find('.')
            if lugar_punto_extension > 0:
                auxiliar = auxiliar.split('.',1)[0]
                fechas_archivos.append(auxiliar)
        
    # Encontrando las fechas despreciables
    for fecha in fechas_archivos:
        fecha_limite = info.fechas.hoy - dt.timedelta(days = info.fechas.plazo_historial_dias)
        fecha_d = datetime.strptime(fecha, info.fechas.formato )
        diferencia = fecha_d - fecha_limite
        if diferencia.days < 0:
            fechas_eliminar.append(fecha)
        
        
    # Eliminando los archuivos coincidentes
    for archivo in lista_archivos:
        for fecha in fechas_eliminar:
            comparacion = fecha in archivo
            if comparacion:
                file = info.c_ra_historial.ruta + '\\' + archivo
                os.remove(file)
                
    
            
            





# Aquí empieza el archivo principal del Administrador de archivos
def administrador_archivos_main(comportamiento, info):
    if comportamiento == 1:
        crear_verificar_carpetas(info)
        
    elif comportamiento == 2:
        gestionar_los_archivos(info)
        
    elif comportamiento == 3:
         gestion_historial(info)
         
    elif comportamiento == 4:
        validacion = crear_verificar_carpetas(info)
        if validacion: gestionar_los_archivos(info)
        
    elif comportamiento == 5:
        validacion = crear_verificar_carpetas(info)
        if validacion: gestion_historial(info)
        
    elif  comportamiento == 6:
        validacion = crear_verificar_carpetas(info)
        if validacion: 
            gestionar_los_archivos(info)
            gestion_historial(info)

    


    
