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

def create_product():
    product = {}
    product["code"] = input("Código del producto: ")
    product["name"] = input("Nombre del producto: ")
    product["category"] = input("Categoria del producto: ")
    product["quantity"] = input("Cantidad: ")
    product["price"] = input("Precio unitario: ")
    product_list.append(product)
    print()

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
    print("1. Agregar un producto")
    print("2. Consultar un producto")
    print("3. Salir")

    option = input("Selecciona una opción: ")

    if option == "3":
        print("Good bye! :)")
        break

    if option == "1":
        create_product()

    if option == "2":
        find_all_products()
