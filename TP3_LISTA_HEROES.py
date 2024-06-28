from data_stark import lista_heroes
from os import system
from stark_biblioteca import *



continuar = True

while continuar == True:

    print("Menu")
    print("A_Listado de superheroes NB")    
    print("B_Femenino más alta")
    print("C_Masculino más alto")
    print("D_Masculino más debil")
    print("E_NB mas debil")          
    print("F_NB fuerza promedio")
    print("G_Cantidad de heroes por cada color de ojos")
    print("H_Cantidad de heroes por color de pelo")
    print("I_Listado de heroes por color de ojos")
    print("J_Listado de superheroes por tipo de inteligencia")
    print("K_Salir del menu")

    opcion = input("Ingrese una letra: ")
    system('cls')

    match(opcion.capitalize):
        case 'A'| 'a':
            pass
        case 'B'| 'b':
            pass
        case 'C'| 'c':
            pass
        case 'D'| 'd':
            pass
        case 'E'| 'e':
            pass
        case 'F'| 'f':
            pass
        case 'G'| 'g':
            pass
        case 'H'| 'h':
            pass
