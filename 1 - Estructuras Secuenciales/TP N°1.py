#----EJERCICIO 1----
print("Hola Mundo")


#----EJERCICIO 2----
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#----EJERCICIO 3----
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugarResidencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")


#----EJERCICIO 4----
radio = int(input("Ingrese el radio de un circulo: "))
pi = float(3.1416)
area = float(pi * radio ** 2)
perimetro = float(2 * pi * radio)
print(f"El area del circulo es {area}, y su perimetro es {perimetro}")


#----EJERCICIO 5----
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = int(segundos * 1 / 3600)
print(f"{segundos} segundos equivale a {horas} hr/hrs")


#----EJERCICIO 6----
numero = int(input("Ingrese un numero: "))
for i in range(1,11,1):
    multiplicacion = int(numero * i)
    print(f"{numero} x {i} = {multiplicacion}")


#----EJERCICIO 7----
nro1 = int(0)
nro2 = int(0)
while nro1 <= 0 or nro2 <= 0:
    print("Ingrese dos numeros enteros distintos de 0")
    nro1 = int(input("Valor 1: "))
    nro2 = int(input("Valor 2: "))
print("**************************") 
print(f"{nro1} + {nro2} = {int(nro1 + nro2)}")
print(f"{nro1} - {nro2} = {int(nro1 - nro2)}")
print(f"{nro1} / {nro2} = {float(nro1 / nro2)}")
print(f"{nro1} x {nro2} = {int(nro1 * nro2)}")


#----EJERCICIO 8----
altura = float(input("Ingrese su altura (en metros): "))
peso = int(input("Ingrese su peso (en kg): "))
IndiceMasaC = float(peso / (altura ** 2))
print("Su indice de masa corporal es de: ",IndiceMasaC)


#----EJERCICIO 9----
celsius = int(input("Ingrese una cantidad de grados Celsius: "))
fahrenheit = float(9 / 5 * celsius + 32)
print(f"{celsius} grados celsius es igual a {fahrenheit} grados fahrenheit")


#----EJERCICIO 10----
nro1 = int(input("Valor 1: "))
nro2 = int(input("Valor 2: "))
nro3 = int(input("Valor 3: "))
promedio = float((nro1 + nro2 + nro3) / 3)
print("El promedio de los 3 numeros es de: ",promedio)