import json
import random
import pygame
from biblioteca_ahorcado import *

with open('ahorcado.json', 'r') as file:
	lista_ahorcado = json.load(file)['ahorcado']
with open('ranking_ahorcado.json','r') as file:
	lista_partidas = json.load(file)['partidas']

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

#Banderas establecidas
running = True
español = True
partida_iniciada = False
partida_critica = False
adivinando_palabra = False
derrota = False
palabra_hallada = False
letra_ingresada = False
cancelar = False
confirmar = False
ver_ranking = False
musica = True
seleccion_musica = True
cambio_musica = False
bandera_musica_partida = True
bandera_musica_critico = True
regreso_menu = False

#Configuracion_pantalla
window = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption("Ahorcado")

#Timer
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,1000)
contador = 0
contador_cambios = 0
bandera_timer = True

while(running):

	#Idiomas
	if español:
		idioma = "ES"
		mensaje_idioma_tabla = 'Idioma'
		mensaje_puntaje_tabla = 'Puntuación'
		mensaje_tiempo_tabla = 'Tiempo'
		mensaje_nombre_tabla = 'Nombre'
		mensaje_salir = 'Presiona "Esc" para salir'
		mensaje_puntaje = 'Puntuación: '
		mensaje_tiempo = 'Tiempo: '
		mensaje_boton_jugar = 'Iniciar juego'
		mensaje_boton_ranking = 'Puntajes'
		mensaje_boton_idioma ='Cambiar idioma'
		mensaje_boton_salir = 'Salir'
		mensaje_boton_volver = 'Volver al menu'
		mensaje_intento = 'Intentos: '
		mensaje_derrota = '¡Perdiste!'
		mensaje_adivinado = '¡Bien! Otra palabra en: '
		mensaje_victoria = '¡Ganaste, felicidades!'
		mensaje_volver_menu = 'Volviendo al menú en '
		mensaje_palabra_oculta = 'La palabra era: '
		mensaje_nombre = 'Escriba su nombre'
		mensaje_nombre_usuario = 'Nombre: '
	else:
		idioma = "EN"
		mensaje_idioma_tabla = 'Language'
		mensaje_puntaje_tabla = 'Score'
		mensaje_tiempo_tabla = 'Time'
		mensaje_nombre_tabla = 'Name'
		mensaje_salir ='Press "Esc" to exit'
		mensaje_puntaje = 'Score: '
		mensaje_tiempo = 'Time: '
		mensaje_boton_jugar = 'Start game'
		mensaje_boton_ranking = 'Scores'
		mensaje_boton_idioma = 'Change language'
		mensaje_boton_salir = 'Exit'
		mensaje_boton_volver = 'Back to the menu'
		mensaje_intento = 'Attempts: '
		mensaje_derrota = 'You lose!'
		mensaje_adivinado = 'Good job! Next word in: '
		mensaje_victoria = '¡You win, congratulations!'
		mensaje_volver_menu = 'Returning to the menu in '
		mensaje_palabra_oculta = 'The word was: '
		mensaje_nombre = 'Write your name'
		mensaje_nombre_usuario = 'Name: '

	#Icono musica
	if musica:
		imagen_musica = 'sonido_on.png'		
	else:
		imagen_musica = 'sonido_off.png'

	#Cambio de fondo segun estado del juego
	if not partida_iniciada:
		nombre_fondo = 'menu_fondo.jpg'
		musica_nombre = "tema_menu.mp3"
	elif partida_critica:
		nombre_fondo = 'fondo_estado_critico.jpg'
	else:
		nombre_fondo = 'fondito_partida.jpg'
		
	#Menu
	if partida_iniciada == False and not ver_ranking:

		#Cambio de musica
		if musica and regreso_menu:
			musica_nombre = "tema_menu.mp3"
			seleccion_musica = True
			cambio_musica = True
			regreso_menu = False

		#Restablecimiento de variables
		lista_palabras_usadas = []
		nick_jugador = ''
		datos_jugador = {}
		adivinando_palabra = False
		partida_critica = False
		hay_nombre = False
		contador = 0
		contador_cambios = 0
		puntaje = 0
		intentos = 6
		bandera_musica_partida = True
		bandera_musica_critico = True

		#Cargar imagenes del menu
		fondo = pygame.image.load(nombre_fondo)
		icono_musica = pygame.image.load(imagen_musica)
		window.blit(fondo, (0,0))	

		#Botones del menu
		boton_jugar = pygame.Rect((400, 250), (250, 40)) #zona colision
		pygame.draw.rect(window, (220, 245, 55), (400, 250, 250, 40)) #interfaz colision
		boton_ranking = pygame.Rect((400, 300), (250, 40))
		pygame.draw.rect(window, (220, 245, 55), (400, 300, 250, 40))
		boton_idioma = pygame.Rect((400, 350), (250, 40))
		pygame.draw.rect(window, (220, 245, 55), (400, 350, 250, 40))
		boton_salir = pygame.Rect((400, 400), (250, 40))
		pygame.draw.rect(window, (220, 245, 55), (400, 400, 250, 40))
		boton_musica = pygame.Rect((10, 650), (50, 50))
		window.blit(icono_musica, (10, 650))
		boton_volver = pygame.Rect((380, 610), (250, 40))

		#Texto de interfaz menu
		fuente_texto = cambiar_fuente_texto(25)
		mostrar_texto_negro(mensaje_salir, fuente_texto,(775,10))
		fuente_texto = cambiar_fuente_texto(40)
		mostrar_texto_negro(mensaje_boton_jugar, fuente_texto,(440,260))
		mostrar_texto_negro(mensaje_boton_ranking, fuente_texto,(465,310))
		mostrar_texto_negro(mensaje_boton_idioma, fuente_texto,(405,360))
		mostrar_texto_negro(mensaje_boton_salir, fuente_texto,(490,410))

	#Mostrar los mejores jugadores
	elif ver_ranking: 
		#Fondo menu
		fondo = pygame.image.load(nombre_fondo)
		window.blit(fondo, (0,0))

		#Boton regreso
		boton_volver = pygame.Rect((375, 610), (250, 40))
		pygame.draw.rect(window, (220, 245, 55), (375, 610, 250, 40))
		mostrar_texto_negro(mensaje_boton_volver, fuente_texto, (390,620))

		#Tablero
		pygame.draw.rect(window, (220, 245, 55), (150, 100, 700, 500))
		listar_encabezado(mensaje_nombre_tabla,mensaje_puntaje_tabla, mensaje_tiempo_tabla,mensaje_idioma_tabla, fuente_texto, 200, 110)
		listar_partidas(lista_partidas,fuente_texto,200,110)
		pygame.draw.rect(window, (0, 0, 0), (150, 150, 700, 5))

	#Partida en curso
	else:
		#Cambio de musica
		if musica and bandera_musica_partida:
			musica_nombre = "tema_partida.mp3"
			seleccion_musica = True
			cambio_musica = True
			bandera_musica_partida = False

		#Selección de palabra aleatoria
		if not adivinando_palabra or palabra_hallada:
			palabra_oculta = obtener_palabra_random(lista_ahorcado, idioma)
			print(palabra_oculta)
			palabra_interfaz = slot_palabra(palabra_oculta)
			adivinando_palabra = True
			palabra_hallada = False

		#Fondo
		fondo = pygame.image.load(nombre_fondo)
		window.blit(fondo, (0,0))
		pygame.draw.rect(window, (210, 150, 250), (0, 600, 600, 100))

		#Texto de interfaz de partida
		fuente_texto = cambiar_fuente_texto(25)
		mostrar_texto_negro(mensaje_puntaje + str(puntaje),fuente_texto,(10,10))
		mostrar_texto_negro(mensaje_tiempo + str(contador),fuente_texto,(10,40))
		mostrar_texto_negro(mensaje_intento + str(intentos),fuente_texto,(10,70))
		mostrar_texto_negro(mensaje_salir,fuente_texto,(775,10))
		fuente_texto = cambiar_fuente_texto(120)
		mostrar_texto_negro(palabra_interfaz, fuente_texto,(50,610))
		
		#Diseño del poste
		pygame.draw.rect(window, (133, 47, 4), (900, 100, 10, 500))
		pygame.draw.rect(window, (133, 47, 4), (750, 100, 150, 10))
		pygame.draw.rect(window, (133, 47, 4), (750, 100, 10, 50))
		
		#Ingreso del usuario
		if intentos > 0 and adivinando_palabra and letra_ingresada:
			validacion = verificar_letra_en_palabra(palabra_oculta,letra,palabra_interfaz)
			if validacion != False:
				palabra_interfaz = validacion
			else:
				intentos -= 1
			letra_ingresada = False

		#Usuario adivinó
		if palabra_oculta == palabra_interfaz:
			if bandera_timer:
				contador_cambios = 6
				bandera_timer = False
				puntaje += len(palabra_oculta)

			#pantallazo verde con mensajes
			window.fill((45, 205, 0))
			fuente_texto = cambiar_fuente_texto(80)
			mostrar_texto_blanco(mensaje_adivinado + str(contador_cambios), fuente_texto,(200,50))
			mostrar_texto_blanco(mensaje_palabra_oculta + palabra_oculta, fuente_texto,(150,200))
			mostrar_texto_blanco(mensaje_tiempo + str(contador), fuente_texto,(350,300))
			mostrar_texto_blanco(mensaje_puntaje + str(puntaje), fuente_texto,(350,400))
			
			if contador_cambios == 0:
				palabra_hallada = True

		#Sección de intentos
		if not contador_cambios:
			if intentos <= 5:
				pygame.draw.circle(window, (240, 170, 225), (755, 200), 50)
			if intentos <= 4:
				pygame.draw.rect(window, (160, 30, 30), (720, 250, 70, 130))
			if intentos <= 3:
				pygame.draw.rect(window, (160, 30, 30), (690, 250, 30, 70))
				pygame.draw.rect(window, (240, 170, 225), (690, 320, 30, 30))
			if intentos <= 2:
				pygame.draw.rect(window, (160, 30, 30), (790, 250, 30, 70))
				pygame.draw.rect(window, (240, 170, 225), (790, 320, 30, 30))
				partida_critica = True

				#Cambio de musica
				if musica and bandera_musica_critico:
					seleccion_musica = True
					cambio_musica = True
					musica_nombre = 'tema_partida_critica.mp3'
					bandera_musica_critico = False
			if intentos <= 1:
				pygame.draw.rect(window, (50, 65, 255), (720, 380, 35, 100))
				pygame.draw.rect(window, (0,0,0), (720, 480, 35, 30))
			if intentos == 0:
				pygame.draw.rect(window, (50, 65, 255), (755, 380, 35, 100))
				pygame.draw.rect(window, (0,0,0), (755, 480, 35, 30))
				derrota = True

	if derrota: #conclusion de la partida
		if not hay_nombre:
			window.fill((255, 35, 30))

			#Ingreso del nombre
			if letra_ingresada:
				if len(nick_jugador) < 8:
					nick_jugador += letra
				letra_ingresada = False
				confirmar = False
			if cancelar:
				nick_jugador = ''
				cancelar = False
			if confirmar and nick_jugador != '': #Nombre registrado.
				#Se guardan los datos del jugador
				datos_jugador = {
				'nombre': nick_jugador,
				'puntaje': puntaje,
				'tiempo': contador,
				'idioma': idioma
				}

				#Se sube los datos al archivo json
				lista_partidas.append(datos_jugador)
				ordenar_lista_diccionarios(lista_partidas,'puntaje','desc')
				data = {'partidas': lista_partidas}
				with open('ranking_ahorcado.json', 'w') as file:
					json.dump(data, file, indent=4, ensure_ascii=False)
				
				hay_nombre = True
				confirmar = False

			#Texto de interfaz seleccion nombre
			fuente_texto = cambiar_fuente_texto(80)
			mostrar_texto_blanco(mensaje_derrota,fuente_texto,(350,100))
			mostrar_texto_blanco(mensaje_nombre,fuente_texto,(200,350))
			fuente_texto = cambiar_fuente_texto(50)
			mostrar_texto_blanco(mensaje_palabra_oculta + palabra_oculta,fuente_texto,(200,200))
			mostrar_texto_blanco(mensaje_nombre_usuario + nick_jugador,fuente_texto,(200,450))
			
		else:
			if bandera_timer:
				contador_cambios = 10
				bandera_timer = False

			#Mensajes en pantalla
			window.fill((255, 35, 30))
			fuente_texto = cambiar_fuente_texto(80)
			mostrar_texto_blanco(mensaje_derrota,fuente_texto,(350,100))
			fuente_texto = cambiar_fuente_texto(50)
			mostrar_texto_blanco(mensaje_palabra_oculta + palabra_oculta,fuente_texto,(200,200))
			mostrar_texto_blanco(mensaje_nombre_usuario + nick_jugador,fuente_texto,(200,300))
			mostrar_texto_blanco(mensaje_tiempo + str(contador),fuente_texto,(200,400))
			mostrar_texto_blanco(mensaje_puntaje + str(puntaje),fuente_texto,(200,350))
			mostrar_texto_blanco(mensaje_volver_menu + str(contador_cambios),fuente_texto,(200,600))

			if contador_cambios == 0 or confirmar:
				regreso_menu = True
				partida_iniciada = False
				derrota = False

	#Musica de fondo
	if musica:
		if seleccion_musica: #Cambio de tema 
			if cambio_musica: #Utilizo bandera para que no rompa la primer vez
				musica_fondo.stop()
				cambio_musica = False
			musica_fondo = pygame.mixer.Sound(musica_nombre)
			musica_fondo.set_volume(0.2)
			musica_fondo.play(-1)
			seleccion_musica = False
		
	else:
		musica_fondo.stop()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if  event.type == tick: #tiempo real
			if partida_iniciada and not contador_cambios and not derrota: #tiempo de partida
				contador += 1
			if contador_cambios > 0: #cuenta atras para eventos
				contador_cambios -= 1
			else:
				bandera_timer = True
	
		if event.type == pygame.MOUSEBUTTONDOWN: #mouse
			if not partida_iniciada:
				if boton_jugar.collidepoint(event.pos):
					partida_iniciada = True
				if boton_idioma.collidepoint(event.pos):
					if español:
						español = False
					else:
						español = True
				if boton_ranking.collidepoint(event.pos):
					ver_ranking = True
				if boton_salir.collidepoint(event.pos):
					running = False
				if boton_musica.collidepoint(event.pos):
					if musica:
						musica = False
					else:
						musica = True
						seleccion_musica = True
			if ver_ranking:
				if boton_volver.collidepoint(event.pos):
					ver_ranking = False
			
		if event.type == pygame.KEYDOWN: #teclado
			if event.key == pygame.K_ESCAPE and not ver_ranking:
				running = False
			elif event.key == pygame.K_ESCAPE and ver_ranking:
				ver_ranking = False
			if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
				cancelar = True
			if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
				confirmar = True

			if partida_iniciada and not contador_cambios:
				if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c or event.key == pygame.K_d or event.key == pygame.K_e or event.key == pygame.K_f or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_i or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_l or event.key == pygame.K_m or event.key == pygame.K_n or event.key == pygame.K_o  or event.key == pygame.K_p or event.key == pygame.K_q or event.key == pygame.K_r or event.key == pygame.K_s or event.key == pygame.K_t or event.key == pygame.K_u or event.key == pygame.K_v or event.key == pygame.K_w or event.key == pygame.K_x or event.key == pygame.K_y or event.key == pygame.K_z:
					
					letra = chr(event.key)
					letra_ingresada = True

	pygame.display.flip()

'''
A. Se elegirá el idioma a jugar, palabras en español o en inglés. 									LISTO
B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar / Play”, “Puntajes / Scores” y		LISTO
“Salir / Exit” (dependiendo el idioma seleccionado), la misma deberá tener alguna
imagen cubriendo completamente el fondo y tener un sonido de fondo. Al apretar el
botón jugar se iniciará el juego.
C. Se tendrán 6 intentos (uno por cada parte del cuerpo del ahorcado). 								LISTO
D. Cada palabra descubierta suma un punto por letra de la misma. Ejemplo: “elefante”
tiene 8 letras y en consecuencia 8 puntos.															LISTO
E. La figura del ahorcado será:																		LISTO
➢ Círculo para la cabeza.
➢ Rectángulo para el tórax.
➢ Líneas para brazos y piernas.
(Opcionalmente se puede usar imagenes en vez de círculos, rectángulos o líneas)

F. Al finalizar la partida se debe colocar el nick del jugador en una caja de texto.				LISTO
G. El botón “Puntajes / Scores” deberá tener la funcionalidad de mostrar el top 5 de los			LISTO
mejores puntajes en la pantalla inicial.
H. Se debe tener a la vista los puntos que se van acumulando durante la partida.					LISTO
I. Luego de cada partida, debe guardar en un archivo los siguientes datos:							LISTO
➢ Nick.
➢ Puntaje.
J. Opcionalmente se puede agregar a la pantalla inicial un botón para “mutear /						LISTO
desmutear” el audio. 🔇/🔊
K. Opcionalmente se puede agregar audio cada vez que se descubre una palabra y otro
cuando se pierde la partida.
'''