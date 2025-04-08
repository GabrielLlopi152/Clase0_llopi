import pygame

pygame.init()

running = True

window = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption("Ahorcaoo")

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,1000)
contador = 0

posicion_circulo_x = 250
posicion_circulo_y = 250
radio = 75
velocidad_circulo = 10

posicion_cuadrado_x = 500
posicion_cuadrado_y = 500
ancho_cuadrado = 100
alto_cuadrado= 100
velocidad_cuadrado = 20

#window.fill((200, 200, 200)) # Se pinta el fondo de la ventana

while(running):
	window.fill((100, 100, 100)) # Se pinta el fondo de la ventana

	circulo = pygame.draw.circle(window, (200, 200, 205), (posicion_circulo_x, posicion_circulo_y), radio)
	pygame.draw.rect(window, (10, 210, 100), (posicion_cuadrado_x, posicion_cuadrado_y,ancho_cuadrado,alto_cuadrado))
	pygame.Vector2()

	fuente_texto = pygame.font.SysFont("Arial Narrow", 40)
	texto = fuente_texto.render('Tiempo: ' + str(contador), True, (0, 0, 0))
	window.blit(texto,(10,10))


	for event in pygame.event.get(): #eventos, mouse, teclado, joystick, señales que recibe 
		if event.type == pygame.QUIT:
			running = False
		if event.type == tick:
			contador += 1

		if event.type == pygame.MOUSEBUTTONDOWN: #mouse
			pass

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

			#CIRCULO
			if event.key == pygame.K_LEFT:
				posicion_circulo_x -= velocidad_circulo
			
			if event.key == pygame.K_UP:
				posicion_circulo_y -= velocidad_circulo
			
			if event.key == pygame.K_DOWN:
				posicion_circulo_y += velocidad_circulo
				
			if event.key == pygame.K_RIGHT:
				posicion_circulo_x += velocidad_circulo
			

			#CUADRADO
			if event.key == pygame.K_a:
				posicion_cuadrado_x -= velocidad_cuadrado
			
			if event.key == pygame.K_w:
				posicion_cuadrado_y -= velocidad_cuadrado
			
			if event.key == pygame.K_s:
				posicion_cuadrado_y += velocidad_cuadrado

			if event.key == pygame.K_d:
				posicion_cuadrado_x += velocidad_cuadrado
				

	pygame.display.flip()
