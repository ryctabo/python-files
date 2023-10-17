'''
Ingreso de pacientes con los siguientes datos:
- código del paciente
- nombre del paciente
    - apellido paterno
    - apellido materno
- sintoma
El ingreso de estos datos es a través de un archivo CSV
'''

import csv

data_list = []

def add_patient():
    print('-'*90)
    code = input("Ingresa el código del paciente: ")
    name = input("Ingresa el nombre del paciente: ")
    lastname = input("Ingresa el apellido paterno del paciente: ")
    mother_lastname = input("Ingresa el apellido materno del paciente: ")
    symptoms = input("Ingresa los sintomas del paciente: ")
    print('-'*90)

    data = { 
        "code": code, 
        "firstname": name,
        "lastname": lastname, 
        "mother_lastname": mother_lastname, 
        "symptoms": symptoms 
    }

    data_list.append(data)

    save_data_to_csv()

def save_data_to_csv():
    try:
        filename = 'health-manager.csv'
        with open(filename, 'w') as csv_file:
            columns = ['code', 'firstname', 'lastname', 'mother_lastname', 'symptoms']
            writer = csv.DictWriter(csv_file, columns)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)
        print(f"Se ha guardado el paciente perfectamente en el archivo csv: {filename}")
    except Exception as e:
        print(f"Se ha producido un error al guardar la información en el archivo CSV: {e}")

while True:
    print('-'*90)
    print("(1) Agregar un nuevo paciente")
    print("(2) Salir")
    option = input("Selecciona una opción: ")
    print('-'*90)

    if option == '2':
        print("Saliendo del programa...")
        break
    if option == '1':
        add_patient()
