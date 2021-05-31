
import math

#constantes
k = 9*10**9

#Lados
a = 0
b = 5

c = (float(input("ingresar distancia de la particula: ")))

#angulos
A = math.radians(50)
B = math.degrees(0)
C = math.degrees(0)

#cargas
q1 = float(input("Escriba la carga 1: "))
q2 = float(input("Escriba la carga 2: "))
q3 = float(input("Escriba la carga 3: "))

#fuerza sobre carga 2

#teorema de coseno para el lado
a = (b**2-2*b*c*math.cos(A)+c**2)**0.5


#Teorema de coseno y de pitagoras para los angulos
#Sacamos el angulo de arriba
B = math.degrees(math.acos((0.5 * a**2 - 0.5 * b**2 + 0.5 * c**2) / (a*c)))

#Sacamos el angulo de la izquierda
A = math.degrees(A)
C = 180 - (A + B) 

#Pasamos la distancia a m
c = c/1000
a = a/100


# Calculamos fuerzas totales
f12 = round((k * ((q1*10**-6 * q2*10**-6) / c**2)),2)
f21 = f12 * -1


f32 = round((k * ((q3*10**-6 * q2*10**-6) / a**2)),2)


# Calculamos fuerzas en x e y
angulo_q3_int = 180 - (90 + 50)
angulo_q3_ext = C - angulo_q3_int

f32x = round((math.cos (angulo_q3_ext)) * fq3),2)
f32y = round((math.sin (angulo_q3_ext)) * fq3),2)

f23x = f32x * -1
f23y = f32y * -1




print("lado a :", a)
print("angulo A", A)
print("angulo B:", B)
print("angulo C:", C)
print("Fuerza f12:", f12)
print("Fuerza f32", f32)
print("Fuerza 32x", f32x)
print("Fuerza 32y", f32y)

