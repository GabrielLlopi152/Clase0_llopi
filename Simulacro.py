import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Llopi
---
Ejercicio: Simulacro
---
Enunciado:
Se desea desarrollar un programa que permita al usuario ingresar el nombre, año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015), si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        costo_juego_mayor = 1
        costo_juego_menor = 10000
        cantidad_juegos = 10
        suma_costos_juegos_online = 0
        contador_juegos_online = 0
        contador_juegos_offline = 0
        juego_entre_2000_y_2015 = False
        costo_menor_juego_entre_2000_y_2015 = 10000
        costo_mayor_juego_entre_2000_y_2015 = 1
        contador_juegos_antes_2000 = 0
        contador_juegos_entre_2000_2015 = 0
        contador_juegos_despues_2015 = 0
        juego_mas_barato_entre_2000_y_2015 = ""
        juego_mas_caro_entre_2000_y_2015 = ""

        for i in range (cantidad_juegos):
            nombre_juego = prompt(title= "Atención", prompt= "ingrese el nombre del juego")
            while nombre_juego == "" or None:
                prompt(title= "Atención", prompt= "ingrese su nombre del juego")

            año_emitido = int(prompt(title= "Atención", prompt= "ingrese el año del juego"))
            while año_emitido == None:
                año_emitido = int(prompt(title= "Atención", prompt= "ingrese el año del juego"))

            modo_juego = prompt(title= "Atención", prompt= "¿Es online u offline?").upper()
            while modo_juego != "ONLINE" and modo_juego != "OFFLINE":
                modo_juego = prompt(title= "Atención", prompt= "¿Es online u offline?").upper()

            costo_juego = int(prompt(title= "Atención", prompt= "ingrese el costo"))
            while (costo_juego < 500 or costo_juego > 10000) or costo_juego == None:
                costo_juego = int(prompt(title= "Atención", prompt= "ingrese el costo"))

            if costo_juego >= costo_juego_mayor:
                costo_juego_mayor = costo_juego
                juego_mas_caro = nombre_juego
            elif costo_juego <= costo_juego_menor:
                costo_juego_menor = costo_juego
                juego_mas_barato = nombre_juego

            if modo_juego == "ONLINE":
                contador_juegos_online += 1
                suma_costos_juegos_online += costo_juego
            else:
                contador_juegos_offline += 1

            if año_emitido >= 2000 and año_emitido <= 2015:
                contador_juegos_entre_2000_2015 += 1
                if juego_mas_barato_entre_2000_y_2015 == False:
                    juego_mas_barato_entre_2000_y_2015 = nombre_juego
                    juego_mas_barato_entre_2000_y_2015 = nombre_juego
                    juego_entre_2000_y_2015 = True
                else:
                    if costo_juego >= costo_mayor_juego_entre_2000_y_2015:
                        costo_juego_mayor = costo_juego
                        juego_mas_caro_entre_2000_y_2015 = nombre_juego
                    elif costo_juego <= costo_menor_juego_entre_2000_y_2015:
                        costo_juego_menor = costo_juego
                        juego_mas_barato_entre_2000_y_2015 = nombre_juego
            else:
                if año_emitido < 2000:
                    contador_juegos_antes_2000 += 1
                else:
                    contador_juegos_despues_2015 += 1

        if contador_juegos_antes_2000 > contador_juegos_entre_2000_2015 and contador_juegos_antes_2000 > contador_juegos_despues_2015:
            epoca_mayor_juegos = "Anterior al 2000"
        else:
             if contador_juegos_despues_2015 > contador_juegos_entre_2000_2015 and contador_juegos_despues_2015 > contador_juegos_entre_2000_2015:
                 epoca_mayor_juegos = "Después del 2015"
             else:
                 epoca_mayor_juegos = "Entre el 2000 y el 2015"


        #A
        mensaje_a = "El videojuego más caro de todos es {0}, mientras que el mas barato es {1}".format(juego_mas_caro, juego_mas_barato)
        print(mensaje_a)

        #B
        if contador_juegos_online >= 1:
            promedio_costos = suma_costos_juegos_online / contador_juegos_online
            mensaje_b = "El promedio de costos de juegos online es: ${0}".format(promedio_costos)
            print(mensaje_b)

        #C
        if juego_entre_2000_y_2015 == True:
            mensaje_c = ("el juego mas caro entre 2000 y 2015 es {0}, y el mas barato es {1}").format(juego_mas_caro_entre_2000_y_2015, juego_mas_barato_entre_2000_y_2015)
            print(mensaje_c)

        #D
        if contador_juegos_offline >= 1:
            porcentaje_juegos_offline = contador_juegos_offline * 100 / cantidad_juegos
            mensaje_d = ("El porcentaje de juegos offline es de {0}").format(porcentaje_juegos_offline)
            print(mensaje_d)

        #E
        mensaje_e = "El período con más videojuegos es {0}".format(epoca_mayor_juegos)
        print(mensaje_e)
        


            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
