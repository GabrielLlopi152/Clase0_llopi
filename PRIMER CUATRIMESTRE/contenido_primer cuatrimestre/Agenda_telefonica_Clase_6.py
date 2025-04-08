from os import system

def listar(lista_1:list, lista_2:list, lista_3:list): #3
    for i in range(len(lista_1)):
        if lista_1[i] == "OCUPADO":
            mostrar(lista_2, lista_3, i)

def mostrar(lista:list, lista_2:list, indice:int): #2
   '''
   Recibe dos listas y un mismo indice.
   Imprimirá los datos que estén en el indice de ambas listas.
   ''' 
   mensaje = "{0}_ Nombre: {1}, {2} años".format(indice+1, lista[indice], lista_2[indice])
   print(mensaje)

def buscar(lista:list, dato:str)->int:
    '''
    La funcion busca el dato en una lista.
    Si es encontrado, retornará su índice.
    En caso contrario, retornará -1. 
    '''
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

def validar(respuesta:str)->bool:
    '''
    Recibe un dato y corrobora que sea lo solicitado.
    Devolverá True en caso de ser valido.
    En caso contrario, devolverá False
    '''
    validacion = False
    if respuesta == "S" or respuesta == "N" or respuesta == "s" or respuesta == "n":
        validacion = True
    return validacion

def buscar_libre(lista:list, espacio_libre:str)->int:
    '''
    Busca un espacio libre en la lista ingresada
    Retornará el indice del primer espacio libre que encuentre.
    '''
    retorno = -1
    for i in range (len(lista)):
        if lista[i] == espacio_libre:
            retorno = i
            break
    return retorno

def lista_vacia(lista:list, espacio_libre:str)->bool:
    '''
    Recibe una lista y el caracter que representa su espacio libre.
    Si la lista está vacía, devolverá un booleano True
    En caso contrario, devuelve False
    '''
    retorno= True
    for i in range(len(lista)):
        if lista[i] != espacio_libre:
            retorno= False
            break
    return retorno

def alta(mensaje:str)->str:
    '''
    Recibe un comentario para que el usuario introduzca el dato necesario.
    Retorna el dato que ingrese el usuario.
    '''
    dato = input(mensaje)
    return dato

nombres = ["A", "A", "A", "A", "A"]
Estado = ["LIBRE","LIBRE","LIBRE","LIBRE","LIBRE"]
edad = ["A", "A", "A", "A", "A"]

continuar = True
contador = 0

while continuar == True:
    print("Menu")
    print("1_Alta")
    print("2_Lista")
    print("3_Baja")
    print("4_Modificar")
    print("5_Salir")

    opcion = int(input("Ingrese un numero: "))
    system("cls")

    match opcion:
        case 1:
            indice = buscar_libre(Estado, "LIBRE")
            if indice >= 0:
                nombres[indice] = alta('Ingrese el nombre: ')
                edad[indice] = alta('Ingrese la edad: ')
                Estado[indice] = "OCUPADO"
            else:
                print("Lo sentimos, espacio insuficiente")

        case 2:
            if lista_vacia(Estado, "LIBRE") == False:
                listar(Estado, nombres, edad)
            else:
                print("No se registraron nombres")

        case 3:
            
            if lista_vacia(Estado, "LIBRE") == False:
                nombre_baja = input("Ingrese el nombre que desea eliminar: ")
                indice = buscar(nombres, nombre_baja)
                if indice >= 0:
                    mostrar(nombres, edad, indice)
                    respuesta = input("¿Está seguro que desea eliminar el contacto? [S | N]")
                    while validar(respuesta) == False:
                        respuesta = input("¿Está seguro que desea eliminar el contacto? [S | N]")
                    if respuesta == "S" or respuesta == "s":
                        Estado[indice] = "LIBRE"
                        nombres[indice] = "A"
                        edad[indice] = "A"
                        print("Contacto eliminado.")
                    
                    else:
                        print("Contacto no eliminado.")
            else:
                print("No se encontró el contacto")
                        
        case 4:
            if lista_vacia(Estado, "LIBRE") == False:
                nombre_modificar = input("Ingrese el nombre que desea modificar: ")
                indice = buscar(nombres, nombre_modificar)
                if indice >= 0:
                    mostrar(nombres, edad, indice)
                    respuesta = input("¿Está seguro que desea modificar el contacto? [S | N]")
                    while validar(respuesta) == False:
                        respuesta = input("¿Está seguro que desea modificar el contacto? [S | N]")
                    if respuesta == "S" or respuesta == "s":
                        respuesta = input("Ingrese el nuevo nombre: ")
                        nombres[indice] = respuesta
                        print("Contacto modificado.")
            else:
                print("No se encontró el contacto")

        case 5:
            continuar = False

        case _:
            print("Numero ingresado incorrecto.")


'''
Alta verifica estado libre, luego ingresa nombre y edad
Listar muestra solo ocupados con nombre y edad
Baja verifica 
Modificar solo nombre y edad
'''

#Agenda telefonica, se debe ingresar gente con su nombre y edad, cada uno ocupará un espacio (maximo 5 personas).
#En listar solo se debe ver los espacios ocupados, y debe imprimir su nombre y edad correspondiente
#Baja elimina nombre y edad, y cambia el espacio a libre
#Modificar cambia solo nombre y edad del espacio