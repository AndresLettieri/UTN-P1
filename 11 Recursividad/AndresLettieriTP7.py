#1
def facto(num):
    return 1 if num == 0 else num * facto(num - 1)

def main():
    num = int(input("Ingrese un numero: "))
    result = facto(num)
    print(f"El factorial de {num} es {result}")

main()

#2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def main():
    n = int(input("Ingrese un numero: "))
    result = fibonacci(n)
    print(f"El {n} número de Fibonacci es {result}")

main()

#3
def potencia(n, m):
    return 1 if m == 0 else n * potencia(n, m - 1)

def main():
    n = int(input("Ingrese la base: "))
    m = int(input("Ingrese el exponente: "))
    result = potencia(n, m)
    print(f"{n} elevado a {m} es {result}")
main()

#4
def aBinario(n):
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    else:
        return str(aBinario(n//2)) + str(n%2)  

def main():
    n = int(input("Ingrese un numero positivo: "))
    while n < 0:
        print("El número debe ser positivo.")
        n = int(input("Ingrese un numero positivo: "))  

    result = aBinario(n)
    print(f"El número {n} en binario es {result}")

main()

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def main():
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

main()

#6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def main():
    n = int(input("Ingrese un número: "))
    result = suma_digitos(n)
    print(f"La suma de los dígitos de {n} es {result}")

main()

#7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
def main():
    n = int(input("Ingrese un número: "))
    result = contar_bloques(n)
    print(f"El número de bloques en {n} es {result}")

main()

#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

def main():
    numero = int(input("Ingrese un número: "))
    digito = int(input("Ingrese el dígito a encontrar: "))
    result = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {result} veces en el número {numero}")

main()