def sumar(numero_a, numero_b):
    resultado = numero_a + numero_b
    return resultado

#numero = sumar(43,57)
#print (numero)

'''
Funciones Parte I

1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

2. Crear una función que verifique si un número dado por argumento es par o impar. 
   La función debe imprimir un mensaje indicando si el número es par o impar.
   
3. Define una función que encuentre el máximo de tres números. 
   La función debe aceptar tres argumentos y devolver el número más grande.
   
4. Diseña una función que calcule la potencia de un número. 
   La función debe recibir la base y el exponente como argumentos y devolver el resultado.

5. Realizar el mismo ejercicio del item 2, pero sin utilizar el operador % 
'''

#ejercicio_1

def solicitar_entero()->int:
    numero_entero = int(input("Ingrese un número: "))
    return numero_entero

numero_funcion = solicitar_entero()
print(numero_funcion)

#ejercicio_2

def verificar_par_impar(numero:int):
   
    if numero % 2 == 0:
      print("El número es par")
    else:
      print("El número es impar")

numero = int(input("Ingrese un número: "))
verificar_par_impar(numero)

#ejercicio_3

def definir_maximo(numero_a:int, numero_b:int, numero_c:int)->int:
   '''
   Compara los 3 datos y retorna el mayor de estos.

   numero_a -> int
   numero_b -> int
   numero_c -> int

   return -> int
   '''
   numero_maximo = numero_a
   if numero_b > numero_maximo and numero_b > numero_c:
      numero_maximo = numero_b
   elif numero_c > numero_a:
      numero_maximo = numero_c

   return numero_maximo

maximo = (definir_maximo(0,40,200))
print("El número máximo es: " + str(maximo))

#ejercicio_4

def potenciar(base:int,exponente:int)->int:
   '''
   Summary:
      Permite obtener el resultado de potencia entre dos números y retorna el resultado.
      
      Base(int): numero base a potenciar
      Exponente(int): cantidad de veces que multiplica la base

      Return:
         int
   '''      
   resultado = 1
   for i in range(exponente):
      resultado *= base

   return resultado

numero_elevado = potenciar(2,4)
print(numero_elevado)

#ejercicio_5

def verificacion_par_impar_2(numero:int):
   '''
   summary:
      Verifica el número e imprime si es par o impar. El 0 
      numero -> int
   '''

   if numero < 0:
      numero *= -1
      
   while numero >= 2:
      numero -= 2

   if numero == 1:
      print("El número es impar")
   else:
      print("El número es par")

verificacion_par_impar_2(15)