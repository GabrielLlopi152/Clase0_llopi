from data_stark import lista_heroes
from os import system

'''Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú'''

def comparativa_mayor(diccionario:dict, clave:str, dato:str)->str:
    bandera = False
    for i in diccionario:
        for key in i.keys():
            if key == clave and  i['genero'] == dato:
                if bandera == False or float(i[key]) > altura_mayor:
                    altura_mayor = float(i[key])
                    nombre_heroe = i['nombre']
                    bandera = True
    return nombre_heroe

continuar = True

while continuar == True:

    print("Menu")
    print("A_Listado de superheroes NB")    #Listo
    print("B_Femenino más alta")            #Listo
    print("C_Masculino más alto")           #Listo
    print("D_Masculino más debil")          #LIsto
    print("E_NB mas debil")                 #listo
    print("F_NB fuerza promedio")
    print("G_Cantidad de heroes por cada color de ojos")
    print("H_Cantidad de heroes por color de pelo")
    print("I_Listado de heroes por color de ojos")
    print("J_Listado de superheroes por tipo de inteligencia")
    print("K_Salir del menu")

    opcion = input("Ingrese una letra: ")
    system('cls')

    match opcion:
        case 'A' | 'a': #Listado de superheroes NB
            for heroe in lista_heroes: #Recorremos cada heroe y verificamos su genero, si es NB imprimimos el nombre
                if heroe['genero'] == 'NB':
                    print(heroe['nombre'])

        case 'B' | 'b': #Femenino más alta
            nombre_heroe = comparativa_mayor(lista_heroes, 'altura', 'F')
            mensaje = "La heroina mas alta de todas es {0}".format(nombre_heroe)
            print(mensaje)

        case 'C' | 'c': #Masculino más alto
            nombre_heroe = comparativa_mayor(lista_heroes,'altura', 'M')
            mensaje = "El heroe masculino mas alto de todos es {0}".format(nombre_heroe)
            print(mensaje)
        
        case 'D' | 'd': #Masculino más debil
            bandera_primer_heroe = False
            for heroe in lista_heroes:
                for key in heroe.keys():
                    if key == 'fuerza' and heroe['genero'] == 'M':
                        if bandera_primer_heroe == False or int(heroe[key]) < fuerza_menor:
                            fuerza_menor = int(heroe[key])
                            nombre_heroe = heroe['nombre']
                            bandera_primer_heroe = True

            mensaje = "El heroe masculino mas debil de todos es {0}".format(nombre_heroe)
            print(mensaje)

        case 'E' | 'e': #NB mas debil
            bandera_primer_heroe = False
            for heroe in lista_heroes:
                for key in heroe.keys():
                    if key == 'fuerza' and heroe['genero'] == 'NB':
                        if bandera_primer_heroe == False or int(heroe[key]) < fuerza_menor:
                            fuerza_menor = int(heroe[key])
                            nombre_heroe = heroe['nombre']
                            bandera_primer_heroe = True

            mensaje = "El heroe no binario mas debil de todos es {0}".format(nombre_heroe)
            print(mensaje)

        case 'F' | 'f': #NB fuerza promedio
            suma_peso = 0
            contador = 0
            for dato in lista_heroes:
                for dato_key in dato.keys():
                    if dato_key == 'fuerza' and dato['genero'] == 'NB':
                        suma_peso += float(dato[dato_key])
                        contador += 1

            promedio = suma_peso / contador
            mensaje = "La cantidad de superheroes no binario son {0}, y la fuerza promedio es un total de {1}".format(contador, promedio)
            print(mensaje)

        case 'G' | 'g': #Cantidad de heroes por cada color de ojos
            lista_color_ojos = []
            for heroe in lista_heroes:
                lista_color_ojos.append(heroe['color_ojos'].capitalize())

            set_color_ojos = set(lista_color_ojos)
            for color in set_color_ojos:
                contador= 0
                for heroe in lista_heroes:
                    if color == heroe['color_ojos'].capitalize():
                        contador +=1
                print(f"{contador} de color {color}")

        case 'H' | 'h': #Cantidad de heroes por color de pelo
            lista_color_pelo = []
            for heroe in lista_heroes:
                if heroe['color_pelo'] != "":
                    lista_color_pelo.append(heroe['color_pelo'].capitalize())

            set_color_pelo = set(lista_color_pelo)
            for color in set_color_pelo:
                contador= 0
                for heroe in lista_heroes:
                    if color == heroe['color_pelo'].capitalize():
                        contador +=1
                print(f"{color}, cantidad = {contador}")

        case 'I' | 'i': #Listado de heroes por color de ojos
            diccionario_color_ojos= {}
            for heroe in lista_heroes:
                color = heroe['color_ojos']
                if color in diccionario_color_ojos:
                    diccionario_color_ojos[color] += " - " + heroe['nombre']
                else:
                    diccionario_color_ojos[color] = heroe['nombre']

            for color, conteo in diccionario_color_ojos.items():
                print(f"ojos: {color} \t \t heroes: {conteo}")

        case 'J' | 'j': #Listado de superheroes por tipo de inteligencia
            diccionario_nivel_inteligencia= {}
            for heroe in lista_heroes:
                inteligencia = heroe['inteligencia']
                if inteligencia != "":
                    if inteligencia in diccionario_nivel_inteligencia:
                        diccionario_nivel_inteligencia[inteligencia] += " - " + heroe['nombre']
                    else:
                        diccionario_nivel_inteligencia[inteligencia] = heroe['nombre']

            for inteligencia, conteo in diccionario_nivel_inteligencia.items():
                print(f"intelecto: {inteligencia} \t \t heroes: {conteo}")
                print("- - - - - - - - -")

        case 'K' | 'k': #Salir
            continuar = False
