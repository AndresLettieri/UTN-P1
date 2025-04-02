#1)
edad = int(input("¿Cuantos años tenes? "))
#si bien el enunciado indica mayor de 18, la mayoria de edad se podria interpretar como mayor o igual a 18
if edad >= 18: 
    print("!Sos mayor de edad!")

#2)
nota = float(input("Ingresa tu nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3)
numero = int(input("Ingrese un número:"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print( "Por favor, ingrese un número par")

#4)
edad = int(input("¿Cuantos años tenes? "))

if edad < 12:
    print("Sos un niño.")
elif edad >= 12 and edad < 18:
    print("Sos un adolescente.")
elif edad >= 18 and edad < 30:
    print("Sos un adulto/a joven.")
elif edad >= 30:
    print("Sos un adulto/a.")

#5)
password = input("Ingrese una contraseña que contenga entre 8 y 14 carateres: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)
from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculate the mode, median, and mean
moda = mode(numeros_aleatorios)
mediana =median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana:
    sesgo = "positivo"
elif media < mediana:
    sesgo = "negativo"
else:
    sesgo = "no hay sesgo"

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Sesgo: {sesgo}")

#7)
frase  = input("Ingrese una frase o palabra: ")

if frase[-1].upper() == "A" or frase[-1].upper() == "E" or frase[-1].upper() == "I" or frase[-1].upper() == "O" or frase[-1].upper() == "U":
    print(f"{frase}!")
else:
    print(f"{frase}")

#8)
nombre  = input("Ingrese su nombre: ")
print("Ingrese 1 si quiere su nombre en mayúsculas")
print("Ingrese 2 si quiere su nombre en minúsculas")
print("Ingrese 3 si quiere su nombre con la primera letra mayúscula")
opcion = int(input("Ingrese opción: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#9)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10)
hemisferio = input("¿En que hemisferio estas? Ingrese N para norte y S para sur: ").strip().upper()
mes = int(input("Ingrese en que mes del año está: "))
dia = int(input("¿Que día del mes es? "))


if (mes == 12 and dia >= 21) or mes <= 2 or (mes == 3 and dia <= 20):
    if hemisferio == "S":
        estacion = "Verano"  
    else: 
        estacion = "Invierno"
elif (mes == 3 and dia >= 21) or mes <= 5  or (mes == 6 and dia <= 20):
    if hemisferio == "S":
        estacion = "Otoño"  
    else: 
        estacion = "Primavera"
elif (mes == 6 and dia >= 21) or mes <= 8 or (mes == 9 and dia <= 20):
    if hemisferio == "S":
        estacion = "Invierno"  
    else: 
        estacion = "Verano"
elif (mes == 9 and dia >= 21) or mes <= 11 or (mes == 12 and dia <= 20):
    if hemisferio == "S":
        estacion = "Primavera"  
    else: 
        estacion = "Otoño"

print(f"Te encuentras en la estación: {estacion}.")