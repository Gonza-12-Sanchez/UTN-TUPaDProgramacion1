#----EJERCICIO 1----
edad = int(input("Ingrese su edad: "))
if edad > 18: 
    print("Es mayor de edad")


#----EJERCICIO 2----
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#----EJERCICIO 3----
numero = int(input("Ingrese solo un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#----EJERCICIO 4----
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria Adolescente")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria Adulto/a joven")
else:
    print("Usted pertenece a la categoria Adulto/a")


#----EJERCICIO 5----
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#----EJERCICIO 6----
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios) 
#La moda o "mode" son los numeros mas repetidos en un conjunto de numeros
mediana = median(numeros_aleatorios)
#La mediana o "median" retorna el valor central de un conjunto de numeros
media = mean(numeros_aleatorios)
#La media o "mean" es el promedio de un conjunto de numeros

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No hay sesgo indentificable")

print(f"media: {media}, mediana: {mediana}, moda: {moda}")


#----EJERCICIO 7----
palabra = input("Ingrese una palabra o frase: ").lower()
ultima_letra = int(len(palabra) - 1) 
#"in" es un operador de pertenencia, en este caso verifica si la ultima letra pertenece al string "aeiou"
if palabra[ultima_letra] in "aeiou":
    print(palabra + "!")
else:
    print(palabra)


#----EJERCICIO 8----
nombre = input("Ingrese su nombre: ")
print("**Elija una opcion**")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input())
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no reconocida")


#----EJERCICIO 9----
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3:
    print(f"La magnitud {magnitud} se encuentra en la categoria: muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print(f"La magnitud {magnitud} se encuentra en la categoria: leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print(f"La magnitud {magnitud} se encuentra en la categoria: moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print(f"La magnitud {magnitud} se encuentra en la categoria: fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print(f"La magnitud {magnitud} se encuentra en la categoria: muy fuerte (puede causar daños significativos)")
else:
    print(f"La magnitud {magnitud} se encuentra en la categoria: extremo (puede causar graves daños a gran escala)")


#----EJERCICIO 10----
hemisferio = input("¿En que hemisferio se encuentra? (Norte = N/ Sur = S): ").lower()
mes = int(input("¿Que mes del año es? (Ingrese el numero del mes): "))
dia = int(input("¿Qu dia es? (Ingrese el numero del dia): "))
if (dia >= 21 and mes == 12) or (mes == 1 or mes == 2) or (dia <=20 and mes == 3):
    Estacion_H_N = "Invierno"
    Estacion_H_S = "Verano"
elif (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
    Estacion_H_N = "Primavera"
    Estacion_H_S = "Otoño"
elif (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9):
    Estacion_H_N = "Verano"
    Estacion_H_S = "Invierno"
elif (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
    Estacion_H_N = "Otoño"
    Estacion_H_S = "Primavera"

if hemisferio == "n" and (dia < 32 and dia > 0) and (mes > 0 and mes < 13):
    print("Usted se encuentra en",Estacion_H_N)
elif hemisferio == "s" and (dia < 32 and dia > 0) and (mes > 0 and mes < 13): 
    print("Usted se encuentra en",Estacion_H_S)
else:
    print("Hemisferio, mes o dia ingresados incorrectamente!")