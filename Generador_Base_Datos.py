# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:18:02 2021

@author: Andrés Cueto Estrada
Nombre: Generador_Base_Datos
Descripción: Este script se encargará de generar la base de datos
Entradas: -Lista de empleados.xlsx
Salidas: - Base de datos.xlsx
Comentarios: 
"""
# Importando módulos
import os
import shutil
from os import path
from Biblioteca_objetos import informacion
from Lectura_archivos import lectura_documentos
from Administrador_archivos import administrador_archivos_main
from Escritura_archivos import escribiendo_excel
from Funciones_recurrentes import comparar_diccionarios


# Verificar la existencia de los archivos
def verificar_existencia_del_archivo(archivo, desactivar_mensaje):

    bandera_le = path.exists(archivo.ruta)
    if bandera_le: 
        return True
    else:
        if desactivar_mensaje == False: print('El archivo  "{}{}" no se ecnontró, por favor, ingréselo'.format(archivo.nombre, archivo.extension))
        return False
    




# Main de Generador_Base_Datos    
def generador_bd_main(info):
    # Lista de empleados
    bandera_le = verificar_existencia_del_archivo(info.le, True)
    [bandera_le, diccionario_le] = lectura_documentos(bandera_le, info.le)
    # Base de Datos
    bandera_bd = verificar_existencia_del_archivo(info.bd, False)
    bandera_bd = bandera_bd and bandera_le
    [bandera_bd, diccionario_bd] = lectura_documentos(bandera_bd, info.bd)
    
    for elemento in diccionario_bd.values():
        print('{} \t {} \t {}'.format(elemento.nombre, elemento.esquema_gral_entrada, elemento.esquema_gral_salida))
    
    if bandera_le and bandera_bd:
        print('Actualizando base de datos')
        # Comparar diccionarios
        diccionario_superiores = comparar_diccionarios(diccionario_bd, diccionario_le)
        # Modificar BD
        escribiendo_excel(info.bd, diccionario_superiores)
        print()
    elif bandera_le and not bandera_bd:
        print('...Generando la base de datos...')
        escribiendo_excel(info.bd, diccionario_le)
    else:
         print('No se pudo generar la Base de Datos debido a la falta de uno de los archivos')   
         
    viejo = info.bd.ruta
    nuevo = info.la1.ruta
    shutil.copy(viejo, nuevo)   
    
    
    
    return bandera_le, diccionario_le, bandera_bd, diccionario_bd