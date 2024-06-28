'print("Hola mundo")'

verduras = ["tomate", "lechuga", 'col', 'zanahoria']
frutas = []

def listar(lista:list):
    if lista != []:
        for i in lista:
         print(i)
    else:
       print("Lista vacía")

listar(frutas)

def mostrar(lista:list, indice:int):
   print(lista[indice])