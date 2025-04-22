#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3
frutas = list(precios_frutas.keys())
print(frutas)

#4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

#5
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio
    
#6
def verificar_balanceo(texto):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    if len(texto) % 2 == 1 or texto == "":
        return False
    
    for c in texto:
        if c in pares.values():
            pila.append(c)
        elif c in pares.keys():
            if not pila or pila[-1] != pares[c]:
                return False
            pila.pop()

    return not pila

# Ejemplo de uso
texto = input("Ingrese una cadena de texto: ")
print(verificar_balanceo(texto))  

#7
from collections import deque

class ColaBanco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
         return self.cola.popleft() if not self.esta_vacia() else "La cola está vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0 
    
    def siguiente_cliente(self):
        return self.cola[0] if not self.esta_vacia() else "La cola está vacía"

#8
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

#9
def invertir_lista_enlazada(lista):
    anterior = None
    actual = lista.cabeza

    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    lista.cabeza = anterior
