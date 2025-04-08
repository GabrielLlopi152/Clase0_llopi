import json
from data_stark import lista_heroes

'''1.1. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornara un string con la información del mismo.

1.2. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir
Se creó el archivo: nombre_archivo.csv

1.3. Crear la función generar_csv()
La función va a recibir el nombre y extensión del archivo csv de los
superhéroes (Puede ser ruta absoluta o relativa) y la lista de los
mismos.
Si la lista no está vacía la función deberá guardar en un string la
información en formato csv (separado con comas) con la cabecera
correspondiente.
Una vez generado el string debería usar la función de 1.2 para guardar
ese string generado al archivo.
Si la lista está vacia retornar False

1.4. Crear la función leer_csv() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa)
La función se tiene que encargar de generar una lista de superhéroes
en base al contenido de ese archivo csv que se le paso. Pueden usar
la cabecera de ese csv para generar las claves de cada uno de los
diccionarios.
La función debe retornar la lista de diccionarios si es que existe el
archivo y sino False.

1.5. Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista. (Hecho en la clase pasada!!!!)

1.6. Crear la función leer_json() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el
nombre de la lista a leer por ejemplo en la imagen anterior la lista está
en la clave “heroes”
Si el archivo existe deberia leer el archivo json y retornar la lista
obtenida.
'''


'''1.1. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornara un string con la información del mismo.'''

def leer_archivo(archivo_nombre:str):
    contenido = False
    if len(archivo_nombre) != 0:
        with open(archivo_nombre, 'r') as file:
            contenido = file.read()
        return contenido

#print(leer_archivo('texto.txt'))

'''1.2. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir
Se creó el archivo: nombre_archivo.csv'''

def guardar_archivo(nombre_archivo:str, contenido_archivo:str):
    retorno= False
    if len(nombre_archivo) != 0 and len(contenido_archivo) != 0:
        with open(nombre_archivo, 'w') as file:
            file.write(contenido_archivo)
            retorno = 'Se creó el archivo: ' + nombre_archivo
    return retorno

#print(guardar_archivo('archivo_prueba.txt', 'HOLA MUNDO'))

'''1.3. Crear la función generar_csv()
La función va a recibir el nombre y extensión del archivo csv de los
superhéroes (Puede ser ruta absoluta o relativa) y la lista de los
mismos.
Si la lista no está vacía la función deberá guardar en un string la
información en formato csv (separado con comas) con la cabecera
correspondiente.
Una vez generado el string debería usar la función de 1.2 para guardar
ese string generado al archivo.
Si la lista está vacia retornar False'''

def generar_csv(nombre_archivo:str, lista:list):
    retorno = False
    all_keys = ''
    datos = ''
    if len(lista) != 0:
        for key in lista[0].keys():
            all_keys += key + ','
        all_keys += '\n'
        for personaje in lista:
            for dato in personaje.values():
                datos += dato + ','
            datos += '\n'
        guardar_archivo(nombre_archivo, all_keys + datos)
    else:
        return False

#generar_csv('a.csv', lista_heroes)

'''1.4. Crear la función leer_csv() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa)
La función se tiene que encargar de generar una lista de superhéroes
en base al contenido de ese archivo csv que se le paso. Pueden usar
la cabecera de ese csv para generar las claves de cada uno de los
diccionarios.
La función debe retornar la lista de diccionarios si es que existe el
archivo y sino False.'''

def leer_csv(nombre_archivo:str):
    lista = []
    lista_final = []
    diccionario = {}
    with open(nombre_archivo, 'r') as file:
        lista_lineas = file.readlines() #forma una lista de strings y se guardan en una variable
        for i in range(len(lista_lineas)):
            lista_lineas[i] = lista_lineas[i].replace(',\n', '')
            if i == 0:
                keys = lista_lineas[i].split(',')
            else:
                lista.append(lista_lineas[i].split(','))

        for i in range (len(lista)):
            for j in range(len(lista[i])):
                diccionario.update({keys[j] : lista[i][j]})
        lista_final.append(diccionario)
        
    return lista_final

print(leer_csv('a.csv'))

'''1.5. Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista. (Hecho en la clase pasada!!!!)'''

def generar_json(nombre:str, lista:list, clave:str):
    data = {clave: lista}

    with open(nombre, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False) 

'''1.6. Crear la función leer_json() que va a recibir el nombre y extensión de
donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el
nombre de la lista a leer por ejemplo en la imagen anterior la lista está
en la clave “heroes”
Si el archivo existe deberia leer el archivo json y retornar la lista
obtenida.'''

def leer_json (nombre_archivo, key):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
    return (data[key])

'''2. Segunda Parte
2.1. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera ascendente
2.2. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera descendente.
2.3. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza). Preguntar al usuario si lo quiere
ordenar de manera ascendente (‘asc’) o descendente (‘desc’) (reutilizar
funciones anteriores dependiendo del caso)

(TODO ESTO YA LO TIENE RESUELTO)

3. Desarrollar los siguientes puntos (usando el data_stark.py) -> Se deben
desarrollar funciones extra dependiendo de la situación o reutilizar funciones
anteriores como normalizar o listar.
● 1-Normalizar datos (No debe dejar de entrar a las otras opciones)
● 2-Generar CSV (Guardar la lista generada en otra variable)
● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el
mismo existe)
● 4-Generar JSON (Guardar la lista generada en otra variable)

● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si
el mismo existe)
● 6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si
ordenar de manera ASC o DESC
● 7-Salir'''

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

def swap(lista:list, dato_a, dato_b):
    auxiliar = lista[dato_a]
    lista[dato_a] = lista[dato_b]
    lista[dato_b] = auxiliar
    return lista

def ordenar_array(lista:list, criterio:str = "ASC")-> list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if criterio == "ASC" and lista[i] > lista[j] or criterio == "DESC" and lista[i] < lista [j]:
                swap(lista, i, j)
    return lista


'''2. Segunda Parte
2.1. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera ascendente
2.2. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza) de manera descendente.
2.3. Crear una función para ordenar héroes por alguna de las claves
númericas (altura, peso y fuerza). Preguntar al usuario si lo quiere
ordenar de manera ascendente (‘asc’) o descendente (‘desc’) (reutilizar
funciones anteriores dependiendo del caso)'''

def ordenar(lista:list, clave:str, ascendente:bool=True)->list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if ascendente and lista[i][clave] > lista[j][clave] or ascendente == False and lista[i][clave] < lista [j][clave]:
                swap(lista, i, j)
    return lista

stark_normalizar_datos(lista_heroes)

print(ordenar(lista_heroes, 'peso', False))
