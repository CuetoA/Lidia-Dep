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
from os import path
from Biblioteca_objetos import informacion
from Lectura_archivos import lectura_documentos
from Administrador_archivos import administrador_archivos_main



# Verificar la existencia de los archivos
def verificar_existencia_del_archivo(archivo):

    bandera_le = path.exists(archivo.ruta)
    if bandera_le: 
        return True
    else:
        print('El archivo  "{}{}" no se ecnontró, por favor, ingréselo'.format(archivo.nombre, archivo.extension))
        return False
    




# Main de Generador_Base_Datos    
def generador_bd_main(info):
    bandera = verificar_existencia_del_archivo(info.bd)
    [bandera, diccionario] = lectura_documentos(bandera, info.bd)
    # Por ahora se regresa el diccionario de lectura documentos para probar
    return diccionario
    # Posteriormente se verificará la existencia del archivo le Y SE LEERÁ
    
    









