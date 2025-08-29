#----EJERCICIO 1----
for a in range (101):
    print(a)


#----EJERCICIO 2----
num = int(input("Ingrese un numero entero: "))
cant_digitos = 0
aux = num
if num > 0:
    while aux >= 1:
        aux = aux / 10
        cant_digitos += 1
elif num == 0:
    cant_digitos = 1
else:
    while aux <= -1:
        aux = aux / 10
        cant_digitos += 1
print(f"{num} contiene {cant_digitos} digitos")


#----EJERCICIO 3----
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
sumatoria = 0
for i in range(num1 + 1, num2):
    sumatoria += i
print(f"La sumatoria de todos los valores comprendidos entre el {num1} y el {num2} es de {sumatoria}")


#----EJERCICIO 4----
num = 1
sumatoria = 0
while num != 0:
    num = int(input("Ingrese un numero para sumarlo (Ingrese 0 para terminar de sumar): "))
    sumatoria += num
print("La sumatoria de todos los numeros ingresados es de:", sumatoria)


#----EJERCICIO 5----
import random
num_correcto = random.randint(0,9)
cant_intentos = 0
num = 10
print("Juguemos a adivinar el numero (entre 0 y 9)")
while num != num_correcto:
    num = int(input("Ingrese un numero: "))
    cant_intentos += 1
print("Acerto!")
print("Cantidad de intentos:",cant_intentos)


#----EJERCICIO 6----
for i in range (100,-1,-2):
    print(i)


#----EJERCICIO 7----
sumatoria = 0
num = int(input("Ingrese un numero entero positivo: "))
while num < 1:
    num = int(input("Numero invalido. Ingrese otro: "))
for i in range (1,num + 1):
    sumatoria += i
print(f"La sumatoria de todos los numeros comprendidos entre el 0 y el {num} es de {sumatoria}")


#----EJERCICIO 8----
pares = 0
impares = 0
negativos = 0
positivos = 0
print("Ingrese numeros enteros")
for i in range (100):
    num = int(input())
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print("**************")
print("Pares:",pares)
print("Impares:",impares)
print("Negativos:",negativos)
print("Positivos:",positivos)


#----EJERCICIO 9----
sumatoria = 0
print("Ingrese numeros enteros")
for i in range(100):
    num = int(input())
    sumatoria += num
media = sumatoria / 100
print("La media de los numeros ingresados es de",media)


#----EJERCICIO 10----
num = int(input("Ingrese un numero: "))
aux = num
num_invertido = 0
while aux >= 1:
    digito = aux % 10
    aux = aux // 10
    num_invertido = num_invertido * 10 + digito
print(f"{num} invertido es {num_invertido}") 