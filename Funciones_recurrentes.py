# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:54:20 2021

@author: Andrés Cueto Estrada
Nombre: Funciones_recurrentes
Descripción: Este script contendráfunciones de uso recurrente en todos los demás scripts
Entradas: -Diccionarios y otros
Salidas: - Diccionarios y otros
Comentarios: 
"""
from Biblioteca_objetos import informacion

horarios = informacion.horarios

def comparar_diccionarios(diccionario_1, diccionario_2):
    # Diccionario 1 tendrá que ser el más viejo, mientras que el 2 será el más nuevo
    # pr ahora 1) BD y 2) LE
    lista_todos = []
    lista_todos_d1 = []
    lista_todos_d2 = []
    lista_estables = []
    lista_agregados = []
    lista_eliminados = []
    lista_eliminados_agregados = []
    
    lista_todos_d1 = list(diccionario_1.keys())
    lista_todos_d2 = list(diccionario_2.keys())
    lista_todos = lista_todos_d1 + lista_todos_d2
    lista_todos = sorted(lista_todos)
    lista_todos = set(lista_todos)
    
    
    # Si están en LE pero no en BD son agregados
    for elemento in lista_todos_d2:
        if elemento not in lista_todos_d1:
            lista_agregados.append(elemento)
    # Si están en BD pero no en LE son eliminados
    for elemento in lista_todos_d1:
        if elemento not in lista_todos_d2:
            lista_eliminados.append(elemento)
    # Si están en ambos son estables
    lista_eliminados_agregados = lista_agregados + lista_eliminados
    for elemento in lista_todos:
        if elemento not in lista_eliminados_agregados:
            lista_estables.append(elemento)
    
    # Generamos un diccionario general de trabajo
    diccionario_trabajo = diccionario_2
    for elemento in diccionario_1:
        diccionario_trabajo[elemento] = diccionario_1[elemento]
    
    # Eliminamos los eliminados del diccionario
    for elemento in lista_eliminados:
        del diccionario_trabajo[elemento]
    # Separaremos los diccionarios por superior
    diccionario_superiores = {}
    for elemento in diccionario_trabajo.values():
        superior_n = elemento.superior.title()
        if superior_n == '': superior_n = 'Sin asignar'.title()
        
        if superior_n in diccionario_superiores:
            # si el cabo ya está, se agrega el elemento objeto a su lista
            diccionario_superiores[superior_n][elemento.numero_empleado] = elemento
        else:
            diccionario_superiores[superior_n] = {elemento.numero_empleado: elemento}
    
    
    
    return diccionario_superiores





def anilizar_datos_trabajador(trabajador_n):
    # ELIMINAR siguientes renglones
    from Biblioteca_objetos import trabajador
    trabajador_n =  trabajador
    
    # Obteniendo datos princiales para el análisis
    entrada_str = trabajador_n.hora_entrada
    salida_str = trabajador_n.hora_salida
    
    
    # Confirmamos que su formato sea el adecuado
    entrada, datos_inesperados_entrada, revision_manual_entrada = confirmando_formato_horas(entrada_str)
    salida, datos_inesperados_salida, revision_manual_salida  = confirmando_formato_horas(salida_str)
    
    
    # Se marca de una vez si será necesaria una revisión manual
    trabajador_n.revision_manual = revision_manual_entrada or revision_manual_salida
    trabajador_n.error_datos_inesperados = datos_inesperados_entrada or datos_inesperados_salida
    
    # Se continúa con el análisis en caso de no haber datos inesperados
    if datos_inesperados_entrada or datos_inesperados_salida:
        return trabajador_n, False
    else:
        trabajador_n, bandera = analisis_de_jornada(entrada,salida, trabajador_n)
        return trabajador_n, bandera
    

def analisis_de_jornada(entrada, salida, trabajador):
    print()
    # Verenmos 
    # A estas alturas, el trabajador ya tiene definido si tiene que aplicar o no las banderas generales, 
    # cuales son las banderas generales y si sus datos de hora de entrada y salida son correctos
    # Ahora lo que deberíamos hacer es: Analizar cada uno de sus casos
    
    # 1.- Ver si una de las banderas está activa, la que sea 
    # 2.- Si la bandera está activa checamos si entrada o salida contienen algún valor
    return trabajador, True
    
    
    
def confirmando_formato_horas(hora):    
    """
    Esta función se encarga solo de filtrar la entrada, o sea, generar una salida tipo string 
    aceptable para la función de análisis de datos.
    Ejemplo:
        Entrada  |   Salida   | Datos inesper | Rev manual
        --------------------------------------------------
        800      |    800     |     True      |    False
        400      |    400     |     True      |    True
        4:00     |    400     |     True      |    True
        4:00B    |    400     |     True      |    True
        4,00     |    400     |     True      |    True
        2401     |    2401    |     False     |    True
        40       |     40     |     True      |    True
        jdbf     |    jdbf    |     False     |    True
        ''       |    ''      |     False     |    True
    """
    # Banderas que regresará
    datos_inesperados = False # Si los datos están completamente mal
    revision_manual = False # Si los datos pueden ser interpretados y lo serán, pero requieren de revisión manual
    
    # Acondicionado simple, quitar espacios
    hora = hora.strip()
    
    # En caso de ser originalmente un espacio vacío
    if len(hora) == 0 or hora == None: 
        datos_inesperados = False
        revision_manual = False
        return hora, datos_inesperados, revision_manual
    
    elif hora.isnumeric():
        # Comprobando longitudes de cadena
        muy_corto = len(hora) < 3
        muy_largo = len(hora) > 4
        if muy_corto or muy_largo: datos_inesperados = True
        
        # Comprobando que el dato en la cadena es lógico
        hora_int = int(hora)
        mayor_que_entrada = hora_int >= horarios.entrada_temprano
        if not mayor_que_entrada: revision_manual = True
        
        menor_a_dia = hora_int <= 2400
        if not menor_a_dia: datos_inesperados = True
        
        mayor_a_salida_max = hora_int > horarios.salida_tarde
        if mayor_a_salida_max:    revision_manual = True
        
        # Si no hay datos inesperados se continúa el análisis, si hay, no se continúa
        if datos_inesperados:  return hora, datos_inesperados, revision_manual
         
            
    elif hora.isalpha():
        # Ver si es igual a alguna de las Excepciones
        datos_inesperados = not comparar_anotaciones_grales(hora)
        return hora, datos_inesperados, revision_manual
        
    elif hora.isalnum():
        hora = ''.join(filter(lambda i: i.isdigit(), hora))
        # AQUÍ, primero habría que ver si 
        confirmando_formato_horas(hora)
        
    else:
        # Si no es igual a alguna de las excepciones hay algo raro
        print('error por caracteres indefinidos en confirmando_formato_horas em Funciones_recurrentes.py')
        return hora, True, True

    # Aquí hemor terminado al parecer, con la confirmación de formatos
    return hora, datos_inesperados, revision_manual
    
def comparar_anotaciones_grales(hora):
    # Acondicionamos cadenas
    hora_aux = hora.upper()
    hora_aux = hora_aux.strip()
    
    # Instanciamos bandera de regreso
    bandera_anotaciones_grales = hora in informacion.anotaciones_generales
    
    return bandera_anotaciones_grales

    


    
    










    
