# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:53:29 2021

@author: Andrés Cueto Estrada
Nombre: Lidia_Principal
Descripción: Este será el script principal con el que se ejecutarán todos los demás
Entradas: Ninguna
Salidas: Objetos
Comentarios: 
"""

# Importando bibliotecas
from Biblioteca_objetos import informacion
from Administrador_archivos import  administrador_archivos_main
from Generador_Base_Datos import generador_bd_main

# Obteniendo datos
carpeta_raiz = r'C:\Users\ADMIN\Documents\0 Professional Development\1 Trabajo y Negocios\1 Negocios\Automatizaciones\Margaleff\3 Lidia Dep\Codigo'
info = informacion(carpeta_raiz)
info.fechas.plazo_historial_dias = 4

# Indicando las posiciones para cada documento
# Lista de empleados
info.le.columnas.numero_empleado = 'A'
info.le.columnas.nombre = 'B'
info.le.columnas.categoria = 'C'
# Lista de asistencia
info.la1.columnas.numero_empleado = 'A'
info.la1.columnas.categoria = 'B'
info.la1.columnas.nombre = 'E' 
info.la1.columnas.hora_entrada = 'H'
info.la1.columnas.hora_salida = 'I'
info.la1.columnas.observaciones = 'J'
info.la1.columnas.superior = 'M'
# Reporte de asistencia excel
info.ra_e.columnas.numero_empleado = 'A'
info.ra_e.columnas.nombre = 'B'
info.ra_e.columnas.categoria = 'C'
info.ra_e.columnas.hora_entrada = 'H'
info.ra_e.columnas.hora_salida = 'I'
info.ra_e.columnas.retardo = 'J'
info.ra_e.columnas.tiempo_ext = 'K'
info.ra_e.columnas.jornada = 'L'
info.ra_e.columnas.observaciones = 'O'
info.ra_e.columnas.superior = 'R'


# Ejecutando la secuencia del programa
# administrador_archivos_main(1,info)

diccionario_bd = generador_bd_main(info)