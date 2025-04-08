'''
Apellido y nombre: Llopi Gabriel
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion 1
Instancia: Primer examen parcial
'''

from os import system
from agencia_vuelos_biblioteca import *
import json
'''
De una agencia de vuelos se tienen los siguientes datos: 
 Id (debe comenzar en 1 y ser autoincremental) 
 Aerolínea (AA, LATAM o IBERIA) 
 Apellido_Nombre_Pasajero (Hasta de 30 caracteres) 
 DNI_Pasajero 
 Precio (Entre 500.000 y 2.000.000) 
 Origen (Buenos Aires, Madrid, París, Miami, Roma o Tokio) 
 Destino (Buenos Aires, Madrid, París, Miami, Roma o Tokio) 
 Clase (Turista o Ejecutivo) 
 Fecha (formato AAAAMMDD)

A- Cargar el archivo data.json. 
Luego de la carga del archivo, realizar un menú de opciones que realice lo siguiente en 
memoria: 
Realizar un menú de opciones que realice lo siguiente: 
B- Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)]. 
C- Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
tipo y dato a modificar”). 
D- Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
baja correspondiente. 
E- Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: 
Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre
F- Hacer un submenú que realice lo siguiente:
1) Listar por pantalla los pasajes de menor y mayor precio.
2) Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el
usuario por consola.
3) Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente
(‘asc’) o descendente („desc‟). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble
sort (burbujeo).
4) Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.
5) Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1. 
G Hacer un submenú que realice lo siguiente:
1) Listar por pantalla los pasajes de una aerolínea determinada. El usuario deberá ingresar por consola la Aerolínea.
2) Listar por pantalla todos los pasajes de una clase y destino determinados. El usuario deberá ingresar por consola la Clase y el Destino.
H) Salir

Nota 0: No se podrá acceder a ningún ítem del menú, sin antes haber cargado el archivo. En tal sentido, realizar la 
validación correspondiente. 
Nota 1: Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por 
consola. Cada ítem del menú deberá ser una función. 
Nota 2: Se deberá desarrollar biblioteca y funciones propias. 
Nota 3: El set de datos proviene de un json. 
Nota 4: Utilizar las funciones propias desarrolladas durante la cursada en lugar de los métodos o funciones propias 
del lenguaje.
'''

continuar = True
json_cargado = False
bandera_crear_csv = False
bandera_crear_json = False
lista_pasajero_precio = []

while continuar == True:

    print('')
    print("Menu - Registro de vuelos de la empresa Llopi")
    print("A_Cargar archivo json")
    print("B_Alta") 
    print("C_Modificar")
    print("D_Baja")   
    print("E_listar")
    print("F_submenu + submenu 2")
    print("G_Salir")

    opcion = input("Ingrese una letra: ")
    system('cls')

    if json_cargado == False:
        lista_vuelos = A_cargar_json(opcion)
        json_cargado = True

    else:
        match opcion:

            case 'B' | 'b':
                B_alta(lista_vuelos)
            case 'C' | 'c':
                C_modificar(lista_vuelos)
            case 'D' | 'd':
                lista_vuelos = D_baja(lista_vuelos)
            case 'E'| 'e':
                E_listar(lista_vuelos)
            case 'F'| 'f':

                submenu_activo = True
                while submenu_activo:
                    existe_pasaje = False

                    print(' ')
                    print("Menu")
                    print("1_Listar el pasaje de mayor o menor precio")
                    print("2_Mostrar pasajes por destino") 
                    print("3_listar pasajes segun fecha")
                    print("4_Exportar a json")
                    print("5_Exportar a csv")
                    print("6_Listar pasajes por aerolinea")
                    print("7_Listar pasajes por clase y destino")
                    print("8_Salir")
                    
                    ''' 1) Listar por pantalla los pasajes de una aerolínea determinada. El usuario deberá ingresar por consola la Aerolínea.
                    2) Listar por pantalla todos los pasajes de una clase y destino determinados. El usuario deberá ingresar por consola la Clase y el Destino.'''

                    opcion = input("Seleccione lo que desea modificar: ")
                    system('cls')
                    match opcion:

                        case '1':
                            opcion = input('mayor | menor: ')
                            while opcion != 'mayor' and opcion != 'menor':
                                opcion = input('mayor | menor: ')

                            bandera = False
                            for pasajero in lista_vuelos:
                                if opcion.lower() == 'mayor':
                                    if bandera == False or float(pasajero['Precio']) > float(mayor_precio):
                                        bandera = True
                                        mayor_precio = float(pasajero['Precio'])
                                        pasajero_precio = pasajero
                                elif opcion.lower() == 'menor':
                                    if bandera == False or float(pasajero['Precio']) < float(menor_precio):
                                        bandera = True
                                        menor_precio = float(pasajero['Precio'])
                                        pasajero_precio = pasajero

                            mensaje = 'El viaje con {0} precio es {1}'.format(opcion, pasajero_precio)
                            print(mensaje)
                            lista_pasajero_precio.append(pasajero_precio)
                            bandera_crear_csv = True
                            
                        case '2':
                            contador = 0
                            destino_ingresado = input('Introduzca el destino (buenos aires | roma | tokio | paris | miami | madrid): ')
                            for pasajero in lista_vuelos:
                                if pasajero['Destino'].upper() == destino_ingresado.upper():
                                    contador += 1
                            mensaje = 'El total de pasajes con destino a {0} es de {1}'.format(destino_ingresado, contador)
                            print(mensaje)

                        case '3':
                            opcion = input('asc | desc: ')
                            while opcion != 'asc' and opcion != 'desc':
                                opcion = input('asc | desc: ')
                            ordenar_lista_diccionarios(lista_vuelos,'Fecha', opcion)

                            lista_ordenada = ['Fecha','Aerolinea','Clase','Origen','Destino','Precio', 'DNI_Pasajero','Apellido_Nombre_Pasajero']
                            encabezado = ''
                            for dato in lista_ordenada:
                                encabezado += '|'
                                dato = rellenar_bytes(dato)
                                encabezado += dato    
                            print(encabezado) 

                            for pasajero in lista_vuelos:
                                mensaje = ''
                                for dato in lista_ordenada:
                                    mensaje+= '|'
                                    mensaje += rellenar_bytes(pasajero[dato])
                                print(mensaje)
                            bandera_crear_json = True

                        case '4':
                            if bandera_crear_json:
                                data = {'pasajeros': lista_vuelos}
                                actualizar_json('archivo_parcial.json', data)
                            else:
                                print('Realice la operación "3" primero')

                        case '5':
                            if bandera_crear_csv:
                                generar_csv('archivo_parcial.csv', lista_pasajero_precio)
                                print('Se ha exportado con exito')
                            else:
                                print('Realice la operación "1" primero')

                        case '6':
                            lista_nueva = []

                            nombre_aerolinea = alta('Introduzca la aerolinea (LATAM | AA | IBERIA): ')
                            while nombre_aerolinea.upper() != 'LATAM' and nombre_aerolinea.upper() != 'AA' and nombre_aerolinea.upper() != 'IBERIA':
                                nombre_aerolinea = alta('Introduzca la aerolinea (LATAM | AA | IBERIA): ')

                            for pasajeros in lista_vuelos:
                                if pasajeros["Aerolinea"] == nombre_aerolinea.upper():
                                    lista_nueva.append(pasajeros)

                            E_listar(lista_nueva)

                        case '7':
                            lista_nueva = []

                            clase = alta('turista | ejecutivo: ')
                            while clase.upper() != 'TURISTA' and clase.upper() != 'EJECUTIVO':
                                clase = alta('turista | ejecutivo: ')

                            destino_vuelo = alta('Introduzca el destino del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')
                            while destino_vuelo.upper() != 'BUENOS AIRES' and destino_vuelo.upper() != 'ROMA' and destino_vuelo.upper() != 'TOKIO' and destino_vuelo.upper() != 'PARIS' and destino_vuelo.upper() != 'MIAMI' and destino_vuelo.upper() != 'MADRID':
                                destino_vuelo = alta('Introduzca el destino del vuelo (buenos aires | roma | tokio | paris | miami | madrid): ')
                            
                            for pasajeros in lista_vuelos:
                                if pasajeros["Clase"] == clase.capitalize() and pasajeros["Destino"].capitalize() == destino_vuelo.capitalize():
                                    lista_nueva.append(pasajeros)
                                    existe_pasaje = True
                                
                            if existe_pasaje:
                                E_listar(lista_nueva)
                            else:
                                mensaje = 'No existe ningún pasaje con clase "{0}" y destino a {1}'.format(clase,destino_vuelo)
                                print(mensaje)

                        case '8':
                            submenu_activo = False
                
            case 'G'| 'g':
                continuar = False
