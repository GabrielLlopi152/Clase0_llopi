'''nombre = "Dairon"

print(nombre)

for i in range(len(nombre)):
    print(nombre[i])
'''
nombres= ["Maia", "Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
numeros = [[20, 19, 21, 25], [23, 24, 26, 22]]
matriz = [[2, 1, 3, 7], [5, 8, 4, 6]]

#ORDENAMIENTO DE FILAS EN UNA MATRIZ

'''print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])-1):
        for k in range(j+1, len(matriz[i])):
            if matriz[i][j] > matriz[i][k]:
                auxiliar = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = auxiliar
            #print(f"i:{i}, j:{j}, k:{k}")

print(matriz)
'''

'''for i in range(len(nombres)):
    for j in range(len(nombres[i])):
        print(nombres[i][j])'''

'''bandera = False

for i in range(len(numeros)):
    
    for j in range(len(numeros[i])):
        if bandera == False:
            minimo = numeros[i][j]
            maximo = numeros[i][j]
            bandera = True
        else:
            if numeros[i][j] > maximo:
                maximo = numeros[i][j]
            elif numeros[i][j] < minimo:
                minimo = numeros[i][j]
            
print(maximo, minimo)'''

print(matriz)
for i in range((len(matriz)+1) * len(matriz)):
    for j in range((len(matriz)+1) * len(matriz)+1):
        for k in range(j+1, len(matriz[i])):
            if matriz[i][j] > matriz[i][k]:
                auxiliar = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = auxiliar
            print(f"i:{i}, j:{j}, k:{k}")

print(matriz)