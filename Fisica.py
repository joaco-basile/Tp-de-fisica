import pygame
import math

#constantes
k = 9*10**9

#Lados
a = 0
b = 0.5
c = (float(input("ingresar distancia de la particula: ")))

#angulos
A = math.radians(50)
B = 0
C = math.degrees(0)

#cargas
q1 = float(input("Escriba la carga 1: "))
q2 = float(input("Escriba la carga 2: "))
q3 = float(input("Escriba la carga 3: "))

#fuerza sobre carga 2
fq1 = 0
fq3 = 0
fq3y = 0
fq3x = 0
ft = 0

#teorema de coseno para el lado
a = (b**2-2*b*c*math.cos(A)+c**2)**0.5


#Teorema de coseno y de pitagoras para los angulos
#Sacamos el angulo de arriba
B = math.degrees(math.acos((0.5 * a**2 - 0.5 * b**2 + 0.5 * c**2) / (a*c)))

#Sacamos el angulo de la izquierda
A = math.degrees(A)
C = 180 - (A + B) 

#Pasamos la distancia a mm
c = c/1000
a = a/100
q1 = q1/10
q2 = q2/10
q3 = q3/10

# Calculamos fuerzas totales
fq1 = round((k * ((q1*10**-6 * q2*10**-6) / c**2)),2)

fq3 = round((k * ((q3*10**-6 * q2*10**-6) / a**2)),2)

# Calculamos fuerzas en x e y
fq3x = round((math.cos (30) * fq3),2)
fq3y = round((math.sin (30) * fq3),2)




#****************************************************************************************** PYGAME ENTORNO GRAFIO **************************************************************************************************

#pantalla
pygame.init()
tamanho = [1600, 900]
screen = pygame.display.set_mode(tamanho)
reloj = pygame.time.Clock()
desplazar_y = 0
c = c*1000
Rojo = 255
Verde = 255
Azul = 255
color = (Rojo, Verde, Azul)
screen.fill(color)



flecha = pygame.image.load("C:\Programacion 2\Pro_fisica\Flecha.png").convert()

ps_flecha = (700, 600)


for desplazar_y in range(0, 600, 50):
        pygame.draw.line(screen, (255, 0, 0), [500, 600 - desplazar_y], [500, 560 - desplazar_y], 5)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False          
    
    #Textos
    fuente = pygame.font.Font(None, 25)
    texto = fuente.render("Distancia", True, (255, 255, 0))
    screen.blit(texto, [1210, 710,] )
    
    fuente = pygame.font.Font(None, 25)
    texto = fuente.render("Distancia", True, (255, 255, 0))
    screen.blit(texto, [1210, 710,] )
    
    fuente = pygame.font.Font(None, 25)
    texto = fuente.render("Distancia", True, (255, 255, 0))
    screen.blit(texto, [1210, 710,] )
    
    #Pocicion de las cargas
    centro = ( 500, 600)
    centro2 = (centro[0]-121, centro[1]-144)
    centro3 = (centro[0], centro[1] - (c * 37.79527559055))
    
    #color de las cargas
    color_cargas = (0, 0, 255)
    
    #Dibujamos las cargas
    pygame.draw.circle(screen, color_cargas, centro3, 20)
    pygame.draw.circle(screen, color_cargas, centro2, 20)
    pygame.draw.circle(screen, color_cargas, centro, 20)

    #Dibujamos los lados
    pygame.draw.line(screen, color_cargas, centro, centro2, 5)    
    pygame.draw.line(screen, color_cargas, centro3, centro2, 5)    
    

    img = pygame.transform.rotate(flecha, C + math.degrees(180))
    img_rect = img.get_rect()
    img_rect.center=ps_flecha
    screen.blit(img, img_rect)
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()