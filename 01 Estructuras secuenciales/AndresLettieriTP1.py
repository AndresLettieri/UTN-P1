#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("¿Como te llamas? ")
print(f"Hola {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("¿Cual es tu primer nombre? ")
apellido = input("Cual es tu apellido? ")
edad = int(input("¿Cuantos años tenes? "))
residencia = input("¿Donde vivis? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área ysu perímetro.
import math

radio = float(input("Ingrese el radio de un circulo:" ))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar de {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingresa primer numero entero distinto de 0: "))

while numero1 == 0:
    numero1 = int(input("El numero tiene que ser distinto de 0. Ingresa nuevamente: "))
    
numero2 = int(input("Ingresa segundo numero entero distinto de 0: "))

while numero2 == 0:
    numero2 = int(input("El numero tiene que ser distinto de 0. Ingresa nuevamente: "))
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    print(f"Suma: {numero1} + {numero2} = {suma}")
    print(f"Resta: {numero1} - {numero2} = {resta}")
    print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
    print(f"División: {numero1} / {numero2} = {division}")


#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Igrese su altura: "))
peso = float(input("Igrese su peso: "))
masa = peso / (altura ** 2)
print(f"Su masa corporal es {masa}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit

celcius = float(input("Igrese grados celcius a convertir: "))
fahrenheit = (9/5 * celcius) + 32
print(f"{celcius} grados celcius equivalen a {fahrenheit} grados fahrenheit")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
# Pedir al usuario 3 números

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio de los 3 números
promedio = (numero1 + numero2 + numero3) / 3

# Imprimir el resultado
print(f"El promedio de los tres números es {promedio}")
