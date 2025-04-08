#Lista paralela

def mostrar_datos(lista0:list, lista1:list, lista2:list): 
    for i in range(len(lista0)):
        if lista0[i] == "OCUPADO":
            print(lista1[i], lista2[i])
'''
estado = ["OCUPADO", "OCUPADO","OCUPADO",]
nombres = ["Pedro", "Ana", "Jose"]
edades = [23, 30, 18]

mostrar_datos(estado, nombres, edades)'''

#Listas anidadas

estado = ["OCUPADO", "OCUPADO","OCUPADO",]
nombres = ["Pedro", "Ana", "Jose"]
edades = [23, 30, 18]

personas = [["OCUPADO", "Pedro", 23, "M"] , ["OCUPADO", "Ana", 30, "F"] , ["OCUPADO", "Jose", 18, "M"]]

'''
for i in range(len(personas)):
    print(personas[i][0], personas[i][1])'''

'''for persona in personas:
    print(persona[0], persona[1])'''

def listar_lista_de_listas(lista:list):
    #Se recorre la lista
    for i in range(len(lista)):
        #seteo de variables
        mensaje = ""
        flag = False
        bandera_ocupado = True
        estado_ocupado = False

        #se recorre cada elemento (son otras listas) de la lista
        for j in range(len(lista[i])):
            #Se controla el primer elemento para verificar si es OCUPADO o LIBRE, para evitar imprimir ese dato
            if bandera_ocupado == True:
                bandera_ocupado = False
                #Corroboro que el elemento esté ocupado para mostrarlo en la segunda vuelta de j
                if lista[i][j] == "OCUPADO":
                    estado_ocupado = True
            #verifico que el estado esté ocupado en cada elemento de la lista general
            elif estado_ocupado == True:
                if type(lista[i][j]) == int:
                    (lista[i][j]) = str((lista[i][j]))
                if flag == False:
                    mensaje +=  lista[i][j]
                    flag = True
                #Separo el mensaje con espacios en blanco
                else: 
                    mensaje += " " + lista[i][j]
        #Imprimo unicamente los espacios ocupados
        if estado_ocupado == True:  
            print(mensaje)

listar_lista_de_listas(personas)