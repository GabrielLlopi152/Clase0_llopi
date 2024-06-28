import random
Usuario = ['Gabriel', 'Llopi', 19, 'argentino']


#for i in Usuario:
#    print (i)

#for i in range(len(Usuario)):
#    print(Usuario [i])

Usuario.append('videojuegos')

def mostrar_datos (lista):
    for i in range(len(lista)):
        print(lista[i])

numeros = []
for numero in range(10):
    numeros.append(random.randint(1,1000))

#Es una carga secuencial

def buscar_dato(lista, indice):
    dato = False
    if indice >= 0 and indice < len(lista):
        dato = lista[indice]
    return dato

#print(buscar_dato(Usuario, 3))


'''
contador= 0
for i in range(len(enteros)):
    if enteros[i-contador] == 5:
        enteros.pop(i-contador)
        contador += 1
mostrar_datos(enteros)

lista_auxiliar = []

for i in enteros:
    if enteros != 5:
        lista_auxiliar.append(i)
        
mostrar_datos (lista_auxiliar)
'''
enteros = [2,1,5,4,6,9,3]
lista_ordenada = []
minimo = False

for i in range (len(enteros)):
    num_minimo = enteros[i]
    for j in range (len(enteros)):
        if enteros[j] < num_minimo:
            num_minimo= enteros[j]
    lista_ordenada.append(num_minimo)

mostrar_datos(lista_ordenada)
