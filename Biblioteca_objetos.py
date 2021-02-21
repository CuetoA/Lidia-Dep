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
from datetime import datetime 



class informacion:
    
    anotaciones_generales = []
    anotaciones_generales.append('TC')
    anotaciones_generales.append('TE')
    anotaciones_generales.append('E')
    
    class horarios:
        entrada_regular = 800
        salida_regular = 1800
        entrada_temprano = 700
        salida_tarde = 2000
        tiempo_cuadro = 1200
        tiempo_regular = 800
        
    
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
        extension = ''
        
        # Detalles
        num_honas = 1
        nom_hojas = ['Hoja 1']
        # Ubicación de la información
        class columnas():
            nombre = ''
            superior = ''
            categoria = ''
            numero_empleado = ''
            hora_entrada = ''
            hora_salida = ''
            retardo = ''
            tiempo_ext = ''
            jornada = ''
            observaciones = ''
            
            nombre_tit = 'NOMBRE'
            superior_tit = 'SUPERIOR'
            categoria_tit = 'CATEGORÍA'
            numero_empleado_tit = 'NUMEMP'
            hora_entrada_tit = 'ENTRADA'
            hora_salida_tit = 'SALIDA'
            retardo_tit = 'RETARDO'
            tiempo_ext_tit = 'TIEMP EXTRA'
            jornada_tit = 'TIPO JORNADA'
            observaciones_tit = 'OBSERVACIONES'
            nombre_comb = ''
            superior_comb = ''
            categoria_comb = ''
            numero_empleado_comb = ''
            hora_entrada_comb = ''
            hora_salida_comb = ''
            retardo_comb = ''
            tiempo_ext_comb = ''
            jornada_comb = ''
            observaciones_comb = ''
            
            def __init__(self):
                pass
            
        class renglones():
            actual = 0
            titulos = 1
            inicial = 2
            anotacion_general = 2
            def __init__(self):
                pass
            
        class celdas():
            nombre = ''
            superior = ''
            categoria = ''
            numero_empleado = ''
            hora_entrada = ''
            hora_salida = ''
            retardo = ''
            tiempo_extr = ''
            jornada = ''
            observaciones = ''
            def __init__(self):
                pass
        
            

        def __init__(self, nombre):
            self.nombre = nombre.title()
        def __ubicacion__(self, ubicacion, extension):
            self.ubicacion = ubicacion
            self.extension = extension
            self.ruta = ubicacion + '\\' + self.nombre + self.extension
        def siguiente_renglón(self):
            if self.renglones.actual == 0:
                self.renglones.actual = self.renglones.inicial
            else:
                self.renglones.actual += 1
            self.generando_celdas_actuales ()
        
        def generando_celdas_actuales(self):
            renglon_actual_str = str(self.renglones.actual)
            # En objetos string
            #print('columnas superior',self.columnas.superior )
            #print('renglon actual', renglon_actual_str)
            self.celdas.nombre = self.columnas.nombre + renglon_actual_str
            self.celdas.superior = self.columnas.superior + renglon_actual_str
            self.celdas.categoria = self.columnas.categoria + renglon_actual_str
            self.celdas.numero_empleado = self.columnas.numero_empleado + renglon_actual_str
            self.celdas.hora_entrada = self.columnas.hora_entrada + renglon_actual_str
            self.celdas.hora_salida = self.columnas.hora_salida + renglon_actual_str
            self.celdas.retardo = self.columnas.retardo + renglon_actual_str
            self.celdas.tiempo_extr = self.columnas.tiempo_ext + renglon_actual_str
            self.celdas.jornada = self.columnas.jornada + renglon_actual_str
            self.celdas.observaciones =  self.columnas.observaciones + renglon_actual_str
            
            
        
        
        
    class fecha:
        formato = '%d-%m-%y'
        plazo_historial_dias = 30
        hoy = datetime.today()
        
    
        
  
    # Nombre de los archivos
    le = archivo('lista empleados')
    le.celdas = archivo.celdas()
    le.renglones = archivo.renglones()
    le.columnas = archivo.columnas()
    
    bd = archivo('base de datos')
    bd.celdas = archivo.celdas()
    bd.renglones = archivo.renglones()
    bd.columnas = archivo.columnas()
    
    la1 = archivo('lista de asistencia')
    la1.celdas = archivo.celdas()
    la1.renglones = archivo.renglones()
    la1.columnas = archivo.columnas()
    
    la2 = archivo('lista de asistencia')
    la2.celdas = archivo.celdas()
    la2.renglones = archivo.renglones()
    la2.columnas = archivo.columnas()
    
    ra_e = archivo('reporte de asistencia')
    ra_e.celdas = archivo.celdas()
    ra_e.renglones = archivo.renglones()
    ra_e.columnas = archivo.columnas()
    
    ra_pdf = archivo('reporte de asistencia')
    ra_pdf.celdas = archivo.celdas()
    ra_pdf.renglones = archivo.renglones()
    ra_pdf.columnas = archivo.columnas()
    
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
    # Instanciando nuestro objeto fechas
    fechas = fecha()
    
    
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
        self.bd.__ubicacion__(self.c_bd.ruta, '.xlsx')
        self.le.__ubicacion__(self.c_le.ruta, '.xlsx')
        # Definiendo la ubicación de los archivos del tercer nivel
        self.la1.__ubicacion__(self.c_la_hoy.ruta, '.xlsx')
        self.la2.__ubicacion__(self.c_la_ayer.ruta, '.xlsx')
        self.ra_e.__ubicacion__(self.c_ra_actual.ruta, '.xlsx')
        self.ra_pdf.__ubicacion__(self.c_ra_actual.ruta, '.pdf')










class trabajador:
    nombre = ''
    apellido_1 = ''
    apellido_2 = ''
    nombre_completo = ''
    
    superior = ''
    categoria = ''
    numero_empleado = ''
    
    hora_entrada = ''
    hora_salida = ''
    retardo = ''
    tiempo_extra = ''
    jornada_laboral = ''
    observaciones = ''
    
    # Errores al momento de analizar los datos
    error_datos_inesperados = False
    revision_manual = False
    
    # Esquemas generales para todos los trabajadores
    aplicar_esuqema_general_entrada = False
    aplicar_esuqema_general_salida = False
    esquema_gral_entrada = ''
    esquema_gral_salida = ''
    
    
    
    
    def __init__(self, numero_empleado, nombre_completo, categoria):
        #[self.apellido1, self.apellido2, self.nombre] = nombre_completo.split()
        self.numero_empleado = numero_empleado
        self.nombre_completo = nombre_completo
        self.categoria = categoria
    def clear(self):
        self.nombre = ''
        self.apellido_1 = ''
        self.apellido_2 = ''
        self.nombre_completo = ''
        
        self.superior = ''
        self.categoria = ''
        self.numero_empleado = ''
        
        self.hora_entrada = ''
        self.hora_salida = ''
        self.retardo = ''
        self.tiempo_extra = ''
        self.jornada_laboral = ''
        self.observaciones = ''
        self.error_datos_inesperados = False
        self.revision_manual = False


        
    
    
    
    
    
    