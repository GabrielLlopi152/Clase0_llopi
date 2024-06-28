#hacer listado ordenado por sexo, y si hay igualdad que se ordene con orden alfabetico

Personas = [["M", "Gabriel", 19],["M", "Sam", 20],["F", "Ellie", 32],["F", "Claudia", 20],["M", "Nathan", 36],["F", "Zoe", 17],["F", "Miranda", 19],["M", "Lisandro", 23]]

for i in range(len(Personas)): #Recorro cada persona 
    for j in range(len(Personas)): #recorro nuevamente para hacer comparaciones

        if Personas[j][0] == "F" and j > i:   #si es MUJER, y está despues del usuario N° i:
                auxiliar = Personas[i]
                Personas[i] = Personas[j]
                Personas[j] = auxiliar

print("Ordenado por sexo: ", Personas)
print("")

#TERMINADO EL ORDENAMIENTO POR SEXO

contador_f = 0
contador_m = 0
for persona in range(len(Personas)): #Hago un conteo de la lista
    if Personas[persona][0] == "F":
       contador_f += 1
    else:
        contador_m += 1

total = contador_f + contador_m

#TERMINADO EL CONTEO

if contador_f >= 2: #Si hay 2 o mas mujeres en la lista, procedo a ordenarlos alfabeticamente
    contador_break = 0

    for i in range(len(Personas)): #Recorro nuevamente para hacer comparaciones
        contador_break += 1
        for j in range(len(Personas)):

            if bin(ord(Personas[j][1][0])) >= bin(ord(Personas[i][1][0])): #Recojo la primer letra del nombre de la persona y comparo binarios
                    auxiliar = Personas[i]
                    Personas[i] = Personas[j]
                    Personas[j] = auxiliar
        
        if contador_break == contador_f:
            break

elif contador_m >= 2: #Si hay 2 o mas hombres en la lista, procedo a ordenarlos alfabeticamente
    contador_break = 0

    for i in range(contador_f, total): #Recorro nuevamente para hacer comparaciones              
        contador_break += 1
        for j in range(contador_f, total):

            if bin(ord(Personas[j][1][0])) >= bin(ord(Personas[i][1][0])): #Recojo la primer letra del nombre de la persona y comparo binarios
                    auxiliar = Personas[i]
                    Personas[i] = Personas[j]
                    Personas[j] = auxiliar
        
        if contador_break == contador_m:
            break

print("Ordenado por sexo y nombre: ", Personas)
        
'''
Falta corregir ordenamiento por NOMBRES MASCULINO
'''     


