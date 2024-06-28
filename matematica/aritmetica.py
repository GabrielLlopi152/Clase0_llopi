def sumar(variable_a, variable_b):
    resultado = variable_a + variable_b
    return resultado

def restar(variable_a, variable_b):
    resultado = variable_a - variable_b
    return resultado

def multiplicar(variable_a, variable_b):
    resultado = variable_a * variable_b
    return resultado

def dividir(variable_a, variable_b):
    resultado = variable_a / variable_b
    return resultado

def factorial(numero_natural:int)->int:
    '''
    Summary:
    La función recibe el numero natural, y realiza el factorial de éste

    Args:
    numero_natural(int): debe ser mayor o igual a 0

    return:
    int: en caso de ser negativo, devolverá un numero predefinido (-999)
    '''
    resultado = 1
    if numero_natural >= 0:
        for i in range (numero_natural,1, -1):
            resultado *= i
    else: 
        resultado = -999
    return resultado

