#----EJERCICIOS----
#DEFINICION DE FUNCIONES.
def mostrar_productos():
    #Leemos y mostramos los productos del archivo "productos".
    with open("productos.txt","r") as archivo:
        print("---- PRODUCTOS ----")
        #Recorremos las lineas del archivos, y las mostramos por pantalla.
        for linea in archivo:
            linea = linea.strip()
            producto = linea.split(",")
            print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")

def ingresar_nuevo_producto():
    #Solicitamos al usuario que ingrese un nuevo producto.
    print("--INGRESE UN NUEVO PRODUCTO--")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    #Juntamos toda la informacion en una variable.
    producto = nombre + "," + "$" + precio + "," + cantidad + "\n"
    #Agregamos dicho producto al archivo, sin borrar nada.
    with open("productos.txt","a") as archivo:
        archivo.write(producto)

def cargar_productos_lista_diccionarios():
    #Cargamos los datos del archivo en una lista de diccionarios.
    productos = []
    with open("productos.txt","r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            informacion_producto_lista = linea.split(",")
            productos.append({"Nombre":informacion_producto_lista[0],"Precio":informacion_producto_lista[1],"Cantidad":informacion_producto_lista[2]})
    return productos

def buscar_producto_por_nombre(productos):
    #Solicitamos al usuario que ingrese un nombre de un producto.
    nombre_producto = input("INGRESE EL NOMBRE DEL PRODUCTO A BUSCAR: ")
    existe = False
    #Verificamos si dicho producto existe.
    for producto in productos:
        if nombre_producto == producto["Nombre"]:
            print("Producto encontrado!")
            print("La informacion sobre el producto es la siguiente:")
            print(f"Producto: {producto["Nombre"]} | Precio: {producto["Precio"]} | Cantidad: {producto["Cantidad"]}")
            existe = True
    if existe == False:
        print("Error. Producto no encontrado")

def guardar_productos_actualizados(productos):
    #Sobreescribimos los datos del archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
    with open("productos.txt","w") as archivo:
        for producto in productos:
            producto = producto["Nombre"] + "," + producto["Precio"] + "," + producto["Cantidad"] + "\n"
            archivo.write(producto)

#PROGRAMA PRINCIPAL.
#Creamos un archivo y agregamos 3 productos iniciales.
with open("productos.txt","w") as archivo:
    archivo.write("Manzana,$100,10\n")
    archivo.write("Banana,$80,5\n")
    archivo.write("Melon,$200,15\n")
#Cargamos los productos en un lista y mostramos los productos iniciales.
productos = cargar_productos_lista_diccionarios()
mostrar_productos()
#Creamos un mini menu para el usuario.
while True:
    print("*****MENU*****")
    print("1. Mostrar productos")
    print("2. Agregar productos")
    print("3. Buscar producto por nombre")
    print("4. Salir")
    opcion = input()
    #Verificamos la opcion.
    while opcion not in "1234":
        print("Opcion incorrecta. Ingrese otra")
        opcion = input()
    #Realizamos la opcion seleccionada.
    if opcion == "1":
        mostrar_productos()
    elif opcion == "2":
        ingresar_nuevo_producto()
        productos = cargar_productos_lista_diccionarios()
    elif opcion == "3":
        buscar_producto_por_nombre(productos)
    else:
        print("Archivo de productos actualizado!")
        print("Hasta luego!!")
        break
#Guardamos los productos actualizados en el archivo.
guardar_productos_actualizados(productos)