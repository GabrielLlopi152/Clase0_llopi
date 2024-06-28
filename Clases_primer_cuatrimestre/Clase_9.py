generos = ["F", "F", "M", "F", "M", "M", "M", "F"]
nombres = ["Maia", "Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
edades = [20, 19, 21, 25, 23, 24, 26, 22]
apellidos = ["Garcia", "Lopez", "Lima", "Garcia", "Martino", "Lopez", "Martino", "Grandon"]

for i in range(len(generos)):
    print(generos[i] + " " + apellidos[i] + " " + nombres[i] + " " + str(edades[i]))

for i in range(len(generos)):
    for j in range(len(generos)):
        if (generos[i] < generos[j]) or (generos[i] == generos[j] and nombres[i] < nombres[j]) or (generos[i] == generos[j] and nombres[i] == nombres[j] and edades[i] < edades[j]):
            auxiliar = generos[i]
            generos[i] = generos[j]
            generos[j] = auxiliar

            auxiliar = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = auxiliar

            auxiliar = edades[i]
            edades[i] = edades[j]
            edades[j] = auxiliar

            auxiliar = apellidos[i]
            apellidos[i] = apellidos[j]
            apellidos[j] = auxiliar
        
print("")

for i in range(len(generos)):
    print(generos[i] + " " + apellidos[i] + " " + nombres[i] + " " + str(edades[i]))
