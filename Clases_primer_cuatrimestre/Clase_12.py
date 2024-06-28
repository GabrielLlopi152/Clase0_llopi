#DICCIONARIOS

'''
    Las claves de los diccionarios son unicas, pero sus variables pueden repetirse en variables externas.
    diccionario= "variable" : "dato", "variable2" : "dato 2"
    Puede haber un diccionario en otro diccionario
diccionario = "nombre de diccionario" : {"variable": "dato", "variable2" : "dato2"}
Los FOR recorren las claves/keys/variables, NO los datos

Shallow copy        solo copia las referencias a los elementos contenidos en el objeto, osea,
permite modificar solo los de referencia -> .copy
Deepcopy()          copia todo y no detecta cambios dentro de arrays y/o diccionarios del diccionario original
.get()              busca la clave ingresada y devuelve su dato, si no hay nada, devuelve la condicion ingresada.
.keys()             devuelve las keys pertenecientes al diccionario.
.values()           devuelve los valores de cada clave/key del diccionario.
.items()            devuelve tanto la key como su valor en una lista.
.pop()              elimina una key del diccionario.
.update()           actualiza una lista, agregando keys y datos o pisandoya existentes.
.clear()            limpia completamente el diccionario.
'''

persona = {'nombre' : 'Leo', 'apellido': 'Messi', 'edad' : 37} #ESTO es un diccionario
persona2 = persona

print(persona)
print(persona2)

persona['nombre'] ='mateo' 

print(persona)
print(persona2)

persona_copia = persona.copy()

persona_items = persona.items()

for i in persona_items:
    print(i)
