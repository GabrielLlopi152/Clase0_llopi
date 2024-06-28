Edades = []

acumulador= 0
for i in range(5):
    edad = input("Ingrese una edad: ")
    edad = int(edad)
    Edades.append(edad)
    acumulador += edad

promedio = acumulador / len(Edades)

# i -> de 0 a 4      len(edades) -> cantidad de edades     edades[i] -> valor de edades

flag = False

'''for i in range(len(Edades)):
    if flag == False:
        edad_menor = Edades[i]
        edad_mayor = Edades[i]
        flag = True
    else:
        if Edades[i] > edad_mayor:
            edad_mayor = Edades[i]
        elif Edades[i] < edad_menor:
            edad_menor = Edades[i]'''

for edad in Edades:
    if flag == False:
        edad_menor = edad
        edad_mayor = edad
        flag = True
    else:
        if edad > edad_mayor:
            edad_mayor = edad
        elif edad < edad_menor:
            edad_menor = edad

for i in range(len(Edades)):

    print(Edades[i])

mensaje = "El mayor es {0}, el menor es {1}, y el promedio es de {2}".format(edad_mayor, edad_menor, promedio)
print(mensaje)

#Carga secuencial

'''nombres = ["A", "A", "A", "A", "A"]

for i in range (len(nombres)):
    nombre = input("Ingrese un nombre: ")
    nombres[i] = nombre

nombres[2] = "Burns"

for i in nombres:
    print(i)'''

#Carga aleatoria

'''nombres = ["A", "A", "A", "A", "A"]

for i in range (len(nombres)):
    nombre = input("Ingrese un nombre: ")
    indice = int(input("Ingrese el indice: "))

    while indice < 0 or indice > len(nombres) or nombres[indice] != "A":
        indice = int(input("Error, ingrese el indice: "))

    nombres[indice] = nombre

#nombres[2] = "Burns"

for i in nombres:
    print(i)
'''

#Carga mixta
"""
nombres = ["A", "A", "A", "A", "A"]

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
            if contador < (len(nombres)):
                for i in range (len(nombres)):
                    if nombres[i] == "A":
                        nombre = input("Ingrese un nombre: ")
                        nombres[i] = nombre
                        contador += 1
                        break
            else:
                print("Lo sentimos, espacio insuficiente")

        case 2:
            if contador != 0:
                for i in range (len(nombres)):
                    if nombres[i] != "A":
                        print(nombres[i])
            else:
                print("No se registraron nombres")

        case 3:
            nombre_baja = input("Ingrese el nombre que desea eliminar: ")
            indice = buscar(nombres, nombre_baja)
            if indice >= 0:
                mostrar(nombres, indice)
                respuesta = input("¿Está seguro que desea eliminar el contacto? [S | N]")
                while validar(respuesta) == False:
                    respuesta = input("¿Está seguro que desea eliminar el contacto? [S | N]")
                if respuesta == "S" or respuesta == "s":
                    nombres[i] = "A"
                    print("Contacto eliminado.")
                    contador -= 1
                else:
                    print("Contacto no eliminado.")
            else:
                print("No se encontró el contacto")
                        
        case 4:
            nombre_modificar = input("Ingrese el nombre que desea modificar: ")
            indice = buscar(nombres, nombre_modificar)
            #nombres[i] = input("Ingrese el nuevo nombre: ")
            if indice >= 0:
                mostrar(nombres, indice)
                respuesta = input("¿Está seguro que desea modificar el contacto? [S | N]")
                while validar(respuesta) == False:
                    respuesta = input("¿Está seguro que desea modificar el contacto? [S | N]")
                if respuesta == "S" or respuesta == "s":
                    respuesta = input("Ingrese el nuevo nombre: ")
                    nombres[i] = respuesta
                    print("Contacto modificado.")
            else:
                print("No se encontró el contacto")

        case 5:
            continuar = False

        case _:
            print("Numero ingresado incorrecto.")
"""