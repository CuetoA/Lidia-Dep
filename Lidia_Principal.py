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
from Generador_Reporte import generador_reporte_main

# Obteniendo datos
carpeta_raiz = r'C:\Users\ADMIN\Documents\0 Professional Development\1 Trabajo y Negocios\1 Negocios\Automatizaciones\Margaleff\3 Lidia Dep\Codigo'
info = informacion(carpeta_raiz)
info.fechas.plazo_historial_dias = 4

# Indicando las posiciones para cada documento
# Lista de empleados
info.le.columnas.numero_empleado = 'A'
info.le.columnas.nombre = 'B'
info.le.columnas.categoria = 'C'
# No hay combinación de celdas en LE

# Lista de asistencia
info.la1.columnas.numero_empleado = 'A'
info.la1.columnas.categoria = 'B'
info.la1.columnas.nombre = 'E' 
info.la1.columnas.hora_entrada = 'H'
info.la1.columnas.hora_salida = 'I'
info.la1.columnas.observaciones = 'J'
info.la1.columnas.superior = 'M'
# Lista asistencia, Celdas a combinar 
info.la1.columnas.categoria_comb = ['B','D']
info.la1.columnas.nombre_comb = ['E','G']
info.la1.columnas.observaciones_comb = ['J','K']
info.la1.columnas.superior_comb = ['M','O']

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
# Reporte asistencia, Celdas a combinar 
info.ra_e.columnas.categoria_comb = ['E','G']
info.ra_e.columnas.nombre_comb = ['B','D']
info.ra_e.columnas.observaciones_comb = ['O','Q']
info.ra_e.columnas.superior_comb = ['R','T']
info.ra_e.columnas.jornada_comb = ['L','N']  

# Base de datos
info.bd.columnas.numero_empleado = 'A'
info.bd.columnas.categoria = 'B'
info.bd.columnas.nombre = 'E' 
info.bd.columnas.hora_entrada = 'H'
info.bd.columnas.hora_salida = 'I'
info.bd.columnas.observaciones = 'J'
info.bd.columnas.superior = 'M'
# Lista asistencia, Celdas a combinar 
info.bd.columnas.categoria_comb = ['B','D']
info.bd.columnas.nombre_comb = ['E','G']
info.bd.columnas.observaciones_comb = ['J','L']
info.bd.columnas.superior_comb = ['M','O']



# ELIMINAR prueba completa
msj = 'Archivo: \t{}\nCol numemp: \t{}\nCol categoria: \t{}\nColnombre: \t{}'
msj2 = '\nCol entrada: \t{}\nCol salida: \t{}\nCol obsrv: \t{}\nCol super: \t{}'
msj3 = msj + msj2


# Ejecutando la secuencia del programa
# administrador_archivos_main(1,info)

# Generando la base de datos
#bandera_le, diccionario_le, bandera_bd, diccionario_bd = generador_bd_main(info)

# Generar el reporte
generador_reporte_main(info)













