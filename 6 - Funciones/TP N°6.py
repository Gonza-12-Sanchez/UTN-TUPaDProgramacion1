#----EJERCICIO 1----
#Definicion de funciones.
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Programa principal.
imprimir_hola_mundo()


#----EJERCICIO 2----
#Definicion de funciones.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#Programa principal.
saludar_usuario(input("Ingrese su nombre: "))


#----EJERCICIO 3----
#Definicion de funciones.
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Programa principal.
print("****Ingrese los siguientes datos personales****")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
residencia = input("Residencia: ")
informacion_personal(nombre,apellido,edad,residencia)


#----EJERCICIO 4----
#Importamos la libreria a utilizar.
import math
#Definicion de funciones.
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
#Programa principal.
radio = float(input("Ingrese el radio de un circulo: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")


#----EJERCICIO 5----
#Definicion de funciones.
def segundos_a_horas(segundos):
    return  round(segundos / 3600,4) #--> Redondeo a 4 decimales.
#Programa principal.
print("****SEGUNDOS A HORAS****")
segundos = int(input("Ingrese los segundos: "))
while segundos <= 0:
    print("Los segundos deben ser positivos.....")
    segundos = int(input())
print(f"{segundos} segundos son {segundos_a_horas(segundos)} hr/hrs")


#----EJERCICIO 6----
#Definicion de funciones.
def tabla_multiplicar(num):
    print(f"****TABLA DEL {num}****")
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
#Programa principal.
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)


#----EJERCICIO 7----
#Definicion de funciones.
def operaciones_basicas(a,b):
    tupla = []
    tupla.append(a+b)
    tupla.append(a-b)
    tupla.append(a*b)
    tupla.append(a/b)
    tupla = tuple(tupla)
    return tupla
#Programa principal.
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
tupla_resultados = operaciones_basicas(num1,num2)
print(f"****OPERACIONES BASICAS CON {num1} Y {num2}****")
print(f"SUMA = {tupla_resultados[0]}")
print(f"RESTA = {tupla_resultados[1]}")
print(f"MULTIPLICACION = {tupla_resultados[2]}")
print(f"DIVISION = {tupla_resultados[3]}")


#----EJERCICIO 8----
#Definicion de funciones.
def calcular_imc(peso,altura):
    return round(peso / (altura**2),2)
#Programa principal.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su indice de masa corporal es de {calcular_imc(peso,altura)}")


#----EJERCICIO 9----
#Definicion de funciones.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#Programa principal.
temperatura = float(input("Ingrese la temperatura en grados celsius: "))
print(f"{temperatura}°C son {celsius_a_fahrenheit(temperatura)}°F")


#----EJERCICIO 10----
#Definicion de funciones.
def calcular_promedio(a,b,c):
    return (a+b+c) / 3
#Programa principal.
val1 = int(input("Ingrese un numero: "))
val2 = int(input("Ingrese otro numero: "))
val3 = int(input("Ingrese otro numero: "))
print(f"El promedio de {val1}, {val2} y {val3} es de {calcular_promedio(val1,val2,val3)}")