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