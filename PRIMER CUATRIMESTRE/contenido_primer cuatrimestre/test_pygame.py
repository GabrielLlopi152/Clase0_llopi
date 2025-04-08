import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("vamos a hacer un juego!")
while(running):
	window.fill((255, 255, 255)) # Se pinta el fondo de la ventana
	pygame.draw.circle(window, (200, 200, 205), (250, 250), 75)
	pygame.draw.line(window, (220, 245, 55), (400, 400), (400, 300), 10)
	for event in pygame.event.get(): #eventos, mouse, teclado, joystick, señales que recibe 
		if event.type == pygame.QUIT:
			running = False

	

	
	pygame.display.flip()# Muestra los cambios en la pantalla