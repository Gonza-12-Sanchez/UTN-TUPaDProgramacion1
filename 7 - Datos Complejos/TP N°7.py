#----EJERCICIO 1, 2 Y 3----
#METODOS DE MOSTRAR LOS DICCIONARIO POR PANTALLA.
#for clave in precios_frutas:
#    print(f"{clave} = ${precios_frutas[clave]}")
#
#for clave,valor in precios_frutas.items():
#    print(f"{clave} = ${valor}")
#Definimos e inicializamos un diccionario.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
print(f"FRUTAS ORIGINALES: {precios_frutas}")
#Agregamos otras frutas al diccionario con sus respectivos precios.
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
#Mostramos el diccionario actualizado por pantalla.
print(f"FRUTAS ACTUALIZADAS: {precios_frutas}")
#Actualizamos el precio de algunas frutas.
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
#Mostramos el diccionario con los precios autualizados.
print(f"PRECIO DE FRUTAS ACTUALIZADAS: {precios_frutas}")
#Creamos una lista unicamente con las keys del diccionario.
lista_frutas = list(precios_frutas.keys())
#Mostramos la lista por pantalla.
print(f"LISTA DE FRUTAS: {lista_frutas}")


#----EJERCICIO 4----
#Definiciones.
numeros_telefonicos = {}
#Solicitamos al usuario que ingrese el nombre y numero del contacto telefonico.
print("---ALMACENAMIENTO DE NUMEROS TELEFONICOS---")
for i in range(5):
    print(f"Ingrese el nombre del {i+1} contacto:")
    nombre = input()
    print("Ingrese su numero:")
    numero = int(input())
    numeros_telefonicos[nombre] = numero
#Seguido solicitamos un nombre, y si existe, se mostramos el numero asociado.
nombre_consultar = input("Ingrese un nombre para consultar su numero: ")
if nombre_consultar in numeros_telefonicos:
    print(f"El numero de {nombre_consultar} es {numeros_telefonicos[nombre_consultar]}")
else:
    print(f"{nombre_consultar} no existe en los contactos...")


#----EJERCICIO 5----
#Definiciones.
recuento = {}
#Solicitamos al usuario que ingrese una frase.
frase = input("Ingrese una frase: ")
#Transformamos la frase en una lista para poder recorrerla, y contar las palabras repetidas.
lista_frase = list(frase.split(" "))
#Convertimos dicha lista en un conjunto para obtener las palabras unicas.
palabras_unicas = set(lista_frase)
#Con la ayuda de un ciclo for recorremos toda la lista para contar las veces que se repiten las palabras.
for i in range(len(lista_frase)):
    if lista_frase[i] not in recuento:
        recuento[lista_frase[i]] = 1
    else:
        recuento[lista_frase[i]] += 1
#Mostramos las palabras unicas, y un diccionario con la cantidad de veces que aparece cada palabra.
print(f"PALABRAS UNICAS DE LA FRASE INGRESADA: {palabras_unicas}")
print(f"CANTIDAD DE VECES QUE APARECE CADA PALABRA: {recuento}")


#----EJERCICIO 6----
#Definiciones.
alumnos = {}
#Solicitamos al usuario que ingrese el nombre y las notas de los alumnos.
for a in range(3):
    print(f"---ALUMNO {a+1}---")
    nombre = input("Nombre: ")
    notas = []
    for b in range(3):
        print(f"Nota {b+1}:")
        nota = int(input())
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
#Mostramos el promedio de cada alumno.
print("---PROMEDIO ALUMNOS---")
for alumno,notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{alumno} = {promedio}")


#----EJERCICIO 7----
#Definimos dos diccionarios de estudiantes aprobados en distintos parciales.
estudiantes = {
    "Parcial 1": {"Juan","Rodrigo","Pepe","Setch"},
    "Parcial 2": {"Pepe","Maria","Ana","Juan"}
}
#Mostramos los estudiantes que aprobaron en ambos parciales.
print(f"Alumnos aprobados en parcial 1 y 2: {estudiantes["Parcial 1"].intersection(estudiantes["Parcial 2"])}")
#Mostramos los estudiantes que aprobaron solo un parcial de los dos.
print(f"Alumnos que aprobaron solo el PRIMER parcial: {estudiantes["Parcial 1"].difference(estudiantes["Parcial 2"])}")
print(f"Alumnos que aprobaron solo el SEGUNDO parcial: {estudiantes["Parcial 2"].difference(estudiantes["Parcial 1"])}")
#Mostramos el total de los estudiantes que aprobaron al menos uno de los dos parciales.
print(f"Alumnos que aprobaron AL MENOS un parcial: {estudiantes["Parcial 1"].union(estudiantes["Parcial 2"])}")


#----EJERCICIO 8----
#Definimos dos diccionarios de estudiantes aprobados en distintos parciales.
estudiantes = {
    "Parcial 1": {"Juan","Rodrigo","Pepe","Setch"},
    "Parcial 2": {"Pepe","Maria","Ana","Juan"}
}
#Mostramos los estudiantes que aprobaron en ambos parciales.
print(f"Alumnos aprobados en parcial 1 y 2: {estudiantes["Parcial 1"].intersection(estudiantes["Parcial 2"])}")
#Mostramos los estudiantes que aprobaron solo un parcial de los dos.
print(f"Alumnos que aprobaron solo el PRIMER parcial: {estudiantes["Parcial 1"].difference(estudiantes["Parcial 2"])}")
print(f"Alumnos que aprobaron solo el SEGUNDO parcial: {estudiantes["Parcial 2"].difference(estudiantes["Parcial 1"])}")
#Mostramos el total de los estudiantes que aprobaron al menos uno de los dos parciales.
print(f"Alumnos que aprobaron AL MENOS un parcial: {estudiantes["Parcial 1"].union(estudiantes["Parcial 2"])}")


#----EJERCICIO 9----
#Creamos un diccionario agenda.
agenda = {
    ("miercoles","00:55"): "Jugar al League of legends",
    ("jueves","06:00"): "Jugar al Minecraft",
    ("jueves","19:00"): "Comer (opcional)"
}
#Solicitamos al usuario que ingrese un dia y una hora.
print("****AGENDA****")
dia = input("Ingrese un dia de la semana: ").lower()
hora = input("Ingrese una hora: ")
#Convertimos la informacion ingresada en tupla.
tupla_fecha = (dia,hora)
#Verificamos si en ese dia y hora tiene algo en la agenda.
if tupla_fecha in agenda:
    print(f"El dia {dia} en la hora {hora} usted tiene que {agenda[tupla_fecha]}")
else:
    print("Usted no tiene nada agendado para esa fecha en la agenda......")


#----EJERCICIO 10----
#Definimos un diccionario vacio.
capitales_y_paises = {}
#Creamos un diciconario de paises y capitales.
paises_y_capitales = {
    "Peru":"Lima",
    "Mexico":"Ciudad de Mexico",
    "Argentina":"Buenos Aires",
    "Chile":"Santiago de Chile"
}
#Invertimos el diccionario original.
for pais, capital in paises_y_capitales.items():
    capitales_y_paises[capital] = pais
#Mostramos el resultado
print(f"DICCIONARIO ORIGINAL: {paises_y_capitales}")
print(f"DICCIONARIO INVERTIDO: {capitales_y_paises}")