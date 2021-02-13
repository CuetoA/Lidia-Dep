# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:20:09 2021

@author: Andrés Cueto Estrada
Nombre: Biblioteca-objetos
Descripción: 
    Aquí se encontrarán todos los objetos requeridos por el programa 
    le - Listado de empleados
    bd - Base de datos
    ra - Reporte Asistencia
    
    cr - CARPETA RAIZ
    c_lidiadep - carpeta de los archivos del programa 
    c_le - carpeta lsitado de empleados
    c_bd - carpeta base de datos
    c_la - carpeta lista de asistencia
    c_la_hoy - carpeta lista de asistencia hoy
    c_la_ayer - carpeta lista de asistencia ayer
    c_ra - carpeta reportes de asistencia
    c_ra_a - carpeta reportes de asistencia actual
    c_ra_h - carpeta reportes de asistencia historial
    
Entradas: Ninguna
Salidas: Objetos
Comentarios: 
"""
class informacion:
    
    # Inner clases 
    class carpeta:
        nombre = ''
        ubicacion = ''
        ruta =''
        def __init__(self, nombre):
            self.nombre = nombre.title()
        def __ubicacion__(self, ubicacion):
            self.ubicacion = ubicacion
            self.ruta = ubicacion + '\\' + self.nombre

    
    class archivo: 
        nombre = ''
        ubicacion = ''
        ruta = ''
        def __init__(self, nombre):
            self.nombre = nombre.title()
        def __ubicacion__(self, ubicacion):
            self.ubicacion = ubicacion
            self.ruta = ubicacion + '\\' + self.nombre
        
    
        
  
    # Nombre de los archivos
    le = archivo('lista empleados')
    bd = archivo('base de datos')
    la1 = archivo('lista de asistencia')
    la2 = archivo('lista de asistencia')
    ra_e = archivo('reporte de asistencia')
    ra_pdf = archivo('reporte de asistencia')
    # Nombre de las carpetas
    cr = ''
    c_lidiadep = carpeta('lidia-dep')
    c_le = carpeta('lista de empleados')
    c_bd = carpeta('base de datos')
    c_la = carpeta('listas de asistencia')
    c_la_hoy = carpeta('lista de asistencia hoy')
    c_la_ayer = carpeta('lista de asistencia ayer')
    c_ra = carpeta('reportes')
    c_ra_actual = carpeta('reporte actual')
    c_ra_historial = carpeta('hitorial de reportes')
    
    
    # Funciones de la Outer Class
    def __init__(self, cr):
        self.cr = cr
        # Definiendo la ubicación de las carpetas del primer nivel
        self.c_lidiadep.__ubicacion__(cr)
        self.c_le.__ubicacion__(cr)
        self.c_bd.__ubicacion__(cr)
        self.c_la.__ubicacion__(cr)
        self.c_ra.__ubicacion__(cr)
        # Definiendo la ubicación de las carpetas del segundo nivel
        self.c_la_hoy.__ubicacion__(self.c_la.ruta)
        self.c_la_ayer.__ubicacion__(self.c_la.ruta)
        self.c_ra_actual.__ubicacion__(self.c_ra.ruta)
        self.c_ra_historial.__ubicacion__(self.c_ra.ruta)
        
        # Definiendo la ubicación de los archivos del segundo nivel
        self.bd.__ubicacion__(self.c_bd.ruta)
        self.le.__ubicacion__(self.c_le.ruta)
        # Definiendo la ubicación de los archivos del tercer nivel
        self.la1.__ubicacion__(self.c_la_hoy.ruta)
        self.la2.__ubicacion__(self.c_la_ayer.ruta)
        self.ra_e.__ubicacion__(self.c_ra_actual.ruta)
        self.ra_pdf.__ubicacion__(self.c_ra_actual.ruta)



