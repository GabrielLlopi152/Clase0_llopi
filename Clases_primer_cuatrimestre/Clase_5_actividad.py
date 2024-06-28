import random
'''
1) Crear una lista de entre 10 a 15 numeros, todos los numeros tienen que ser aleatorios
2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera([indice] valor)
3) Determinar cual es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice]valor)
4) Determinar cual es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice]valor)
5) Determinar el promedio

Usar funciones con nombres claros
'''
#1) Crear una lista de entre 10 a 15 numeros, todos los numeros tienen que ser aleatorios

def crear_lista_aleatoria(tope):
    numeros = []

    for i in range (tope):
        numeros.append(random.randint(0,100))
    return numeros

#print(crear_lista_aleatoria(10))

lista = crear_lista_aleatoria(10)

#2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera([indice] valor)

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(f"([{i+1}], {lista[i]})")

#mostrar_lista(lista)

#3) Determinar cual es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice]valor)

def definir_valor_maximo(lista):
    numero_max = lista[0]
    for i in range(len(lista)):
        if lista[i] > numero_max:
            numero_max = lista[i]

    return numero_max

def definir_indice_maximo(lista):
    numero_max = lista[0]
    for i in range(len(lista)):
        if lista[i] > numero_max:          
            indice_maximo = i    

    return indice_maximo

def mostrar_informacion_maximo(indice, valor):
    print(f"([{indice}], {valor})")

#valor = definir_valor_maximo(lista)
#indice = definir_indice_maximo(lista)

#print(lista)
#mostrar_informacion_maximo(indice, valor)

#4) Determinar cual es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice]valor)

def definir_valor_minimo(lista):
    numero_min = lista[0]
    for i in range(len(lista)):
        if lista[i] < numero_min:
            numero_min = lista[i]

    return numero_min

def definir_indice_minimo(lista):
    numero_min = lista[0]
    for i in range(len(lista)):
        if lista[i] < numero_min:          
            indice_minimo = i    

    return indice_minimo

def mostrar_informacion_minimo(indice, valor):
    print(f"([{indice}], {valor})")


#valor = definir_valor_minimo(lista)
#indice = definir_indice_minimo(lista)

print(lista)
#mostrar_informacion_minimo(indice, valor)

#5) Determinar el promedio

def sumar_numeros(lista):
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    
    return acumulador

def promediar_numeros(lista):
    contador = 0
    acumulador = sumar_numeros(lista)

    for i in range(len(lista)):
        contador += 1
    resultado = acumulador / contador

    return resultado


sumar_numeros(lista)
print(promediar_numeros(lista))