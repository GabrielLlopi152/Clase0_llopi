from os import system
from data_stark import lista_heroes


def promedio_por_genero (diccionario:dict,clave:str,genero:str)->float:
    """_summary_

    Args:
        diccionario (dict): _description_
        key (str): _description_

    Returns:
        float: _description_
        ctrl+shift+2
    """    
    contador = 0
    acumulador_fuerza = 0

    for datos in diccionario:
        for key in datos.keys():
            if key == clave and  datos['genero'] == genero:
                acumulador_fuerza = acumulador_fuerza + float(datos[key])
                contador = contador + 1

    if contador > 0 :
        return acumulador_fuerza / contador
    
def clave_max_min_genero (diccionario:dict, clave:str, genero:str, comparacion:str):
    bandera = True
    for personaje in diccionario:
        if personaje["genero"] == genero:
            if comparacion == "MAX":
                if bandera == True or float(personaje[clave]) > clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
            elif comparacion == "MIN":
                if bandera == True or float(personaje[clave]) < clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
    if bandera == True:
        nombre = "No hay personajes con este genero"
    return nombre

def pausa():
    var = input("Presione Enter para continuar...")
    system ("cls")

def listar_por_caracteristica(lista:list, clave_a_buscar:str):
    diccionario_auxiliar = {}

    for personaje in lista:
        clave = personaje[clave_a_buscar].capitalize()
        if clave != "":
            if clave in diccionario_auxiliar:
                diccionario_auxiliar[clave] += " - " + personaje["nombre"]
            else:
                diccionario_auxiliar[clave] = personaje["nombre"]


    for clave, nombres in diccionario_auxiliar.items():
        print(f"{clave}: {nombres}")
        print ("------------------------")
    
def contar_por_caracteristica (lista:list, clave:str):
    lista_auxiliar = []
    print("Color\t\t\t\tCantidad")
    print("----------------------------------------")
    for personaje in lista:
        lista_auxiliar.append(personaje[clave].capitalize())
    set_auxiliar = set(lista_auxiliar)
    for caracteristica in set_auxiliar:
        contador = 0 
        for personaje in lista:
            if caracteristica == personaje[clave].capitalize():
                contador += 1 
        if len(caracteristica) < 10:
            print(f"{caracteristica}\t\t\t\t{contador}")
        else:
            print(f"{caracteristica}\t\t\t{contador}")

def stark_normalizar_datos (lista:list):
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

"""1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
diccionario el cual representara a un héroe y también recibirá un string que
hace referencia a una “clave” del mismo
Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
llamada “nombre”. Caso contrario la función retornara un False"""

def obtener_dato(diccionario:dict, clave:str) -> bool:
    retorno = False
    if len(diccionario) != 0 and "nombre" in diccionario.keys():
        retorno = diccionario[clave]
        
    return retorno


"""Crear la función 'obtener_nombre" la cual recibirá por parámetro un diccionario el
cual representara a un héroe y devolverá un string el cual contenga su nombre
formateado de la siguiente manera:
Nombre: Howard the Duck
Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
contrario la función retornara un False"""

def obtener_nombre(superheroe):
    retorno = obtener_dato(superheroe, "nombre")
    if retorno != False:
        retorno = "Nombre: " + retorno

    return retorno
    

"""2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
diccionario el cual representara a un héroe y una key (string) la cual
representará el dato que se desea obtener.
     La función deberá devolver un string el cual contenga el nombre y dato
(key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
CUALQUIER OTRO DATO.
●   El string resultante debe estar formateado de la siguiente manera:
(suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
● Validar siempre que la lista no este vacía. Caso contrario la función
retornara un False
NOTA: Reutilizar las funciones del punto anterior"""

def obtener_nombre_y_dato(diccionario:dict, clave_a_obtener):
    retorno = False
    nombre = obtener_nombre(diccionario)
    clave = obtener_dato(diccionario, clave_a_obtener)

    if nombre != False and clave != False:
        retorno = f"{nombre} | {clave_a_obtener}: {clave}"

    return retorno

#print(obtener_nombre_y_dato(lista_personajes[0], "fuerza"))

"""3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
una key (string) la cual representará el dato al cual se le debe calcular su cantidad
MÁXIMA.
● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
un int o un float. Caso contrario la función retornara un False
● En caso de que el dato que se está buscando en el diccionario es de tipo int o
float retornar el mayor que haya encontrado en la búsqueda.
"""

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

#stark_normalizar_datos(lista_personajes)
#print(lista_personajes[0])

#print(obtener_maximo(lista_personajes, "fuerza"))


"""3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
una key (string) la cual representará el dato al cual se le debe calcular su cantidad
MÍNIMA.
● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
un int o un float. Caso contrario la función retornara un False
● En caso de que el dato que se está buscando en el diccionario es de tipo int o
float retornar el menor que haya encontrado en la búsqueda."""

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

#print(lista_personajes[0])
#print(obtener_minimo(lista_personajes, "fuerza"))


"""3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
● La lista de héroes
● Un número que me indique el valor a buscar (puede ser la altura
máxima, la altura mínima o cualquier otro dato)
● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan
con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
3.2
Ejemplo de llamada:
mayor_altura=obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
correspondiente a la altura máxima, y la misma función me podria servir tanto como
para altura menor, como la mayor o alguna altura que yo le especifique también.
3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:
● La lista de héroes
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
contrario no hará nada y retornara False
En caso de que la lista no este vacia imprimir la información completa de
todos los heroes de la lista que se le pase
"""
