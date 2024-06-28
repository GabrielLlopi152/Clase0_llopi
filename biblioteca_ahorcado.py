import random
import pygame
import json

with open('ranking_ahorcado.json','r') as file:
	lista_partidas = json.load(file)['partidas']
lista_palabras_usadas = []
window = pygame.display.set_mode((1000, 700), 0, 32)

def rellenar_bytes(cadena_caracteres:str)->str:
    """recibe un string, y en caso de que no llegue a un byte (multiplo de 8 caracteres), lo completará con caracteres vacios

    Args:
        cadena_caracteres (str): _description_

    Returns:
        str: retorna el str con el tamaño de un byte
    """    

    retorno = False
    while not len(cadena_caracteres) == 8 and not len(cadena_caracteres) == 16 and not len(cadena_caracteres) == 24 and not len(cadena_caracteres) == 32:
        cadena_caracteres += ' '
        
    retorno = cadena_caracteres
    return retorno

def obtener_palabra_random(lista:list, idioma:str)->str:
	"""Elige aleatoriamente una palabra de una lista y la devuelve.
	En caso de que esa palabra se repita, buscará una que no haya aparecido

	Args:
		lista (list): Lista de palabras
		idioma (str): Idioma ("ES" | "EN")

	Returns:
		str: retorna la palabra con el idioma correspondiente
	"""	
	palabra = random.choice(lista)

	if len(lista_palabras_usadas) == len(lista):
		print('¡Felicidades, encontraste todas las palabras!')
		palabra = False
	else:
		while palabra["id"] in lista_palabras_usadas:
			palabra = random.choice(lista)

		lista_palabras_usadas.append(palabra["id"])
		palabra = palabra[idioma]
	return palabra

def slot_palabra(palabra:str)->str:
	"""Recorre una palabra y dibuja por cada letra una barra baja en una nueva cadena de caracteres ("_")

	Args:
		palabra (str):

	Returns:
		str: retorna la cadena de caracteres realizada
	"""
	retorno = ""
	if palabra == False:
		retorno = "Juego terminado"
	else:
		for letra in palabra:
			retorno += "-"

	return retorno

def verificar_letra_en_palabra(palabra_oculta:str, ingreso:str ,palabra:str):
	"""Verifica que la letra ingresada por el usuario coincida con alguna de las letras de la palabra oculta

	Args:
		palabra_oculta (str): palabra secreta que desconoce el usuario
		ingreso (str): letra ingresada por el usuario
		palabra (str): palabra que ve el usuario
	"""	
	bandera_cambio = False

	lista_palabra_secreta = []

	#recorro la palabra a adivinar
	for letra in palabra:
		lista_palabra_secreta.append(letra)

	if len(ingreso) == 1:
		for i in range(len(palabra_oculta)):
			if palabra_oculta[i] == ingreso:
				lista_palabra_secreta[i] = ingreso
				bandera_cambio = True

	palabra_final = ""
	for letra in lista_palabra_secreta:
		palabra_final += letra

	return palabra_final if bandera_cambio == True else False

def cambiar_fuente_texto(tamaño:int):
	"""modifica el tamaño fuente de los textos que aparecen en pantalla.
	Fuente predeterminada: "Arial Narrow"

	Args:
		tamaño (int): numero que representa el tamaño de las letras de la fuente

	Returns:
		_type_: retorna la fuente del texto para que sea utilizado
	"""	
	fuente_texto = pygame.font.SysFont("Arial Narrow", tamaño)
	return fuente_texto
	
def mostrar_texto_blanco(mensaje:str, fuente_texto, coordenadas:tuple):
	"""pinta de blanco en la pantalla el texto que se le asigne con la fuente y coordenadas que reciba

	Args:
		mensaje (str): texto que se verá en la pantalla
		fuente_texto (_type_): fuente/formato del mensaje
		coordenadas (tuple): ubicación del texto en la pantalla
	"""	
	texto = fuente_texto.render(mensaje, True, (255, 255, 255))
	window.blit(texto,(coordenadas))

def mostrar_texto_negro(mensaje:str, fuente_texto, coordenadas:tuple):
	"""pinta de negro en la pantalla el texto que se le asigne con la fuente y coordenadas que reciba

	Args:
		mensaje (str): texto que se verá en la pantalla
		fuente_texto (_type_): fuente/formato del mensaje
		coordenadas (tuple): ubicación del texto en la pantalla
	"""	
	texto = fuente_texto.render(mensaje, True, (0, 0, 0))
	window.blit(texto,(coordenadas))

def ordenar_lista_diccionarios(lista:list,key:str, criterio:str):
	"""ordenamiento de diccionarios que pertenecen a una lista.
	No usar en listas simples

	Args:
		lista (list): lista con los datos a ordenar
		key (str): clave por el cual se realizará el ordenamiento
		criterio (str): asc | desc. Define si el orden se hará ascendente o descendiente
	"""	
	for i in range(len(lista) - 1):
		for j in range(i+1, len(lista)):
			if criterio.lower() == 'asc' and lista[i][key] > lista[j][key] or criterio.lower() == 'desc' and lista[i][key] < lista[j][key]:
				auxiliar = lista[i]
				lista[i] = lista[j]
				lista[j] = auxiliar

def listar_encabezado(mensaje_nombre:str, mensaje_puntaje:str, mensaje_tiempo:str,idioma:str,fuente_texto, direccion_x, direccion_y):
	'''mensaje = '{0}    {1}    {2}    {3}'.format(mensaje_nombre,mensaje_puntaje,mensaje_tiempo,idioma)
	mostrar_texto_negro(mensaje,fuente_texto, (direccion_x,direccion_y))'''
	mostrar_texto_negro(mensaje_nombre,fuente_texto, (direccion_x,direccion_y))
	mostrar_texto_negro(mensaje_puntaje,fuente_texto, (direccion_x+150,direccion_y))
	mostrar_texto_negro(mensaje_tiempo,fuente_texto, (direccion_x+330,direccion_y))
	mostrar_texto_negro(idioma,fuente_texto, (direccion_x+500,direccion_y))

def listar_partidas(lista:list, fuente_texto, direccion_x, direccion_y):
	contador = 0
	for partida in lista:
		contador += 1
		direccion_y += 80
		mensaje = ''
		if contador <= 5:
			for dato in partida.keys():
				mensaje = str(partida[dato])
				mostrar_texto_negro(mensaje, fuente_texto, (direccion_x, direccion_y))
				direccion_x += 175
				
		direccion_x -= 700
		