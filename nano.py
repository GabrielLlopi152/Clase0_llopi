import pygame
import pygame_textinput
import json
import random

pygame.init()
textinput = pygame_textinput.TextInputVisualizer()
running = True
#pantalla
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption('Ahorcado de Nano')
menu = pygame.image.load("menu_fondo.jpg")
menu = pygame.transform.scale(menu,(640,480))
fondo = pygame.image.load("menu.jpg")
fondo = pygame.transform.scale(fondo,(640,480))
#coordenada
x = 380
y = 400
#fuente
font = pygame.font.SysFont("Arial Narrow", 25)
font_2 = pygame.font.SysFont("Arial Narrow", 50)
#contadores
contador_puntos = 0
contador_idi = 0
#palabras
palabra = ''
idioma = 'ESP'
mensaje_puntos_esp = "Puntos"
mensaje_idi_esp = "Presione aqui para cambiar de idioma"
mensaje_errores_esp = "Letras erradas"
mensaje_salir_esp = "Salir"
mensaje_iniciar_esp = "Iniciar"
idi_esp = 'ES'
mensaje_puntos_ing = "Score"
mensaje_idi_ing = "Press here to change language"
mensaje_errores_ing = "Wrong letters"
mensaje_salir_ing = "Exit"
mensaje_iniciar_ing = "Start"
idi_ing = 'EN'

with open("ahorcado.json", "r") as archivo:
    ahorcado = json.load(archivo)["ahorcado"]

lista_palabras_usadas = []

def obtener_palabra_random(lista, idioma):
    palabra = random.choice(lista)
    if len(lista_palabras_usadas) == len(lista):
        print("Ya no quedan palabras para adivinar")
        palabra = False
    else:
        while palabra["id"] in lista_palabras_usadas:
            palabra = random.choice(lista)
        lista_palabras_usadas.append(palabra["id"])
        palabra = palabra[idioma]
    print(palabra)
    return palabra

def slot_palabra(palabra:str):
    retorno = ""
    if palabra == False:
        retorno = "Juego Terminado"
    else:
        for letra in palabra:
            retorno += "-"
    return retorno

def verificar_letra_en_palabra(palabra, ingreso, palabra_secreta):
    bandera_cambio = False
    lista_palabra_secreta = []
    for letra in palabra_secreta:
        lista_palabra_secreta.append(letra)
    if len(ingreso) == 1:
        for i in range(len(palabra)):
            if palabra[i] == ingreso:
                lista_palabra_secreta[i] = ingreso
                bandera_cambio = True
    palabra_final = ""
    for letra in lista_palabra_secreta:
        palabra_final += letra
    print(palabra_final)
    return palabra_final if bandera_cambio == True else False

palabra_secreta = ""
posicion = (130, 12)
contador_errores = 0
iniciar_partida = False

#JERRY. añado 2 banderas mas. una para que busque una palabra al comienzo de la partida y otro que dé señal para validar la letra
hay_letra = False
palabra_inicial = True
#JERRY. añado una bandera para buscar una palabra SOLO cuando es necesario (comienzo o cuando se acierta la anterior)
buscar_palabra = False

while (running):
    #seleccion de idioma
    if idioma == 'ESP':
        mensaje_puntos = mensaje_puntos_esp
        mensaje_idi_1 = mensaje_idi_esp
        mensaje_errores = mensaje_errores_esp
        mensaje_salir = mensaje_salir_esp
        mensaje_iniciar = mensaje_iniciar_esp
        idi = idi_esp
    elif idioma == 'ING':
        mensaje_puntos = mensaje_puntos_ing
        mensaje_idi_1 = mensaje_idi_ing
        mensaje_errores = mensaje_errores_ing
        mensaje_salir = mensaje_salir_ing
        mensaje_iniciar = mensaje_iniciar_ing
        idi = idi_ing

    #JERRY. añadi un buscador de palabra que solo busque cuando se de la señal de buscar. automaticamente se vuelve false tras tener una palabra
    if iniciar_partida == True: #JERRY. solo busca y analiza la palabra cuando inicia la partida
        if palabra_inicial == True or buscar_palabra == True: #SOLO cuando inicia la partida o acierta, busca otra palabra
            palabra = obtener_palabra_random(ahorcado, idi)
            palabra_secreta = slot_palabra(palabra)   
            palabra_inicial = False
            buscar_palabra = False

        if hay_letra == True: #JERRY. solo cuando se recibe una señal de una tecla, verifica 
            validacion = verificar_letra_en_palabra(palabra, letra, palabra_secreta)
            print(letra)
            if validacion != False:
                palabra_secreta = validacion
                print(palabra_secreta)
            else:
                contador_errores += 1
            if validacion == palabra:
                contador_puntos += len(str(palabra))
                buscar_palabra = True
                contador_errores = 0
            if contador_errores == 6:
                '''palabra = obtener_palabra_random(ahorcado, idi)
                palabra_secreta = slot_palabra(palabra)'''
                contador_errores = 0
                iniciar_partida = False
            textinput.value = ""
            hay_letra = False

    #preparacion de datos para imprimir
    texto_puntos = font.render(f"{mensaje_puntos}: {contador_puntos}", True, (170, 170, 170))
    texto_errores = font.render(f"{mensaje_errores}: {contador_errores}", True, (170, 170, 170)) 
    idioma_ing = font.render(f"{mensaje_idi_1}", True, (170, 170, 170))
    texto_rec = font_2.render(f"{palabra_secreta}", True, (20, 20, 20)) 
    texto_salir = font.render(f"{mensaje_salir}", True, (20, 20, 20))
    texto_iniciar = font.render(f"{mensaje_iniciar}", True, (20, 20, 20))
    #impresiones

    #JERRY. añadi afuera un cuadrado que no se verá nunca, ya que rompe porque no lo encuentra en la zona del for
    rect_ingreso = pygame.draw.rect(screen, (200, 200, 200), (1000, 1000, 240, 60))

    #menu al iniciar
    if iniciar_partida == False:
        screen.blit(menu,(0,0)) #fondo
        rect_idioma = pygame.draw.rect(screen, (20, 20, 20), (150, 20, 330, 30)) #rectangulo cambio idioma
        screen.blit(idioma_ing,(150,20)) #idioma 
        rect_inicio = pygame.draw.rect(screen, (150, 150, 150), (240, 200, 80, 30)) #rectangulo inicio
        screen.blit(texto_iniciar,(240,200)) #inicio
    #al jugar
    if iniciar_partida == True:
        screen.blit(fondo,(0,0)) #fondo
        pygame.draw.line(screen, ("brown"), (200,0), (200, 100), 10) #soga
        pygame.draw.ellipse(screen, ("brown"), (150, 100, 100, 50), 5) #soga
        screen.blit(texto_puntos,(10,5)) #puntaje
        screen.blit(texto_errores,(10,25)) #letras erradas
        
        #  JERRY. meti adentro del if el rectangulo de las palabras
        rect_ingreso = pygame.draw.rect(screen, (200, 200, 200), (x, y, 240, 60)) #rectangulo
        screen.blit(texto_rec,(x,y + 5)) #texto rectangulo

    rect_salir = pygame.draw.rect(screen, (255, 0, 0), (0, 440, 70, 40)) #rectangulo salir
    screen.blit(texto_salir,(10,450)) #mensaje salir
    pygame.display.flip()

    #entradas
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_idioma.collidepoint(event.pos):
                if contador_idi == 0:
                    idioma = 'ESP'
                    contador_idi += 1
                else:
                    if contador_idi == 1:
                        idioma = 'ING'
                        contador_idi += 1
                if contador_idi == 2:
                    contador_idi = 0
            if rect_inicio.collidepoint(event.pos):
                iniciar_partida = True
            if rect_ingreso.collidepoint(event.pos) and iniciar_partida: #JERRY. añadi iniciar partida
                palabra = obtener_palabra_random(ahorcado, idi)
                palabra_secreta = slot_palabra(palabra)    
            if rect_salir.collidepoint(event.pos):
                running = False
        
        if event.type == pygame.KEYDOWN: #JERRY. cambié el textinput por esto, y anduvo, si queres hacelo de otra forma
            if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c or event.key == pygame.K_d or event.key == pygame.K_e or event.key == pygame.K_f or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_i or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_l or event.key == pygame.K_m or event.key == pygame.K_n or event.key == pygame.K_o  or event.key == pygame.K_p or event.key == pygame.K_q or event.key == pygame.K_r or event.key == pygame.K_s or event.key == pygame.K_t or event.key == pygame.K_u or event.key == pygame.K_v or event.key == pygame.K_w or event.key == pygame.K_x or event.key == pygame.K_y or event.key == pygame.K_z:
				
                letra = chr(event.key)
                hay_letra = True

'''
JERRY
Corregi varias cosas, te dejo las lineas donde dejé comentarios para que entiendas.
si algo no entendiste decimelo.
linea 89
lin 92
linea 112
113
114
120
149
167
193
199

ah, y bajé abajo el for porque me daba ansieda

Nota: CAMBIALE LOS NOMBRES A LOS FONDOS Y EL ARCHIVO JSON. los puse pa que me ande
'''