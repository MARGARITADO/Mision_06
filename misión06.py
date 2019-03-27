# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

#Martha Maragarira Dorantes Cordero

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO = (0,0,0)			# Representación del color negro en RGB
BLANCO = (255,255,255)	# Representación del color blanco en RGB

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))	# Crea la ventana donde dibujará
    reloj = pygame.time.Clock()		# Para limitar los fps
    termina = False					# Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    ventana.fill(BLANCO)	# Colorear la ventana de blanco (fondo)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:	# El usuario hizo click en el botón de salir
                termina = True				# Queremos terminar el ciclo

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        # Ejecución del código para generar la figura del espirógrafo
        k = r / R
        periodo = int(r//math.gcd(r, R))
        for angulo in range(0,360*periodo + 1,1):
        	theta = math.radians(angulo) # Convierte a radianes
        	x = int( R * ( (1-k) * math.cos(theta) + l*k * math.cos( ((1-k)*theta) / k )) )
        	y = int( R * ( (1-k) * math.sin(theta) - l*k * math.sin( ((1-k)*theta) / k )) )
        	pygame.draw.circle(ventana, (red,green,blue), (x+ANCHO//2,ALTO//2-y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main() :
	r = int(input("\n Ingrese el valor de r: "))
	R = int(input("\n Ingrese el valor de R: "))
	l = float(input("\n Ingrese el valor de l: "))
	dibujar(r,R,l)

# valores sugeridos  r:80, 260  R:45, 35  l:0.45, .90

main()