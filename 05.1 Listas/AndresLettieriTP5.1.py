#1
mi_lista = list(range(4, 101, 4))
print(mi_lista)

#2
mi_lista = ["Acosta","Romeo","Torrico","Romagnoli","Silas"]
print(mi_lista[-2])

#3
lista_vacia = []
lista_vacia.append("Acosta")
lista_vacia.append("Romeo")
lista_vacia.append("Torrico")
print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1]= "oso"
print(animales)

#5
#Se elimina de la lista el valor numerico maximo. En este caso, el 22.

#6
mi_lista = list(range(10, 31, 5))
print(mi_lista[0:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["punto", "307"]
print(autos)

#8
dobles = []
for i in range(5, 16,5):
    dobles.append(i * 2)

print (dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "manteca"
compras[0].remove("pan")
print(compras)

#10
lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5,57.9,30.6])
lista_anidada.append(False)
print(lista_anidada)
