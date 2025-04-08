from os import system


def promedio_por_genero (diccionario:dict,clave:str,genero:str)->float:
    """_summary_

    Args:
        diccionario (dict): _description_
        key (str): _description_

    Returns:
        float: _description_
        ctrl+shift+2
    """    
    contador = 0
    acumulador_fuerza = 0

    for datos in diccionario:
        for key in datos.keys():
            if key == clave and  datos['genero'] == genero:
                acumulador_fuerza = acumulador_fuerza + float(datos[key])
                contador = contador + 1

    if contador > 0 :
        return acumulador_fuerza / contador
    
def clave_max_min_genero (diccionario:dict, clave:str, genero:str, comparacion:str):
    bandera = True
    for personaje in diccionario:
        if personaje["genero"] == genero:
            if comparacion == "MAX":
                if bandera == True or float(personaje[clave]) > clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
            elif comparacion == "MIN":
                if bandera == True or float(personaje[clave]) < clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
    if bandera == True:
        nombre = "No hay personajes con este genero"
    return nombre

def pausa():
    var = input("Presione Enter para continuar...")
    system ("cls")

def listar_por_caracteristica(lista:list, clave_a_buscar:str):
    diccionario_auxiliar = {}

    for personaje in lista:
        clave = personaje[clave_a_buscar].capitalize()
        if clave != "":
            if clave in diccionario_auxiliar:
                diccionario_auxiliar[clave] += " - " + personaje["nombre"]
            else:
                diccionario_auxiliar[clave] = personaje["nombre"]


    for clave, nombres in diccionario_auxiliar.items():
        print(f"{clave}: {nombres}")
        print ("------------------------")
    
def contar_por_caracteristica (lista:list, clave:str):
    lista_auxiliar = []
    print("Color\t\t\t\tCantidad")
    print("----------------------------------------")
    for personaje in lista:
        lista_auxiliar.append(personaje[clave].capitalize())
    set_auxiliar = set(lista_auxiliar)
    for caracteristica in set_auxiliar:
        contador = 0 
        for personaje in lista:
            if caracteristica == personaje[clave].capitalize():
                contador += 1 
        if len(caracteristica) < 10:
            print(f"{caracteristica}\t\t\t\t{contador}")
        else:
            print(f"{caracteristica}\t\t\t{contador}")