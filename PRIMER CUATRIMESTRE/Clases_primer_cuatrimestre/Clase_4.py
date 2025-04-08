'''
6 acomodamientos
factorial
'''
    
def factorial(natural):
    if natural == 0:
        retorno =  1
    else:
        retorno = natural * factorial(natural - 1)
    
    return retorno

dato = factorial(750)
print(dato)
