def contar_caracteres(variable:str)->int:
    contador = 0
    for letra in variable:
        contador += 1

    return contador

'''mensaje = "Hola"

print(contar_caracteres(mensaje))

print(chr(ord('A')+32))

print(ord('A'))

print(chr(97))
'''

nombre = "chilindrina"

def capitalizar(variable:str)->str:
    cantidad = contar_caracteres(variable)

    if ord(variable[0]) >= 97 and ord(variable[0]) <= 122:
        for i in range(cantidad):

            if i == 0:
                letra_inicial = chr(ord(variable[i])-32)
                retorno= letra_inicial
            else:
                retorno += variable[i]
    else:
        retorno = variable

    return retorno

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

def convertir_minuscula(variable:str)->str:
    cantidad = contar_caracteres(variable)
    retorno = ""

    for i in range(cantidad):
        if ord(variable[i]) >= 65 and ord(variable[i]) <= 90:
        
            letra = chr(ord(variable[i])+32) 
            retorno += letra
        else: 
            retorno += variable[i]
        
    return retorno

nombre_1 = capitalizar(nombre)
print(nombre_1)

nombre_2 = convertir_mayuscula(nombre)
print(nombre_2)

nombre_3 = convertir_minuscula(nombre)
print(nombre_3)

