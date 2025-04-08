'''
Apellido y nombre: Llopi Gabriel
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion 1
Instancia: Primer examen parcial
'''

import json
from os import system

def leer_json(nombre_archivo):
    data = []
    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
    return(data)

def leer_csv(nombre_archivo):
    lista = []
    lista_final = []
    
    with open(nombre_archivo, 'r') as archivo:
        
        lista_lineas = archivo.readlines()
        for i in range(len(lista_lineas)):
            lista_lineas[i] = lista_lineas[i].replace(",\n", "")
            if i == 0:
                keys = lista_lineas[i].split(",")
            else:
                lista.append(lista_lineas[i].split(","))
        for i in range(len(lista)):
            diccionario = {}
            for j in range(len(lista[i])):
                diccionario.update({keys[j] : lista[i][j]})
            lista_final.append(diccionario)
    return lista_final

def alta(mensaje:str)->str:
    '''
    Recibe un comentario para que el usuario introduzca el dato necesario.
    Retorna el dato que ingrese el usuario.
    '''
    dato = input(mensaje)
    return dato

def convertir_mayuscula(variable:str)->str:
    cantidad = contar_caracteres(variable)
    retorno = ""    
    
    for i in range(cantidad):

        if ord(variable[i]) >= 97 and ord(variable[i]) <= 122:
            letra = chr(ord(variable[i])-32)               
            retorno += letra
        else:
            retorno += variable[i]
        
    return retorno

def normalizar_datos (lista:list):
    """_summary_
    Recibe como parametro una lista y convierte todos los value numericos de string a entero o flotante segun cada caso.
    Args:
        lista (list): Recibe una lista de diccionarios a recorrer

    Returns:
        bool: Devuelve un booleano, si hace el casteo sera True, si es una lista vacia o si los datos ya fueron normalizados retornara False.
    """    
    retorno = False
    for personaje in lista:
        for key in personaje.keys():
            if type(personaje[key]) != type(int) or type(personaje[key]) != type(float):               
                if personaje[key].isdigit():
                    personaje[key] = int(personaje[key])
                    retorno = True
                else:
                    flag_2 = False
                    flag = False
                    for letra in personaje[key]:
                        if letra.isdigit() == True:
                            flag = True
                        elif letra == ".":
                            flag_2 = True
                        else:
                            flag = False
                    if flag and flag_2:
                        personaje[key] = float(personaje[key])
                        retorno = True
    if retorno == True:
        print("Datos Normalizados")
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    return retorno

def buscar(lista:list, dato:str)->int:
    '''
    La funcion busca el dato en una lista.
    Si es encontrado, retornará su índice.
    En caso contrario, retornará -1. 
    '''
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

def listar_id_nombre(diccionario:dict):
    '''
    Listado de ID y NOMBRES.

    Recibe un diccionario, e imprime ID y el NOMBRE vinculado a esa id
    '''
    for pasajero in diccionario:
        for clave in pasajero.keys():
            if clave == 'Id':
                mensaje = 'ID:  {0}. \t Nombre: {1}'.format(pasajero[clave], pasajero['Apellido_Nombre_Pasajero'])
                print(mensaje)

def validar_id(diccionario:dict, id:str):
    """Busca la ID ingresada. Si no existe, retornará False
    Devuelve la lista del pasajero correspondiente al ID

    Args:
        diccionario (dict): el diccionario que recorre debe contener datos
        id (str):

    Returns:
        _type_: devuelve el diccionario que contenga la id ingresada. Caso contrario retornará False
    """

    retorno = False
    for pasajero in diccionario:
        for clave in pasajero.keys():
            if clave == 'Id' and id == str(pasajero[clave]):
                retorno = pasajero
    
    return retorno

def consultar_id(diccionario:dict)->dict:
    """Consulta al usuario un ID. Buscará en el diccionario el id seleccionado. En caso de no hallar, preguntará por un ID valido.

    Args:
        diccionario (dict): _description_

    Returns:
        dict: devuelve el usuario que contenga la ID seleccionada
    """ 
    opcion = input('Seleccione el ID del usuario correspondiente')
    persona_encontrada = validar_id(diccionario, opcion)
    while persona_encontrada == False:
        opcion = input('Error, seleccione el ID del usuario correspondiente')
        persona_encontrada = validar_id(diccionario, opcion)
    return persona_encontrada

def contar_indice(diccionario:dict)->int:
    """cuenta el total de indice de una lista de un diccionario
    Devuelve el indice final

    Args:
        diccionario (dict): diccionario principal que contiene la lista
        nombre_lista (list): lista perteneciente al diccionario

    Returns:
        int: indice
    """    
    contador = 0
    for i in diccionario:
        contador += 1
    return contador

def contar_caracteres(variable:str)->int:
    contador = 0
    for letra in variable:
        contador += 1

    return contador

def introducir_fecha():
    fecha= ''

    año = input('Ingrese el año ("20XX"): ')
    while contar_caracteres(año) != 4 or not año.isdigit() or int(año) < 2000 or int(año) > 2050:
        año = input('ERROR, ingrese el año ("20XX"): ')
    fecha += año

    mes = input('Ingrese el mes ("XX"): ')
    while contar_caracteres(mes) != 2 or not mes.isdigit() or int(mes) > 12 or int(mes) < 0:
        mes = input('ERROR, ingrese el mes ("XX"): ')
    fecha += mes

    dia = input('Ingrese el dia ("XX"): ')
    while contar_caracteres(dia) != 2 or not dia.isdigit() or int(dia) > 31 or int(dia) < 0:
        dia = input('ERROR, ingrese el dia ("XX"): ')
    fecha += dia

    return fecha

def modificar_dni():
    cambio = input('Ingrese el nuevo DNI: ')
    while len(cambio) != 8 or not cambio.isdigit():
        cambio = input('ERROR, ingrese el nuevo DNI: ')
    return cambio

def modificar_nombre_apellido():
    cambio = input('Ingrese el nuevo apellido y nombre: ')
    while len(cambio) > 30:
        cambio = input('ERROR. Nombre muy largo. Ingrese otro: ')
    return cambio

def registrar_nuevo_vuelo(diccionario:dict):
    """Pide al usuario el ingreso de datos, y valida que sean los adecuados antes de guardarlos

    Args:
        diccionario (dict): _description_

    Returns:
        dict: retorna un diccionario con los datos almacenados 
    """
    indice= contar_indice(diccionario)
    indice +=1

    nombre_aerolinea = alta('Introduzca la aerolinea (LATAM | AA | IBERIA): ')
    while nombre_aerolinea.upper() != 'LATAM' and nombre_aerolinea.upper() != 'AA' and nombre_aerolinea.upper() != 'IBERIA':
        nombre_aerolinea = alta('Introduzca la aerolinea (LATAM | AA | IBERIA): ')

    nombre_y_apellido = alta('Introduzca el nombre del pasajero (Menos de 30 caracteres): ')
    while len(nombre_y_apellido) > 30:
        nombre_y_apellido = alta('Introduzca el nombre del pasajero (Menos de 30 caracteres): ')

    dni = alta('Introduzca el DNI del pasajero: ')
    while not int(dni.isdigit()) or contar_caracteres(dni) != 8:
        dni = alta('Introduzca el DNI del pasajero: ')

    precio_vuelo = alta('Introduzca el precio: ')
    while not int(precio_vuelo.isdigit()) or float(precio_vuelo) < 500000 or float(precio_vuelo) > 2000000:
        precio_vuelo = alta('Introduzca el precio: ')

    origen_vuelo = alta('Introduzca el origen del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')
    while origen_vuelo.upper() != 'BUENOS AIRES' and origen_vuelo.upper() != 'ROMA' and origen_vuelo.upper() != 'TOKIO' and origen_vuelo.upper() != 'PARIS' and origen_vuelo.upper() != 'MIAMI' and origen_vuelo.upper() != 'MADRID':
        origen_vuelo = alta('Introduzca el origen del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')

    destino_vuelo = alta('Introduzca el destino del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')
    while destino_vuelo.upper() != 'BUENOS AIRES' and destino_vuelo.upper() != 'ROMA' and destino_vuelo.upper() != 'TOKIO' and destino_vuelo.upper() != 'PARIS' and destino_vuelo.upper() != 'MIAMI' and destino_vuelo.upper() != 'MADRID' or destino_vuelo == origen_vuelo:
        destino_vuelo = alta('Introduzca el destino del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')

    clase = alta('turista | ejecutivo: ')
    while clase.upper() != 'TURISTA' and clase.upper() != 'EJECUTIVO':
        clase = alta('turista | ejecutivo: ')

    fecha_vuelo = introducir_fecha()

    datos = {
    "Id": indice,
    "Aerolinea": nombre_aerolinea.upper(),
    "Apellido_Nombre_Pasajero": nombre_y_apellido.capitalize(),
    "DNI_Pasajero": dni,
    "Precio": precio_vuelo,
    "Origen": origen_vuelo.capitalize(),
    "Destino": destino_vuelo.capitalize(),
    "Clase": clase.capitalize(),
    "Fecha": fecha_vuelo
    }

    return datos

def submenu_modificar(persona_modificar):
    
    for i in persona_modificar:
        print(i, ':\t \t', persona_modificar[i])
    print(' ')
    print("Menu")
    print("1_DNI")
    print("2_Apellido y Nombre") 
    print("3_Fecha")
    print("4_Salir")

    opcion = input("Seleccione lo que desea modificar: ")
    system('cls')
    match opcion:
        case '1':
            persona_modificar['DNI_Pasajero'] = modificar_dni()
            print('Cambio realizado exitosamente')
        case '2':
            persona_modificar['Apellido_Nombre_Pasajero'] = modificar_nombre_apellido().capitalize()
            print('Cambio realizado exitosamente')
        case '3':
            persona_modificar['Fecha'] = introducir_fecha()
            print('Cambio realizado exitosamente')
        case '4':
            pass
        case _:
            print('Error, se ingresó un dato erróneo')
    return persona_modificar

def consultar_finalizar():
    opcion = input('¿Desea finalizar? S | N: ')
    respuesta_valida = False
    if opcion.upper() == "S":    
            respuesta_valida = True
            continuar = False
    elif opcion.upper() == 'N':
            respuesta_valida = True
            continuar = True
    while not respuesta_valida:
        opcion = input('¿Desea finalizar? S | N: ')
        if opcion.upper() == "S":    
            respuesta_valida = True
            continuar = False
        elif opcion.upper() == 'N':
            respuesta_valida = True
            continuar = True
    return continuar

def actualizar_json(nombre_archivo:str, nuevo_diccionario:dict):
    """Actualiza el archivo ingresado por el segundo

    Args:
        nombre_archivo (str): nombre del archivo original
        nuevo_diccionario (dict): diccionario que reemplazará el archivo .json
    """    
    carga = {}
    carga.update(nuevo_diccionario)

    with open(nombre_archivo, 'w') as file:
        json.dump(carga, file, indent= 4, separators= (',', ': '))
        print('Éxito, registro actualizado')

def validar_eliminacion(persona_borrar:dict):
    mensaje = '¿Está seguro que quiere eliminar a {0}? S | N: '.format(persona_borrar['Apellido_Nombre_Pasajero'])
    opcion = input(mensaje)
    respuesta_valida = False
    if opcion.upper() == "N":    
            respuesta_valida = True
            continuar = False
    elif opcion.upper() == 'S':
            respuesta_valida = True
            continuar = True
    while not respuesta_valida:
        opcion = input(mensaje)
        if opcion.upper() == "N":    
            respuesta_valida = True
            continuar = False
        elif opcion.upper() == 'S':
            respuesta_valida = True
            continuar = True
    return continuar

def acomodar_tras_eliminacion(registro_vuelos:dict, persona_borrar:dict):
        lista_nueva = []

        for pasajero in registro_vuelos: #acomodo los ID y agrego a una nueva lista
            if pasajero['Id'] != persona_borrar['Id']:
                if pasajero['Id'] > persona_borrar['Id']:      
                    pasajero['Id'] -= 1
                    lista_nueva.append(pasajero)    
                else:
                    lista_nueva.append(pasajero)

        return lista_nueva

def rellenar_bytes(cadena_caracteres:str)->str:
    """recibe un string, y en caso de que no llegue a un byte (multiplo de 8 caracteres), lo completará con caracteres vacios

    Args:
        cadena_caracteres (str): _description_

    Returns:
        str: retorna el str con el tamaño de un byte
    """    

    retorno = False
    while not len(cadena_caracteres) == 8 and not len(cadena_caracteres) == 16 and not len(cadena_caracteres) == 24 and not len(cadena_caracteres) == 32:
        cadena_caracteres += ' '
        
    retorno = cadena_caracteres
    return retorno

def A_cargar_json(opcion:str)->dict|bool:
    """Cumple las condiciones solicitadas del punto A.
    NO ES REUTILIZABLE.
    
    Args:
        opcion (str): recibe una letra
        "A" -> cargar datos json
        "G" -> salir
        Cualquier otro caracter imprimirá que ha ocurrido un error.

    Returns:
        dict|bool: retorna el archivo json cargado, o un False
    """    
    match opcion:
        case 'A' | 'a':
            with open('data.json', 'r') as file:
                archivo_json = json.load(file)['pasajeros']
            print('Datos cargados correctamente')
            return archivo_json
            #archivo_json = leer_json('data.json')
        
        case 'G' | 'g':
            continuar = False
            return continuar

        case _:
            print('Error, cargue el archivo json primero')

def B_alta(diccionario:dict):
    """Cumple las condiciones solicitadas del punto B.
    NO ES REUTILIZABLE.

    Args:
        diccionario (dict): variable donde está contenido la informacion del archivo json
    """    
    nuevo_vuelo = registrar_nuevo_vuelo(diccionario)
    diccionario.append(nuevo_vuelo)
    #actualizar_json('data.json', diccionario)

def C_modificar(diccionario:dict):
    """Cumple las condiciones solicitadas del punto C.
    NO ES REUTILIZABLE.

    Args:
        diccionario (dict): variable donde está la información del archivo json
    """    
    listar_id_nombre(diccionario)
    persona_modificar = consultar_id(diccionario)
    persona_modificada = submenu_modificar(persona_modificar)
    while consultar_finalizar():
        persona_modificada = submenu_modificar(persona_modificar)
    #actualizar_json('data.json', diccionario)

def D_baja(diccionario:dict):
    """Cumple las condiciones solicitadas del punto D.
    NO ES REUTILIZABLE.

    Args:
        diccionario (dict): variable donde está la información del archivo json
    """    
    listar_id_nombre(diccionario)
    persona_borrar = consultar_id(diccionario)
    eliminacion_confirmada = validar_eliminacion(persona_borrar)

    if eliminacion_confirmada:
        lista_nueva = acomodar_tras_eliminacion(diccionario, persona_borrar)
        diccionario = lista_nueva
        print(diccionario)
        mensaje = 'Se ha eliminado correctamente a {0}'.format(persona_borrar['Apellido_Nombre_Pasajero'])
    else:
        mensaje = 'Se ha cancelado la eliminación de {0}'.format(persona_borrar['Apellido_Nombre_Pasajero'])
    print(mensaje)
    return diccionario

def E_listar(diccionario:dict):
    """Recibe la lista de vuelos y lista tal como pide el enunciado.
    NO es reutilizable

    Args:
        diccionario (dict): Recibe el registro de vuelos
    """

    lista_ordenada_E = ['Fecha','Aerolinea','Clase','Origen','Destino','Precio', 'DNI_Pasajero','Apellido_Nombre_Pasajero']

    encabezado = ''
    for dato in lista_ordenada_E:
        encabezado += '|'
        dato = rellenar_bytes(dato)
        encabezado += dato
        
    print(encabezado)
                
    for pasajero in diccionario:
        mensaje = ''
        for dato in lista_ordenada_E:
            mensaje+= '|'
            mensaje += rellenar_bytes(pasajero[dato])
            
        print(mensaje)

def obtener_maximo(lista:list, clave:str):
    retorno = False
    flag = True
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):
                break
            if flag == True or personaje[clave] > retorno:
                retorno = personaje[clave]
                flag = False
    
    return retorno

def obtener_minimo(lista:list, clave:str):
    retorno = False
    flag = True
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):
                break
            if flag == True or personaje[clave] < retorno:
                retorno = personaje[clave]
                flag = False

    return retorno

def swap(lista:list, dato1, dato2):
    auxiliar = dato1
    dato1 = dato2
    dato2 = auxiliar
    return lista

def ordenar_lista_diccionarios(lista:list,key:str, criterio:str):
	"""ordenamiento de diccionarios que pertenecen a una lista.
	No usar en listas simples

	Args:
		lista (list): lista con los datos a ordenar
		key (str): clave por el cual se realizará el ordenamiento
		criterio (str): asc | desc. Define si el orden se hará ascendente o descendiente
	"""	
	for i in range(len(lista) - 1):
		for j in range(i+1, len(lista)):
			if criterio.lower() == 'asc' and lista[i][key] > lista[j][key] or criterio.lower() == 'desc' and lista[i][key] < lista[j][key]:
				auxiliar = lista[i]
				lista[i] = lista[j]
				lista[j] = auxiliar

def guardar_archivo(nombre_archivo:str, contenido_archivo:str):
    retorno= False
    if len(nombre_archivo) != 0 and len(contenido_archivo) != 0:
        with open(nombre_archivo, 'w') as file:
            file.write(contenido_archivo)
            retorno = 'Se creó el archivo: ' + nombre_archivo
    return retorno

def generar_csv(nombre_archivo:str, lista:list):
    """crea un csv que contiene la informacion de una lista

    Args:
        nombre_archivo (str): nombre del archivo csv
        lista (list): lista que se guardará en el csv

    Returns:
        _type_: _description_
    """    
    retorno = False
    all_keys = ''
    datos = ''
    if len(lista) != 0:
        for key in lista[0].keys():
            all_keys += str(key) + ','
        all_keys += '\n'
        for personaje in lista:
            for dato in personaje.values():
                datos += str(dato) + ','
            datos += '\n'
        guardar_archivo(nombre_archivo, all_keys + datos)
    else:
        return False
    
