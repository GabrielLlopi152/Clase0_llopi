from os import system
from data_stark import lista_heroes


'''0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
lista de héroes. La función deberá:
● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
las keys que representan datos numéricos) por ejemplo fuerza (int),
altura (float), etc
● Validar primero que el tipo de dato no sea del tipo al cual será
casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
verificar antes que no se encuentre ya en ese tipo de dato.
● Si al menos un dato fue modificado, la función deberá retornar el valor
booleano True
● En caso de que la lista esté vacía o ya se hayan normalizado
anteriormente los datos se deberá retornar el valor booleano False
● Crear una opción en el menú que me permita normalizar los datos (No
se debería poder acceder a ninguna otra opción del menú hasta que
los datos esten normalizados)
● En caso de que la llamada a la función retorne True mostrar un
mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
“Hubo un error al normalizar los datos. Verifique que la lista no este
vacía o que los datos ya no se hayan normalizado anteriormente”'''

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

def obtener_dato(diccionario:dict, clave:str):
    retorno= False
    for key in diccionario:
        if len(diccionario) != 0 and "nombre" in diccionario.keys():
            retorno= diccionario[clave]

    return retorno

#print(obtener_dato(lista_heroes[5],'nombre'))

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

#print(obtener_nombre(lista_heroes[1]))

def obtener_nombre_y_dato(diccionario:dict, clave_a_obtener):
    retorno = False
    nombre = obtener_nombre(diccionario)
    clave = obtener_dato(diccionario, clave_a_obtener)

    if nombre != False and clave != False:
        retorno = f"{nombre} | {clave_a_obtener}: {clave}"

    return retorno

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

    