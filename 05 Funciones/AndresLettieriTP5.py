#1

def imprimir_hola_mundo():
    print("Hola Mundo!")

def main():    
    imprimir_hola_mundo()

main()

#2
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

def main():
    nombre = input("Como te llamas? ")
    saludar_usuario(nombre)   

main()

#3
def informacion_personal(nombre, apellido, edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def main():
    nombre = input("Como es tu nombre? ")
    apellido = input("Como es tu apellido? ")
    edad = int(input("Cuantos años tenes? "))
    residencia = input("Donde vivis? ")
    informacion_personal(nombre, apellido, edad, residencia)

main()

#4
def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

def main():
    radio = float(input("Ingresar el radio del círculo a calcular: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area}")
    print(f"El perímetro del círculo es: {perimetro}")

main()

#5
def segundos_a_horas(segundos):
    return segundos / 3600

def main():
    segundos = int(input("Ingrese la cantidad de segundos a transfomar en horas: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos son {horas} horas")

main()

#6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingrese un número: "))
    tabla_multiplicar(numero)

main()

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else: 
        division = "Error: División por cero"
    
    return suma, resta, multiplicacion, division

def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

main()

#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    
    print(f"Su IMC es: {imc:.2f}")

main()

#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def main():
    celsius = float(input("Ingresa la temperatura en celsius a transformar: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} celsius son {fahrenheit} fahrenheit")

main()

#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def main():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    
    promedio = calcular_promedio(a, b, c)
    
    print(f"El promedio es: {promedio}")