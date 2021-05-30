import math

#constantes
k = 9*10**9

#Lados
a = 0
b = 0.5
c = (float(input("ingresar distancia de la particula")))

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


print (fq1)

print (fq3)

print ("EN x",fq3x)

print ("EN y",fq3y)
