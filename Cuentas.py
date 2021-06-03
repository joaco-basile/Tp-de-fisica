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


#teorema de coseno para el lado
a = math.sqrt(((b**2) - 2*b*c*math.cos(A) + (c**2) ))


#Teorema de coseno y de pitagoras para los angulos
#Sacamos el angulo de arriba
B = math.degrees(math.acos((0.5 * a**2 - 0.5 * b**2 + 0.5 * c**2) / (a*c)))

#Sacamos el angulo de la izquierda
A = math.degrees(A)
C = 180 - (A + B) 



# Calculamos fuerzas totales
f12 = round((k * ((q1*10**-4 * q2*10**-4) / c**2)),2)
f21 = f12 * -1


f32 = round((k * ((q3*10**-4 * q2*10**-4) / a**2)),2)
f23 = f32 *-1

# Calculamos fuerzas en x e y
angulo_q3_int = 180 - (90 + 50)
angulo_q3_ext = C - angulo_q3_int


f32x = (math.cos (angulo_q3_ext)) * f32
f32y = (math.sin (angulo_q3_ext)) * f32

f2yt = f32y + f12

f23x = f32x * -1
f23y = f32y * -1




print("lado a :", a)
print("lado b :", b)
print("lado c :", c)
print("angulo A", A)
print("angulo B:", B)
print("angulo C:", C)
print("angulo angulo externo:", angulo_q3_ext)
print("Fuerza f12:", f12)
print("Fuerza f32", f32)
print("Fuerza 32x", f32x)
print("Fuerza 32y", f32y)
print("Fuerza 32yt", f2yt)
print("Fuerza f21:", f21)
print("Fuerza f23", f23)
print("Fuerza 23x", f23x)
print("Fuerza 23y", f23y)

