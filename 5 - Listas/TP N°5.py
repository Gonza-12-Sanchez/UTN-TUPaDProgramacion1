#----EJERCICIO 1----
#Creamos una lista con los numeros del 1 al 100 que sean multiplos de 4 utilizando la funcion range.
lista_numeros = list(range(0,101,4))
#Modificamos el primer valor de la lista.
lista_numeros[0] = 1
#Mostramos la lista por pantalla.
print(lista_numeros)


#----EJERCICIO 2----
#Creamos una lista de 5 elementos.
lista_libros = ["Harry Potter","Game of thrones","El Caballero de la armadura oxidada","Habitos Atomicos","El poder del ahora"]
#Mostramos el penultimo elemento de la lista.
print(lista_libros[-2])


#----EJERCICIO 3----
#Creamos una lista vacia.
lista_vacia = []
#Agregamos tres elementos a la lista.
lista_vacia.append("Naranja")
lista_vacia.append("Banana")
lista_vacia.append("Manzana")
#Mostramos la lista por pantalla.
print(lista_vacia)


#----EJERCICIO 4----
#Creamos una lista con distintos animales.
animales = ["perro", "gato", "conejo", "pez"]
#Reemplazamos el segundo y el ultimo valor por las palabras "loro" y "oso".
animales[1] = "loro"
animales[-1] = "oso"
#Mostramos la lista por pantalla.
print(animales) 


#----EJERCICIO 5----
#Lo que se hace en el codigo dado es:
#1. Se crea una lista llamada "numeros" con 5 elementos de tipo int: 8,15,3,22,7.
#2. Se utiliza la funcion "remove" junto a la funcion "max" para quitar el maximo numero de la lista numeros.
#3. Muestra la lista resultante.


#----EJERCICIO 6----
#Creamos una lista con los numeros del 10 al 30 haciendo saltos de 5 en 5.
numeros = list(range(10,31,5))
#Mostramos por pantalla los 2 primeros elementos de la lista.
print(numeros[0:2])


#----EJERCICIO 7----
#Creamos una lista.
autos = ["sedan", "polo", "suran", "gol"]
#Reemplazamos los valores centrales de la lista.
autos[1] = "nissan"
autos[-2] = "corsa"
#Mostramos la lista.
print(autos)


#----EJERCICIO 8----
#Creamos una lista llamada "dobles".
dobles = []
#Le agregamos a la lista los dobles de 5, 10 y 15.
dobles.append(10)
dobles.append(20)
dobles.append(30)
#Mostramos la lista resultante.
print(dobles)


#----EJERCICIO 9----
#Creamos una matriz con distintos valores.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
#Agregamos la palabra "jugo" a la tercer lista.
compras[2].append("jugo")
#Reemplazamos "fideos" por "tallarines" en la segunda lista.
compras[1][1] = "tallarines"
#Eliminamos "pan" de la primera lista.
compras[0].remove("pan")
#Mostramos la matriz resultante.
for i in range(len(compras)):
    print(compras[i])


#----EJERCICIO 10----
#Creamos una lista llamada "lista_anidada" con diferentes valores.
lista_anidada = [15,True,[25.5,57.9,30.6],False]
#Mostramos la lista anidada por pantalla.
for i in range(len(lista_anidada)):
    print(lista_anidada[i])