'''
1/ Crear un programa que permita
ingresar "PRODUCTOS" de una tienda
en un diccionario desde el teclado

2/ El programa debe permitir consultar
todos los productos en el inventario

CAMPOS
- Codigo_producto
- Nombre_producto
- Categoria_producto
- Cantidad
- Valor_unitario
'''

product_list = []

# 1. crear un diccionario llamado product
# 2. llenar los datos necesarios dentro del diccionario product
# 3. agregar el diccionario creado dentro de una lista
def create_product():
    product = {}
    product["code"] = input("Código del producto: ")
    product["name"] = input("Nombre del producto: ")
    product["category"] = input("Categoria del producto: ")
    product["quantity"] = input("Cantidad: ")
    product["price"] = input("Precio unitario: ")
    product_list.append(product)
    print()

# 1. preguntando si la lista tiene elementos
# 1.a si no tiene elementos imprimir la frase "La lista está vacia."
# 2. recorrer la lista de productos e imprimir cada uno de los valores que tiene el diccionario
def find_all_products():
    if len(product_list) == 0:
        print("La lista está vacia.")
    else:
        for product in product_list:
            print("---")
            print("Código del producto: " + product["code"])
            print("Nombre del producto: " + product["name"])
            print("Categoria del producto: " + product["category"])
            print("Cantidad de producto: " + product["quantity"])
            print("Precio del producto: " + product["price"])
    print()

while True:
    # 1. creando un menú para administrar la lista de productos
    print("1. Agregar un producto")
    print("2. Consultar un producto")
    print("3. Salir")

    # 2. preguntando por una opción
    option = input("Selecciona una opción: ")

    # 3. Salimos del programa?
    if option == "3":
        print("Good bye! :)")
        break

    # Creamos productos?
    if option == "1":
        create_product()

    # Consultamos todos los productos agregados?
    if option == "2":
        find_all_products()
