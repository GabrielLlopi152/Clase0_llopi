from data_stark import lista_heroes
from os import system

'''
A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino 
NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
''' #FALTA HACER "E"
def contar_caracteres(variable:str)->int:
    contador = 0
    for letra in variable:
        contador += 1

    return contador
def convertir_mayuscula(variable:str)->str:
    cantidad = contar_caracteres(variable)
    retorno = ""    
    
    for i in range(cantidad):

        if ord(variable[i]) >= 97 and ord(variable[i]) <= 122:
            letra = chr(ord(variable[i])-32)               
            retorno += letra
        else:
            retorno += variable[i]
        
    return retorno

continuar = True

while continuar == True:
    print("Menu")
    print("A_Listado")
    print("B_Heroe con mayor fuerza")
    print("C_Heroe mas bajo")
    print("D_Peso promedio masculino")
    print("E_Heroes con mayor fuerza al promedio de la fuerza femenina")
    print("F_Salir del menu")

    opcion = input("Ingrese una letra: ")
    system('cls')

    match opcion:
       
        case "A":   #A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
            for dato in lista_heroes:
                for clave_dato in dato.items():
                    print(clave_dato[0] + " = " + clave_dato[1])
                print('- - - - - - - - - - - - - - -')

        case "B":   #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
            bandera_primer_heroe = False
            for dato in lista_heroes: #recorro los heroes
                for dato_key in dato.keys(): #recorro las claves de cada heroe

                    if dato_key == 'fuerza': #si la clave es fuerza
                        if bandera_primer_heroe == False or int(dato[dato_key]) > fuerza_mayor:
                            fuerza_mayor = int(dato[dato_key])
                            identidad_heroe = dato['identidad']
                            peso_heroe = dato['peso']
                            bandera_primer_heroe = True

            mensaje = "La identidad del heroe con mayor fuerza es {0}, y pesa un total de {1}kg".format(identidad_heroe,peso_heroe)
            print(mensaje)             

        case "C":   #C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
            bandera_primer_heroe = False
            for dato in lista_heroes:
                for dato_key in dato.keys():

                    if dato_key == 'altura':
                        if bandera_primer_heroe == False or float(dato[dato_key]) < altura_menor:
                            altura_menor = float(dato[dato_key])
                            nombre_heroe = dato['nombre']
                            identidad_heroe = dato['identidad']
                            bandera_primer_heroe = True

            mensaje = "La identidad del heroe con menor estatura se llama {0}, y su identidad es {1}".format(nombre_heroe,identidad_heroe)
            print(mensaje)

        case "D":    #D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
            suma_peso = 0
            contador = 0
            for dato in lista_heroes:
                for dato_key in dato.keys():
                    if dato_key == 'peso' and dato['genero'] == 'M':
                        suma_peso += float(dato[dato_key])
                        contador += 1

            promedio = suma_peso / contador
            mensaje = "La cantidad de superheroes masculinos son {0}, y el peso promedio es un total de {1}".format(contador, promedio)
            print(mensaje)

#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género)
#los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
        case "E":   
            total_fuerza_femenino = 0
            contador = 0
            for heroe in lista_heroes:
                if heroe['genero'] == 'F':
                    contador += 1
                    total_fuerza_femenino += int(heroe['fuerza'])
            fuerza_promedio_femenino = total_fuerza_femenino / contador

            for heroe in lista_heroes:
                if int(heroe["fuerza"]) > fuerza_promedio_femenino:
                    print("Nombre: " , heroe['nombre'],  "\t \t peso: " , heroe['peso'])
            '''mensaje= ' la fuerza promedio de las {0} mujeres es de {1}'.format(contador, fuerza_promedio_femenino)
            print(mensaje)'''
        case "F":
            continuar = False
        case _:
            pass 