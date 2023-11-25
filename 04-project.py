'''
    TECHNOLOGY IN SOFTWARE DEVELOPMENT
        SEMESTER 1 - SECTION 4

            MEDIC RECORDS
    MANAGEMENT OF CLINICAL HISTORIES

                BY:

    - KAMERON HOLY HERNANDEZ PAUTT
    - KEVIN JESUS PACHECO GOMEZ
    - SAMUEL JESUS TORRES PUELLO
'''

#_________________________________________________________________________________________________________________________________________________________________________________#
# Importamos todas las bibliotecas que vamos a utilizar en nuestro codigo

import os       # Importamos la biblioteca 'os' para limpiar la pantalla
import csv      # Importamos la biblioteca 'csv' para trabajar con archivos CSV 
import shutil   # Importamos la biblioteca 'shutil' para la copia de archivos
import getpass  # Importamos la biblioteca 'getpass' para ocultar la contraseña de usuario

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para limpiar la pantalla

def clean_console():
    if os.name == 'nt':
        os.system('cls')    # Usamos 'os.system()' para ejecutar el comando 'cls', que borra la pantalla en sistemas Windows
    else:                   # De otro modo podemos usar:
        os.system('clear')  # El comando 'clear', que borra la pantalla en sistemas Unix (Linux y macOS)

# Solicitamos nuestra funcion para limpiar la pantalla
clean_console()

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una función para decorar el programa con caracteres ascii, para ello usaremos el siguiente encabezado: 'MEDICAL RECORDS MANAGEMENT'
def header():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Creamos un diccionario con los nombres de usuario, contraseña y el rol que van a desempeñar estos usuarios
users = [
    {
        'username': 'kameronjoly',
        'password': '1128063099',
        'role': 'admin'
    },
    {
        'username': 'kevinjesus',
        'password': '1002191923',
        'role': 'assistant'
    },
    {
        'username': 'samueljesus',
        'password': '1043647631',
        'role': 'doc'
    }
]

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para el menu de administrador
def admin_menu():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('║' + '-'*19 + ' ADMIN MENU ' + '-'*19 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create a new user' + ' '*27 + '║')
    print('║' + '(2) » Consult user data' + ' '*27 + '║')
    print('║' + '(3) » Update user data' + ' '*28 + '║')
    print('║' + '(4) » Delete users' + ' '*32 + '║')
    print('║' + '(5) » Data backup'  + ' '*33 + '║')
    print('║' + '(6) » Exit' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def add_users_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*14 + '  ( Create new user ) ' + ' '*14 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create a new user' + ' '*27 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

new_users = {}  # We create a dictionary for new users

# Definimos la función para crear nuevos usuarios
def add_users_data():

    header()        # We request our header
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*14 + '  ( Create new user ) ' + ' '*14 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '→ Enter a username to continue.' + ' '*19 + '║')
    print('║' + ' '*50 + '║')
    print('║' + '→ The password can be any combination of letters, ' + '║')
    print('║' + '  numbers, and symbols. Use minimun 8 characters. ' + '║')
    print('║' + ' '*50 + '║')
    print('║' + '→ Assign a user role (admin, assistant, doc).' + ' '*5 +'║')
    print('╚' + '═'*50 + '╝')

    # Usamos 'try' para manejar situaciones excepcionales o errores que puedan ocurrir durante la ejecución de un programa
    try:
        # Creamos los campos con los que el administrador podrá crear nuevos usuarios
        new_users['username'] = input(' » Username: ')
        new_users['password'] = input(' » Password: ')
        new_users['role'] = input(' » Role: ')
        print('═'*52)

        # Insertamos los nuevos usuarios en la lista
        users.append(new_users)

    # En caso de que se produzca algún error nos mostrará este mensaje
    except Exception as e:
        print(f' Error: {e}')
        print(' Please try again')
        print('═'*52)

    # Solicitamos nuestra función para guardar a los usuarios en el archivo csv
    save_users_to_csv()

# Definimos una función para guardar usuarios en un archivo CSV
# Modifica la función save_users_to_csv() de la siguiente manera:
def save_users_to_csv():
    try:
        filename_users = 'user-data.csv'
        with open(filename_users, 'w', newline='') as user_file_csv:  # Cambia 'a' a 'w'
            fieldnames = ['username', 'password', 'role']
            writer = csv.DictWriter(user_file_csv, fieldnames)

            writer.writeheader()
            writer.writerows(users)  # Utiliza writerows para escribir la lista completa de usuarios

        print(f'User data saved to {filename_users} successfully')
        print('═'*52)

    except Exception as e:
        print(f'Error: {e}')
        print('Unable to save user data to CSV')
        print('═'*52)

#Definimos una función para consultar los detos de los usuarios
def consult_users_data():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*14 + '( Consult user data )' + ' '*15 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult a user' + ' '*30 + '║')
    print('║' + '(2) » Consult all users' + ' '*27 + '║')
    print('║' + '(3) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una función para consultar los datos de un solo usuario
def view_a_user():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*20 + 'Users data' + ' '*20 + '║')
    print('╚' + '═'*50 + '╝')
    username = input(' Enter the username to consult: ')

    try:
        filename_users = 'user-data.csv'
        with open(filename_users, 'r', newline='') as user_file_csv:
            reader = csv.DictReader(user_file_csv)
            user_found = False   # Variable para rastrear si se encuentra al usuario

            for row in reader:
                if row['username'] == username:
                    user_found = True    # Marcamos que el usuario fue encontrado
                    print()
                    print('╔' + '═'*50 + '╗')
                    print(' '*15 + f'User {username} found' + ' '*14 )
                    print('╚' + '═'*50 + '╝')

                    for key, value in row.items():
                        print(f' {key}: {value}')
                    break   # Rompemos el ciclo una vez que se encuentra al usuario

            if not user_found:
                    print('╔' + '═'*50 + '╗')
                    print(' '*13 + f'User {username} not found' + ' '*12 )  # Mensaje en caso de que no se encuentre el usuario
                    print('╚' + '═'*50 + '╝')  
        print('═'*52)

    except Exception as e:
                print('\t'*9 + ' '*5 + ' An error ocurred while reading information from the file')
                print('═'*52)

# Definimos una funcion para consultar todos los usuarios
def view_all_users():
    try:
        filename_users = 'user-data.csv'
        with open(filename_users, 'r', newline='') as user_file_csv:
            reader = csv.DictReader(user_file_csv)

            # Agregamos algo de decoracion
            clean_console()
            print('╔' + '═'*50 + '╗')
            print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
            print('╠' + '═'*50 + '╣')
            print('║' + ' '*20 + 'Users data' + ' '*20 + '║')
            print('╚' + '═'*50 + '╝')
            print()

            # Iteramos los elementos del diccionario
            # Se imprimen los registros
            for row in reader:
                for key, value in row.items():
                    print(' ' + key, value)
                print()
        print('═'*52)

    except Exception as e:
        print('\t'*9 + ' '*5 + ' An error ocurred while reading information form the file')
        print('═'*52)

# Definimos la función para cambiar los credenciales del usuario
def change_credentials():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*14 + '( Change Credentials )' + ' '*14 + '║')
    print('╚' + '═'*50 + '╝')

    username = input(' Enter your current username: ')
    password = getpass.getpass(' Enter your current password: ')

    user_found = False
    for user in users:
        if user['username'] == username and user['password'] == password:
            user_found = True

            new_username = input(' Enter your new username: ')
            new_password = getpass.getpass(' Enter your new password: ')

            user['username'] = new_username
            user['password'] = new_password

            print(' Your credentials have been updated successfully')
            print('═'*52)
            save_users_to_csv()
            break

    if not user_found:
        print(' Incorrect username or password. Please try again')
        print('═'*52)

def delete_user_menu():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete user data' + ' '*28 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una función para eliminar usuarios del archivo CSV
def delete_user_from_csv(username):
    try:
        filename_users = 'user-data.csv'
        temp_filename = 'temp-user-data.csv'

        with open(filename_users, 'r', newline='') as user_file_csv, \
             open(temp_filename, 'w', newline='') as temp_file_csv:

            fieldnames = ['username', 'password', 'role']
            reader = csv.DictReader(user_file_csv)
            writer = csv.DictWriter(temp_file_csv, fieldnames)

            # Escribimos el encabezado en el nuevo archivo
            writer.writeheader()

            # Copiamos todos los usuarios excepto el que queremos eliminar al nuevo archivo
            for row in reader:
                if row['username'] != username:
                    writer.writerow(row)

        # Reemplazamos el archivo original con el nuevo archivo
        shutil.move(temp_filename, filename_users)

        print(f' User {username} deleted successfully from {filename_users}')
        print('═'*52)

    except Exception as e:
        print(f' Error {e}')
        print(' Unable to delete user from CSV')
        print('═'*52)

# Modificamos la función delete_users_data para usar la función delete_user_from_csv
def delete_users_data():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*15  + '  ( Delete users ) ' + ' '*15 + ' ║')
    print('╚' + '═'*50 + '╝')
    print(' Enter username to delete')
    username_to_delete = input(' » ')

    user_found = False
    for user in users:
        if user['username'] == username_to_delete:
            users.remove(user)
            user_found = True
            break

    if user_found:
        delete_user_from_csv(username_to_delete)
    else:
        print(f' User {username_to_delete} not found')
        print('═'*52)

# Definimos una funcion para el menu de hacer una copia de seguridad de datos
def backup():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*16  + ' ( Data backup ) ' + ' '*16 + ' ║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Make backup' + ' '*33 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para crear una copia de seguridad
def make_backup():
    try:
        print('╔' + '═'*50 + '╗')
        print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
        print('╠' + '═'*50 + '╣')
        print('║' + ' '*16  + ' ( Data backup ) ' + ' '*16 + ' ║')
        print('╚' + '═'*50 + '╝')

        print(' Enter the source path of the CSV file')
        source_path = input(' » ')
        print('═'*52)
        print(' Enter the backup path for the CSV file')
        backup_route = input(' » ')
        print('═'*52)

        shutil.copy2(source_path, backup_route)
        print(f'Successfully backed up {source_path} to {backup_route}')

    except FileNotFoundError:
        print(' Error: The file was not found')
        print(f' {source_path}')
        print('═'*52)

    except PermissionError:
        print(' Error: Permision denied when trying to copy')
        print(f' {source_path}')
        print('═'*52)

    except Exception as e:
        print(' Unexpected error')
        print(f' {e}')
        print('═'*52)

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu de asistente
def assistant_menu():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('║' + '-'*17 + ' ASSISTANT MENU ' + '-'*17 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create new patient record' + ' '*19 + '║')
    print('║' + '(2) » Consult patient data' + ' '*24 + '║')
    print('║' + '(3) » Update patient data' + ' '*25 + '║')
    print('║' + '(4) » Delete patient data' + ' '*25 + '║')
    print('║' + '(5) » Exit' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def add_patient_data_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*16  + ' ( Patient data ) ' + ' '*16 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create new patient record' + ' '*19 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Creamos una lista vacia para almacenar los datos
data_list = []

# Definimos la funcion para crear o añadir pacientes nuevos
def add_patient_data():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*16  + ' ( Patient data ) ' + ' '*16 + '║')
    print('╚' + '═'*50 + '╝')
    id = input(' » Id: ')
    name = input(' » Names: ')
    lastname = input(' » Surnames: ')
    age = input(' » Age: ')
    gender = input(' » Gender: ')
    address = input(' » Address: ')
    phone = input(' » Phone number: ')
    health_coverage = input(' » Health coverage: ')
    print('═'*52)

    # Los datos de los pacientes son almacenas en un diccionario
    data = {
            'Identification': id,
            'Names': name,
            'Surnames': lastname,
            'Age': age,
            'Gender': gender,
            'Address': address,
            'Phone number': phone,
            'Health coverage': health_coverage
    }

    # Insertamos el diccionario dentro de la lista 'data_list' para poder guardar multiples registros
    data_list.append(data)
    save_data_to_csv()

# Definimos una funcion para guardar los datos en un archivo CSV
def save_data_to_csv():
    try:
        filename = 'patient-data.csv'
        with open(filename, 'a', newline='') as csv_file:
            columns = ['Identification', 'Names', 'Surnames', 'Age', 'Gender', 'Address', 'Phone number', 'Health coverage']
            writer = csv.DictWriter(csv_file, columns)

            # Si el archivo esta vacio, se escribira la cabecera o encabezado
            if csv_file.tell() == 0:
                writer.writeheader()

            for data in data_list:
                writer.writerow(data)

        # Cuando el archivo se guarde correctamente nos mostrara este mensaje:
        print(f'\t'*10 +' The patient has been saved perfectly in the file')
        print('═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algun error, se mostrar este mensaje:
        print(' An error occurred while saving information to the file')
        print(f' Error {e}')
        print('═'*52)

# Definimos una funcion para consultar los datos de los pacientes
def consult_patient_data():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*13 + '( Consult patient data )' + ' '*13 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult a patient' + ' '*27 + '║')
    print('║' + '(2) » Consult all patients' + ' '*24 + '║')
    print('║' + '(3) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para consultar los datos de un paciente por medio de su 'id'
def view_a_patient():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*19 + 'Patient data' + ' '*19 + '║')
    print('╚' + '═'*50 + '╝')
    patient_id = input(' '*6 + ' Enter patient ID to consult: ')
    print()
    clean_console()

    try:
        filename = 'patient-data.csv'
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            patient_found = False   # Variable para rastrear si se encuentra el paciente

            for row in reader:
                if row['Identification'] == patient_id:
                    patient_found = True    # Marcamos que se enconstro el paciente
                    print()
                    print('╔' + '═'*50 + '╗')
                    print(' '*9 + f'Patient with ID {patient_id} found' + ' '*9 )
                    print('╚' + '═'*50 + '╝')

                    for key, value in row.items():
                        print(f' {key}: {value}')
                    break   # Rompemos el ciclo una vez que se encuentre el paciente

            if not patient_found:
                    print('╔' + '═'*50 + '╗')
                    print(' '*7 + f'Patient with ID {patient_id} not found' + ' '*7 )  # Mensaje en caso de que el paciente no se encuentre
                    print('╚' + '═'*50 + '╝')  
        print('═'*52)

    except Exception as e:
                print('\t'*9 + ' '*5 + ' An error ocurred while reading information from the file')
                print('═'*52)

# Definimos una funcion para consultar los datos de todos los pacientes
def view_all_patient():
    try:
        filename = 'patient-data.csv'
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # Agregamos decoracion
            clean_console()
            print('╔' + '═'*50 + '╗')
            print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
            print('╠' + '═'*50 + '╣')
            print('║' + ' '*19 + 'Patients data' + ' '*18 + '║')
            print('╚' + '═'*50 + '╝')
            print()
            print('═'*225)
            # Imprimir los nombres de las columnas centrados
            # Para ello iteramos los elementos del diccionario
            for key in reader.fieldnames:
                print(key.center(25), end=' | ')
            print()
            
            # Imprimir los registros
            for row in reader:
                for key, value in row.items():
                    print(value.center(25), end=' | ')
                print()
        print('═'*225)
        print()

    except Exception as e:
        print('\t'*9 + ' '*5 + ' An error ocurred while reading information from the file')
        print('═'*52)

# Definimos una funcion para modificar o actualizar los datos de los pacientes
def update_patient_data_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Update patient' + ' '*30 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Función para actualizar la información de un paciente
def update_patient_data():
    clean_console()
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('╚' + '═'*50 + '╝')

    patient_id = input(' '*6 + ' Enter patient ID to update: ')
    
    try:
        filename = 'patient-data.csv'
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            patients = list(reader)

            for i, row in enumerate(patients):
                if row['Identification'] == patient_id:
                    print()
                    print('╔' + '═'*50 + '╗')
                    print(' '*7 + f'Updating patient with ID {patient_id}' + ' '*7)
                    print('╚' + '═'*50 + '╝')
                    
                    for key, value in row.items():
                        print(f'\t\t{key}: {value}')
                    
                    # Solicitar al usuario los nuevos datos
                    print('\n\t\tEnter new data:')
                    for key in row.keys():
                        new_value = input(f'\t\t{key}: ')
                        patients[i][key] = new_value

                    # Guardar los cambios en el archivo CSV
                    with open(filename, 'w', newline='') as csv_file_write:
                        writer = csv.DictWriter(csv_file_write, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(patients)

                    print(' Patient data updated successfully')
                    print('═'*52)
                    break

            else:
                print('╔' + '═'*50 + '╗')
                print(' '*7 + f'Patient with ID {patient_id} not found' + ' '*7 )  # Mensaje en caso de que el paciente no se encuentre
                print('╚' + '═'*50 + '╝')  

    except Exception as e:
        print('\t'*9 + ' '*5 + f' An error occurred while updating patient information: {e}')
        print('═'*52)

# Función para cargar datos desde el archivo CSV al inicio del programa
def load_data_from_csv():
    try:
        filename = 'patient-data.csv'
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)
    except FileNotFoundError:
        # Si el archivo no existe, se crea vacío
        pass

# Función para actualizar la información de un paciente
def update_patient_data():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('╚' + '═'*50 + '╝')

def delete_save_data_to_csv():
    try:
        filename = 'patient-data.csv'
        with open(filename, 'w', newline='') as csv_file:  # Cambiar 'a' a 'w' para escribir desde el principio
            columns = ['Identification', 'Names', 'Surnames', 'Age', 'Gender', 'Address', 'Phone number', 'Health coverage']
            writer = csv.DictWriter(csv_file, columns)

            # Escribir la cabecera siempre
            writer.writeheader()

            # Escribir todos los datos en la lista
            for data in data_list:
                writer.writerow(data)

        # Cuando el archivo se guarde correctamente, mostrar este mensaje:
        print(' Patient deleted successfully from the CSV file')
        print('═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algún error, mostrar este mensaje:
        print(' An error occurred while saving information to the file')
        print(f' Error {e}')
        print('═'*52)

# Definimos una funcion para eliminar los datos de los pacientes

def delete_patient_data_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete patient' + ' '*30 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def delete_patient_data():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu del doctor
def doctor_menu():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('║' + '-'*18 + ' DOCTOR MENU ' + '-'*19 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create clinic history' + ' '*23 + '║')
    print('║' + '(2) » Consult clinic history' + ' '*22 + '║')
    print('║' + '(3) » Update clinic history' + ' '*23 + '║')
    print('║' + '(4) » Delete clinic history' + ' '*23 + '║')
    print('║' + '(5) » Exit' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

history_list = []

# Definimos una funcion para crear la historia clinica de cada paciente
def add_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*15  + ' ( Clinic history ) ' + ' '*15 + '║')
    print('╚' + '═'*50 + '╝')
    symptoms =  input(' Reason for consultation: ')
    current_illness = input(' Current illness: ')
    medical_history = input(' Medical history: ')
    family_illnesses = input(' Family illnesses: ')
    allergies = input(' Allergies: ')
    treatment = input(' Treatment: ')
    print('═'*50)

    clinic_history = {
                        'Symptoms': symptoms,
                        'Current illness': current_illness,
                        'Medical history': medical_history,
                        'Family illnesses': family_illnesses,
                        'Allergies': allergies,
                        'Treatment': treatment
    }

    history_list.append(clinic_history)
    save_history_data_to_csv()

# Definimos una funcion para guardar los datos en el archivo csv

history_list = []

# Definimos una función para crear la historia clínica de cada paciente

# Definimos una función para guardar los datos en el archivo CSV
def save_history_data_to_csv():
    try:
        clinic_history_file = 'clinic-history.csv'
        with open(clinic_history_file, 'a', newline='') as file:
            line = ['Symptoms', 'Current illness', 'Medical history', 'Family illnesses', 'Allergies', 'Treatment']
            writer = csv.DictWriter(file, fieldnames=line)

            if file.tell() == 0:
                writer.writeheader()

            for clinic_history in history_list:
                writer.writerow(clinic_history)

        # Cuando el archivo se guarde correctamente nos mostrará este mensaje:
        print(f' The history has been saved perfectly in the file')
        print('═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algún error, se mostrará este mensaje:
        print(f'An error occurred while saving history to the file')
        print('═'*52)

# Definimos una funcion para consultar la historia clinica del paciente
def consult_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult medical records' + ' '*21 + '║')
    print('║' + '(2) » Consult all medical records ' + ' '*16 + '║')
    print('║' + '(3) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def view_a_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

def view_all_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para actualizar o modificar la historia clinica del paciente
def update_history_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult medical history' + ' '*21 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def update_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para eliminar la historia clinica de un paciente
def delete_history_menu():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete medical history' + ' '*22 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def delete_history():
    header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para salir, esta funcion se va a encargar de dejar al usuario en el 'login'
def exit():
    # Solicitamos la funcion de limpiar pantalla
    clean_console()
    # Solicitamos la funcion de login para que nos deje en el 'login' y poder ingresar nuevamente
    # cuando el usuario ingrese las credenciales correctas
    login()

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para nuestro 'login'
def login():
    while True:
        # Añadimos algo de decoracion
        header()
        print('╔' + '═'*50 + '╗')
        print('║' + ' '*22 + 'LOGIN' + ' '*23 + '║')
        print('╠' + '═'*50 + '╣')
        print('║' +  ' '*20 + 'Hello again!' + ' '*18 + '║')
        print('║' + ' '*5 + 'Please enter the credentials to continue' + ' '*5 + '║')
        print('╚' + '═'*50 + '╝')
        # Solicitamos el nombre de usuario y la contraseña
        print(' Username')
        username = input(' » ')
        print(' Password')
        password = getpass.getpass(' » ')

        # Rcorremos el diccionario donde estan almacenados los datos de los usuarios usando la funcion 'for'
        for user in users:
            if username == user['username'] and password == user['password']:
                clean_console()

                # Al ingresar se nos va a mostrar un mensaje de bienvenida con el rol del usuario que ingreso al programa
                print('═'*52)
                print(' WELCOME, {}!'.format(user['role']))
                return user['role']
        clean_console()
        # Si los credenciales (usuario o contraseña) son incorrectos nos mostrara un mensaje que lo hara saber
        print(' '*9 + 'Incorrect credentials, try again')
        print()

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion 'menu' que toma como argumento 'role' para determinar que menu se va a mostrar
def menu(role):
    while True:
        # Si 'role' es igual a 'admin' nos mostrara el menu del administrador (Kameron)
        if role == 'admin':
            admin_menu()
            # Creamos una opcion para que el administrador elija lo que desea hacer en su menu
            admin_option = input(' Select an option: ')

            # La opcion '1' le permite al dministrador crear nuevos usuarios, contraseñas y roles
            if admin_option == '1':
                clean_console()
                add_users_menu()
                add_user_option = input(' Select an option: ')

                if add_user_option == '1':
                    clean_console()
                    add_users_data()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif add_user_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '2' le permite al administrador consultar los datos de los usuarios
            elif admin_option == '2':
                clean_console()
                consult_users_data()

                view_users_option = input(' Select an option: ')

                if view_users_option == '1':
                    clean_console()
                    view_a_user()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_users_option == '2':
                    clean_console()
                    view_all_users()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_users_option == '3':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1-3)')
                    print()

            # La opcion '3' le permite al administrador actualizar los datos de los usuarios
            elif admin_option == '3':
                clean_console()
                change_credentials()
                input(' '*8 + 'Press enter to return to the menu: ')
                clean_console()

            # La opcion '4' le permite al administrador eliminar los datos de los usuarios
            elif admin_option == '4':
                clean_console()
                delete_user_menu()
                delete_user_option = input(' Select an option: ')

                if delete_user_option == '1':
                    clean_console()
                    delete_users_data()
                    
                elif delete_user_option == '2':
                    clean_console()

                else:
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '5' le permitre al administrador realizar una copia de seguridad
            elif admin_option == '5':
                clean_console()
                backup()
                backup_option = input(' Select an option: ')

                if backup_option == '1':
                    clean_console()
                    make_backup()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif backup_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '6' le permite al administrador salir del programa, esta opcion lo deja en el 'login' para que ingrese nuevamente
            elif admin_option == '6':
                clean_console()
                login()
            # De otro modo si la opcion no esta entre los numeros del 1-6, nos muestra un mensaje para escoger 
            # una opcion valida entre el rango de estos numeros y nos muestra nuevamente el menu de administrador
            else:
                clean_console()
                print(' '*18 + 'Invalid option')
                print(' '*8 + 'Please select a valid option (1-6)')
                print()

#_________________________________________________________________________________________________________________________________________________________________________________#
        # Si 'role' es igual a 'assitant' nos mostrara el menu del asistente (Kevin)
        elif role == 'assistant':
            assistant_menu()

            # Creamos una opcion para que el asistente elija lo que desea hacer en su menu
            assistant_option = input(' Select an option: ')

            # La opcion '1' le permite al asistente agregar los datos de un nuevo paciente
            if assistant_option == '1':
                clean_console()
                add_patient_data_menu()
                
                add_patient_option = input(' Select an option: ')

                if add_patient_option == '1':
                    clean_console()
                    add_patient_data()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif add_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '2' le permite al asistente consultar uno o todos los registros de los pacientes
            elif assistant_option == '2':
                clean_console()
                consult_patient_data()
                view_patient_option = input(' Select an option: ')

                if view_patient_option == '1':
                    view_a_patient()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_patient_option == '2':
                    view_all_patient()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_patient_option == '3':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1-3)')
                    print()

            # La opcion '3' le permite al asistente actulizar o modificar los registros de un paciente (Informacion personal)
            elif assistant_option == '3':
                clean_console()
                update_patient_data_menu()
                update_patient_option = input(' Select an option: ')

                if update_patient_option == '1':
                    clean_console()
                    update_patient_data()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif update_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '4' le permite al asistente eliminar los datos de un paciente
            elif assistant_option == '4':
                clean_console()
                delete_patient_data_menu()
                delete_patient_option = input(' Select an option: ')

                if delete_patient_option == '1':
                    clean_console()
                    delete_patient_data()

                elif delete_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '5' le permite al asistente salir del programa, esta opcion lo deja en el 'login' para que ingrese nuevamente
            elif assistant_option == '5':
                clean_console()
                login()

            # De otro modo si la opcion no esta entre los numeros del 1-5, nos muestra un mensaje para escoger 
            # una opcion valida entre el rango de estos numeros y nos muestra nuevamente el menu del asistente
            else:
                clean_console()
                print(' '*18 + 'Invalid option')
                print(' '*8 + 'Please select a valid option (1-5)')
                print()

#_________________________________________________________________________________________________________________________________________________________________________________#
        # Si 'role' es igual a 'doc' nos mostrara el menu del doctor o medico (Samuel)
        elif role == 'doc':
            doctor_menu()

            # Creamos una opcion para que el doctor elija lo que desea hacer en su menu
            doc_option = input(' Select an option: ')

            if doc_option == '1':
                clean_console()
                add_history()
                input(' '*8 + 'Press enter to return to the menu: ')
                clean_console()

            # La opcion '2'
            elif doc_option == '2':
                clean_console()
                consult_history()
                view_history_option = input(' Select an option: ')

                if view_history_option == '1':
                    clean_console()
                    view_a_history()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_history_option == '2':
                    clean_console()
                    view_all_history()
                    input(' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_history_option == '3':
                    clean_console()

                else:
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1-3)')
                    print()

            elif doc_option == '3':
                clean_console()
                update_history_menu()
                update_history_option = input(' Select an option: ')

                if update_history_option == '1':
                    clean_console()
                    update_history()
                
                elif update_history_option == '2':
                    clean_console()

                else:
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()
            
            elif doc_option == '4':
                clean_console()
                delete_history_menu()
                delete_history_option = input(' Select an option: ')

                if delete_history_option == '1':
                    clean_console()
                    delete_history()

                elif delete_history_option == '2':
                    clean_console()

                else:
                    print(' '*18 + 'Invalid option')
                    print(' '*8 + 'Please select a valid option (1 or 2)')
                    print()
 
            elif doc_option == '5':
                clean_console()
                login()

            else:
                clean_console()
                print(' '*18 + 'Invalid option.')
                print(' '*8 + 'Please select a valid option (1-5)')
                print()

        else:
            print(' Dont have access to side')
            print()

#_________________________________________________________________________________________________________________________________________________________________________________#
if __name__ == '__main__':
    user_role = login()
    if user_role:
        menu(user_role)
