'''lista= [3, 8, 1, 5, 4]

lista.sort()

print(lista)

lista_2= ["pedro", "alva", "zacarias", "monica"]

lista_2.sort()

print(lista_2)'''

#65 = A
#97 = a

#2'7 2'6 2'5 2'4 2'3 2'2 2'1 2'0
#128 64 32 16 8 4 2 1
#0   1  0  0  0 0 0 1


#128 64 32 16 8 4 2 1
#0   1  1  0  0 0 0 1

#0100 0001
#0110 0001
 
#print(bin(ord("a")))

lista= [3, 8, 1, 5, 4]
lista_2= ["pedro", "alva", "zacarias", "monica"]

#ASCENDENTE
#letras: A a z
#numeros: 0 a 9

#DESCENDENTE
#letras: z a A
#numeros: 9 a 0

'''def ordenar_ascendente(lista:list):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista [j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista

lista_cambiada = ordenar_ascendente(lista)
print(lista_cambiada)'''

def swap(lista:list, dato_a, dato_b):
    auxiliar = lista[dato_a]
    lista[dato_a] = lista[dato_b]
    lista[dato_b] = auxiliar
    return lista

def ordenar_array(lista:list, criterio:str = "ASC")-> list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if criterio == "ASC" and lista[i] > lista[j] or criterio == "DESC" and lista[i] < lista [j]:
                #swap
                #auxiliar = lista[i]
                #lista[i] = lista[j]
                #lista[j] = auxiliar
                swap(lista, i, j)
    return lista

print(ordenar_array(lista))
print(ordenar_array(lista, "DESC"))
