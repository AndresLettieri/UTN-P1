#1
for i in range(101):
    print(i)

#2
numero = int(input("Ingresa un número entero: "))
digitos = len(str(abs(numero)))
print(f"El número tiene {digitos} dígito(s).")


#3
primero = int(input("Ingresá el primer número: "))
segundo = int(input("Ingresá el segundo número: "))

while primero >= segundo:
    print("El primer número debe ser menor que el segundo.")
    primero = int(input("Ingresá el primer número: "))
    segundo = int(input("Ingresá el segundo número: "))

suma = 0

for i in range(primero + 1, segundo):
    suma += i

print(f"La suma es: {suma}")

#4
numero = int(input("Ingresá un número a sumar. Para terminar ingresá 0: "))
total = 0

while numero > 0:
    total += numero
    numero = int(input("Ingresá otro número a sumar. Para terminar ingresá 0: "))

print(f"La suma total es: {total}")


#5
import random

adivinar = random.randint(0, 9)
numero = int(input("Adivina el número entre 0 y 9: "))
intento = 1

while adivinar != numero:
    numero = int(input("Error! probá de nuevo: "))
    intento += 1

print(f"Adivinaste en {intento} intentos.")

#6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#7
fin = int(input("Ingresá un número entero positivo: "))
suma = 0
for i in range(1, fin):
    suma += i
print(f"La suma de los números entre 0 y {fin} es: {suma}")


#8
cantidad = 100  # Puedes cambiar a un número menor para pruebas
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

#9
cantidad = 100  # Cambia este valor si deseas probar con menos números
suma = 0

for _ in range(cantidad):
    num = int(input("Ingresa un número: "))
    suma += num

media = suma / cantidad
print(f"La media de los números ingresados es: {media}")

#10
numero = int(input("Ingresá un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print(f"El número invertido es: {invertido}")