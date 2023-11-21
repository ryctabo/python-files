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
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Creamos un diccionario con los nombres de usuario, contraseña y el rol que van a desempeñar estos usuarios
users = [
    {
        'username': 'admin',
        'password': '1234',
        'role': 'admin'
    },
    {
        'username': 'assistant1',
        'password': '1234',
        'role': 'assistant'
    },
    {
        'username': 'doc1',
        'password': '1234',
        'role': 'doc'
    }
]

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para el menu de administrador
def admin_menu():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '║' + '-'*19 + ' ADMIN MENU ' + '-'*19 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Create a new user' + ' '*27 + '║')
    print('\t'*10 + '║' + '(2) » Consult user data' + ' '*27 + '║')
    print('\t'*10 + '║' + '(3) » Update user data' + ' '*28 + '║')
    print('\t'*10 + '║' + '(4) » Delete users' + ' '*32 + '║')
    print('\t'*10 + '║' + '(5) » Data backup'  + ' '*33 + '║')
    print('\t'*10 + '║' + '(6) » Exit' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def add_users_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*14 + '  ( Create new user ) ' + ' '*14 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Create a new user' + ' '*27 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

new_users = {}  # We create a dictionary for new users

# Definimos la función para crear nuevos usuarios
def add_users_data():
    header()        # We request our header
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*14 + '  ( Create new user ) ' + ' '*14 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '→ Enter a username to continue.' + ' '*19 + '║')
    print('\t'*10 + '║' + ' '*50 + '║')
    print('\t'*10 + '║' + '→ The password can be any combination of letters, ' + '║')
    print('\t'*10 + '║' + '  numbers, and symbols. Use minimun 8 characters. ' + '║')
    print('\t'*10 + '║' + ' '*50 + '║')
    print('\t'*10 + '║' + '→ Assign a user role (admin, assistant, doc).' + ' '*5 +'║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

    # Usamos 'try' para manejar situaciones excepcionales o errores que puedan ocurrir durante la ejecución de un programa
    try:
        # Creamos los campos con los que el administrador podrá crear nuevos usuarios
        new_users['username'] = input('\t'*10 + ' » Username: ')
        new_users['password'] = input('\t'*10 + ' » Password: ')
        new_users['role'] = input('\t'*10 + ' » Role: ')
        print('\t'*10 + '═'*52)

        # Insertamos los nuevos usuarios en la lista
        users.append(new_users)

    # En caso de que se produzca algún error nos mostrará este mensaje
    except Exception as e:
        print('\t'*10 + f' Error: {e}')
        print('\t'*10 + ' Please try again')
        print('\t'*10 + '═'*52)

    # Solicitamos nuestra función para guardar a los usuarios en el archivo csv
    save_users_to_csv()

# Definimos una función para guardar usuarios en un archivo CSV
def save_users_to_csv():
    try:
        filename_users = 'user-data.csv'                               # Definimos el nombre de nuestro archivo CSV
        with open(filename_users, 'a', newline='') as user_file_csv:   # Abrimos el archivo en modo 'append' y definimos su alias
            fieldnames = ['username', 'password', 'role']              # Definimos nuestro encabezado
            writer = csv.DictWriter(user_file_csv, fieldnames)         # Creamos un escritor para nuestro archivo y encabezado

            # Si el archivo está vacío, se escribirá el encabezado
            if user_file_csv.tell() == 0:
                writer.writeheader()
            writer.writerow(new_users)

        # Mensaje en caso de que los datos estén almacenados correctamente
        print('\t'*10 + ' '*3 + f'User data saved to {filename_users} successfully')
        print('\t'*10 + '═'*52)

        # Mensaje en caso de que los datos no se almacenen correctamente
    except Exception as e:
        print('\t'*10 + f' Erorr {e}')
        print('\t'*10 + ' Unable to save user data to CSV')
        print('\t'*10 + '═'*52)

#Definimos una función para consultar los detos de los usuarios
def consult_users_data():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*14 + '( Consult user data )' + ' '*15 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Consult a user' + ' '*30 + '║')
    print('\t'*10 + '║' + '(2) » Consult all users' + ' '*27 + '║')
    print('\t'*10 + '║' + '(3) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una función para consultar los datos de un solo usuario
def view_a_user():
    clean_console()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + ' '*20 + 'Users data' + ' '*20 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    username = input('\t'*10 + ' Enter the username to consult: ')

    try:
        filename_users = 'user-data.csv'
        with open(filename_users, 'r', newline='') as user_file_csv:
            reader = csv.DictReader(user_file_csv)
            user_found = False   # Variable para rastrear si se encuentra al usuario

            for row in reader:
                if row['username'] == username:
                    user_found = True    # Marcamos que el usuario fue encontrado
                    print()
                    print('\t'*10 + '╔' + '═'*50 + '╗')
                    print('\t'*10 + ' '*15 + f'User {username} found' + ' '*14 )
                    print('\t'*10 + '╚' + '═'*50 + '╝')

                    for key, value in row.items():
                        print('\t'*10 + f' {key}: {value}')
                    break   # Rompemos el ciclo una vez que se encuentra al usuario

            if not user_found:
                    print('\t'*10 + '╔' + '═'*50 + '╗')
                    print('\t'*10 + ' '*13 + f'User {username} not found' + ' '*12 )  # Mensaje en caso de que no se encuentre el usuario
                    print('\t'*10 + '╚' + '═'*50 + '╝')  
        print('\t'*10 + '═'*52)

    except Exception as e:
                print('\t'*9 + ' '*5 + ' An error ocurred while reading information from the file')
                print('\t'*10 + '═'*52)

# Definimos una funcion para consultar todos los usuarios
def view_all_users():
    try:
        filename_users = 'user-data.csv'
        with open(filename_users, 'r', newline='') as user_file_csv:
            reader = csv.DictReader(user_file_csv)

            # Agregamos algo de decoracion
            clean_console()
            print('\t'*10 + '╔' + '═'*50 + '╗')
            print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
            print('\t'*10 + '╠' + '═'*50 + '╣')
            print('\t'*10 + '║' + ' '*20 + 'Users data' + ' '*20 + '║')
            print('\t'*10 + '╚' + '═'*50 + '╝')
            print()

            # Iteramos los elementos del diccionario
            # Se imprimen los registros
            for row in reader:
                for key, value in row.items():
                    print('\t'*10 + ' ' + key, value)
                print()
        print('\t'*10 + '═'*52)

    except Exception as e:
        print('\t'*9 + ' '*5 + ' An error ocurred while reading information form the file')
        print('\t'*10 + '═'*52)

# Definimos la función para modificar los datos del usuario
def update_users_data():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Update user data' + ' '*28 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    update_option = input('\t'*10 + ' Select an option: ')

    if update_option == '1':
        change_username()
        print('\t'*10 + ' Enter username to update')
        update_username = input('\t'*10 + ' » ')

        for user in users:
            if user['username'] == update_username:
                print('\t'*10 + f' Update data for user {update_username}')
                
                new_username = input('\t'*10 + ' New username: ')
                new_password = input('\t'*10 + ' New password: ')

                user['username'] = new_username
                user['password'] = new_password

                print('\t'*10 + ' User data update successfully')
                print('\t'*10 + '═'*52)
                save_users_to_csv()
                return
        
        print('\t'*10 + ' User not found')
        print('\t'*10 + '═'*52)

    elif update_option == '2':
        clean_console()

    else:
        clean_console()
        print('\t'*10 + ' '*18 + 'Invalid option')
        print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 3)')
        print()

# Definimos una funcion para cambiar el nombre de usuario
def change_username():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + ' '*15  + '  ( Update users ) ' + ' '*15 + ' ║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para cambiar la contraseña de usuario
def change_password():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + ' '*13  + '  ( Change password ) ' + ' '*14 + ' ║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def delete_user_menu():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Delete user data' + ' '*28 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para eliminar a los usuarios
def delete_users_data():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*15  + '  ( Delete users ) ' + ' '*15 + ' ║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    print('\t'*10 + ' Enter username to delete')
    username_to_delete = input('\t'*10 + ' » ')
    for user in users:
        if user['username'] == username_to_delete:
            users.remove(user)
            print('\t'*10 + f' Username {username_to_delete} delete successfully')
            print('\t'*10 + '═'*52)

            # Actualizamos nuestra lista de usuarios
            save_users_to_csv()
            break
        
        else:
            print('\t'*10 + f' User {username_to_delete} not found')
        print('\t'*10 + '═'*52)

# Definimos una funcion para el menu de hacer una copia de seguridad de datos
def backup():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*16  + ' ( Data backup ) ' + ' '*16 + ' ║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Make backup' + ' '*33 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para crear una copia de seguridad
def make_backup():
    try:
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
        print('\t'*10 + '╠' + '═'*50 + '╣')
        print('\t'*10 + '║' + ' '*16  + ' ( Data backup ) ' + ' '*16 + ' ║')
        print('\t'*10 + '╚' + '═'*50 + '╝')

        print('\t'*10 + ' Enter the source path of the CSV file')
        source_path = input('\t'*10 + ' » ')
        print('\t'*10 + '═'*52)
        print('\t'*10 + ' Enter the backup path for the CSV file')
        backup_route = input('\t'*10 + ' » ')
        print('\t'*10 + '═'*52)

        shutil.copy2(source_path, backup_route)
        print('\t'*10 + f'Successfully backed up {source_path} to {backup_route}')

    except FileNotFoundError:
        print('\t'*10 + ' Error: The file was not found')
        print('\t'*10 + f' {source_path}')
        print('\t'*10 + '═'*52)

    except PermissionError:
        print('\t'*10 + ' Error: Permision denied when trying to copy')
        print('\t'*10 + f' {source_path}')
        print('\t'*10 + '═'*52)

    except Exception as e:
        print('\t'*10 + ' Unexpected error')
        print('\t'*10 + f' {e}')
        print('\t'*10 + '═'*52)

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu de asistente
def assistant_menu():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '║' + '-'*17 + ' ASSISTANT MENU ' + '-'*17 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Create new patient record' + ' '*19 + '║')
    print('\t'*10 + '║' + '(2) » Consult patient data' + ' '*24 + '║')
    print('\t'*10 + '║' + '(3) » Update patient data' + ' '*25 + '║')
    print('\t'*10 + '║' + '(4) » Delete patient data' + ' '*25 + '║')
    print('\t'*10 + '║' + '(5) » Exit' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def add_patient_data_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*16  + ' ( Patient data ) ' + ' '*16 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Create new patient record' + ' '*19 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Creamos una lista vacia para almacenar los datos
data_list = []

# Definimos la funcion para crear o añadir pacientes nuevos
def add_patient_data():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*16  + ' ( Patient data ) ' + ' '*16 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    id = input('\t'*10 + ' » Id: ')
    name = input('\t'*10 + ' » Names: ')
    lastname = input('\t'*10 + ' » Surnames: ')
    age = input('\t'*10 + ' » Age: ')
    gender = input('\t'*10 + ' » Gender: ')
    address = input('\t'*10 + ' » Address: ')
    phone = input('\t'*10 + ' » Phone number: ')
    health_coverage = input('\t'*10 + ' » Health coverage: ')
    print('\t'*10 + '═'*52)

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
                break

        # Cuando el archivo se guarde correctamente nos mostrara este mensaje:
        print(f'\t'*10 +' The patient has been saved perfectly in the file')
        print('\t'*10 + '═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algun error, se mostrar este mensaje:
        print('\t'*10 + ' An error occurred while saving information to the file')
        print('\t'*10 + f' Error {e}')
        print('\t'*10 + '═'*52)

# Definimos una funcion para consultar los datos de los pacientes
def consult_patient_data():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*13 + '( Consult patient data )' + ' '*13 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Consult a patient' + ' '*27 + '║')
    print('\t'*10 + '║' + '(2) » Consult all patients' + ' '*24 + '║')
    print('\t'*10 + '║' + '(3) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para consultar los datos de un paciente por medio de su 'id'
def view_a_patient():
    clean_console()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + ' '*19 + 'Patient data' + ' '*19 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    patient_id = input('\t'*10 + ' '*6 + ' Enter patient ID to consult: ')
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
                    print('\t'*10 + '╔' + '═'*50 + '╗')
                    print('\t'*10 + ' '*9 + f'Patient with ID {patient_id} found' + ' '*9 )
                    print('\t'*10 + '╚' + '═'*50 + '╝')

                    for key, value in row.items():
                        print('\t'*10 + f' {key}: {value}')
                    break   # Rompemos el ciclo una vez que se encuentre el paciente

            if not patient_found:
                    print('\t'*10 + '╔' + '═'*50 + '╗')
                    print('\t'*10 + ' '*7 + f'Patient with ID {patient_id} not found' + ' '*7 )  # Mensaje en caso de que el paciente no se encuentre
                    print('\t'*10 + '╚' + '═'*50 + '╝')  
        print('\t'*10 + '═'*52)

    except Exception as e:
                print('\t'*9 + ' '*5 + ' An error ocurred while reading information from the file')
                print('\t'*10 + '═'*52)

# Definimos una funcion para consultar los datos de todos los pacientes
def view_all_patient():
    try:
        filename = 'patient-data.csv'
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # Agregamos decoracion
            clean_console()
            print('\t'*10 + '╔' + '═'*50 + '╗')
            print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
            print('\t'*10 + '╠' + '═'*50 + '╣')
            print('\t'*10 + '║' + ' '*19 + 'Patients data' + ' '*18 + '║')
            print('\t'*10 + '╚' + '═'*50 + '╝')
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
        print('\t'*10 + '═'*52)

# Definimos una funcion para modificar o actualizar los datos de los pacientes
def update_patient_data_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Update patient' + ' '*30 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

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

# Función para buscar un paciente por ID
def find_patient_by_id(patient_id):
    for patient in data_list:
        if patient['Identification'].strip() == patient_id.strip():
            return patient
    return None

# Función para actualizar la información de un paciente
def update_patient_data():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

    # Solicitar al usuario el ID del paciente a actualizar
    patient_id = input('\t'*10 + ' '*6 + 'Enter patient ID to update: ')
    patient = find_patient_by_id(patient_id)

    if patient:
        # Mostrar la información actual del paciente
        clean_console()
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + '║' + ' '*12 + 'Current Patient Information' + ' '*11 + '║')
        print('\t'*10 + '╚' + '═'*50 + '╝')

        display_patient_info(patient)

        # Permitir al usuario actualizar la información
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + '║' + ' '*6 + 'Enter the new information to continue ' + ' '*6 + '║')
        print('\t'*10 + '╠' + '═'*50 + '╣')
        print('\t'*10 + '║' + ' '*6 + 'Press Enter to keep the current value ' + ' '*6 + '║')
        print('\t'*10 + '║' + ' '*10 + 'Otherwise write the new value ' + ' '*10 + '║')
        print('\t'*10 + '╚' + '═'*50 + '╝')
        name = input('\t'*10 + ' » Names: ')
        lastname = input('\t'*10 + ' » Surnames: ')
        age = input('\t'*10 + ' » Age: ')
        gender = input('\t'*10 + ' » Gender: ')
        address = input('\t'*10 + ' » Address: ')
        phone = input('\t'*10 + ' » Phone number: ')
        health_coverage = input('\t'*10 + ' » Health coverage: ')
        print('\t'*10 + '═'*52)

        # Actualizar la información del paciente
        if name:
            patient['Names'] = name
        if lastname:
            patient['Surnames'] = lastname
        if age:
            patient['Age'] = age
        if gender:
            patient['Gender'] = gender
        if address:
            patient['Address'] = address
        if phone:
            patient['Phone number'] = phone
        if health_coverage:
            patient['Health coverage'] = health_coverage

        # Guardar los cambios en el archivo CSV
        save_data_to_csv()
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + ' '*5 + ' Patient information updated successfully' + ' '*5 )
        print('\t'*10 + '╚' + '═'*50 + '╝')
    else:
        print('\n')
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + ' '*7 + f'Patient with ID: {patient_id} not found' + ' '*7)
        print('\t'*10 + '╚' + '═'*50 + '╝')

# Función para mostrar la información de un paciente
def display_patient_info(patient):
    for key, value in patient.items():
        print('\t'*10 + f' » {key}: {value}')

# Cargar datos desde el archivo CSV al inicio del programa
load_data_from_csv()

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
        print('\t'*10 + ' Patient deleted successfully from the CSV file')
        print('\t'*10 + '═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algún error, mostrar este mensaje:
        print('\t'*10 + ' An error occurred while saving information to the file')
        print('\t'*10 + f' Error {e}')
        print('\t'*10 + '═'*52)

# Definimos una funcion para eliminar los datos de los pacientes

def delete_patient_data_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Delete patient' + ' '*30 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def delete_patient_data():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

    # Solicitar al usuario el ID del paciente a eliminar
    patient_id = input('\t'*10 + ' » Enter patient ID to delete: ')
    patient = find_patient_by_id(patient_id)

    if patient:
        # Mostrar la información actual del paciente antes de eliminar
        clean_console()
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + '║' + ' '*11 + 'Current Patient Information ' + ' '*11 + '║')
        print('\t'*10 + '╚' + '═'*50 + '╝')

        display_patient_info(patient)
        print('\t'*10 + '═'*52 )

        # Confirmar la eliminación
        confirmation = input('\t'*10 + ' Are you sure to delete the data? (yes/no): ').lower()

        if confirmation == 'yes':
            # Eliminar el paciente de la lista
            data_list.remove(patient)

            # Guardar los cambios en el archivo CSV
            delete_save_data_to_csv()
        else:
            print('\t'*10 + ' Deletion cancelled')
    else:
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + ' '*7 + f'Patient with ID: {patient_id} not found' + ' '*7)
        print('\t'*10 + '╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu del doctor
def doctor_menu():
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('\t'*10 + '║' + '-'*18 + ' DOCTOR MENU ' + '-'*19 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Create clinic history' + ' '*23 + '║')
    print('\t'*10 + '║' + '(2) » Consult clinic history' + ' '*22 + '║')
    print('\t'*10 + '║' + '(3) » Update clinic history' + ' '*23 + '║')
    print('\t'*10 + '║' + '(4) » Delete clinic history' + ' '*23 + '║')
    print('\t'*10 + '║' + '(5) » Exit' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

history_list = []

# Definimos una funcion para crear la historia clinica de cada paciente
def add_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*15  + ' ( Clinic history ) ' + ' '*15 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')
    symptoms =  input('\t'*10 + ' Reason for consultation: ')
    current_illness = input('\t'*10 + ' Current illness: ')
    medical_history = input('\t'*10 + ' Medical history: ')
    family_illnesses = input('\t'*10 + ' Family illnesses: ')
    allergies = input('\t'*10 + ' Allergies: ')
    treatment = input('\t'*10 + ' Treatment: ')
    print('\t'*10 + '═'*50)

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
        print(f'\t'*10 + ' The history has been saved perfectly in the file')
        print('\t'*10 + '═'*52)

    except Exception as e:
        # Si el archivo no se guarda correctamente o existe algún error, se mostrará este mensaje:
        print(f'\t'*10 + 'An error occurred while saving history to the file')
        print('\t'*10 + '═'*52)

# Definimos una funcion para consultar la historia clinica del paciente
def consult_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Consult medical records' + ' '*21 + '║')
    print('\t'*10 + '║' + '(2) » Consult all medical records ' + ' '*16 + '║')
    print('\t'*10 + '║' + '(3) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def view_a_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def view_all_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para actualizar o modificar la historia clinica del paciente
def update_history_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Consult medical history' + ' '*21 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def update_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

# Definimos una funcion para eliminar la historia clinica de un paciente
def delete_history_menu():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╠' + '═'*50 + '╣')
    print('\t'*10 + '║' + '(1) » Delete medical history' + ' '*22 + '║')
    print('\t'*10 + '║' + '(2) » Back' + ' '*40 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

def delete_history():
    header()
    print('\t'*10 + '╔' + '═'*50 + '╗')
    print('\t'*10 + '║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('\t'*10 + '╚' + '═'*50 + '╝')

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
        print('\t'*10 + '╔' + '═'*50 + '╗')
        print('\t'*10 + '║' + ' '*22 + 'LOGIN' + ' '*23 + '║')
        print('\t'*10 + '╠' + '═'*50 + '╣')
        print('\t'*10 + '║' +  ' '*20 + 'Hello again!' + ' '*18 + '║')
        print('\t'*10 + '║' + ' '*5 + 'Please enter the credentials to continue' + ' '*5 + '║')
        print('\t'*10 + '╚' + '═'*50 + '╝')
        # Solicitamos el nombre de usuario y la contraseña
        print('\t'*10 + ' Username')
        username = input('\t'*10 + ' » ')
        print('\t'*10 + ' Password')
        password = getpass.getpass('\t'*10 + ' » ')

        # Rcorremos el diccionario donde estan almacenados los datos de los usuarios usando la funcion 'for'
        for user in users:
            if username == user['username'] and password == user['password']:
                clean_console()

                # Al ingresar se nos va a mostrar un mensaje de bienvenida con el rol del usuario que ingreso al programa
                print('\t'*10 + '═'*52)
                print('\t'*10 + ' WELCOME, {}!'.format(user['role']))
                return user['role']
        clean_console()
        # Si los credenciales (usuario o contraseña) son incorrectos nos mostrara un mensaje que lo hara saber
        print('\t'*10 + ' '*9 + 'Incorrect credentials, try again')
        print()

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion 'menu' que toma como argumento 'role' para determinar que menu se va a mostrar
def menu(role):
    while True:
        # Si 'role' es igual a 'admin' nos mostrara el menu del administrador (Kameron)
        if role == 'admin':
            admin_menu()
            # Creamos una opcion para que el administrador elija lo que desea hacer en su menu
            admin_option = input('\t'*10 + ' Select an option: ')

            # La opcion '1' le permite al dministrador crear nuevos usuarios, contraseñas y roles
            if admin_option == '1':
                clean_console()
                add_users_menu()
                add_user_option = input('\t'*10 + ' Select an option: ')

                if add_user_option == '1':
                    clean_console()
                    add_users_data()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif add_user_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '2' le permite al administrador consultar los datos de los usuarios
            elif admin_option == '2':
                clean_console()
                consult_users_data()

                view_users_option = input('\t'*10 + ' Select an option: ')

                if view_users_option == '1':
                    clean_console()
                    view_a_user()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_users_option == '2':
                    clean_console()
                    view_all_users()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_users_option == '3':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1-3)')
                    print()

            # La opcion '3' le permite al administrador actualizar los datos de los usuarios
            elif admin_option == '3':
                clean_console()
                update_users_data()

            # La opcion '4' le permite al administrador eliminar los datos de los usuarios
            elif admin_option == '4':
                clean_console()
                delete_user_menu()
                delete_user_option = input('\t'*10 + ' Select an option: ')

                if delete_user_option == '1':
                    clean_console()
                    delete_users_data()
                    
                elif delete_user_option == '2':
                    clean_console()

                else:
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '5' le permitre al administrador realizar una copia de seguridad
            elif admin_option == '5':
                clean_console()
                backup()
                backup_option = input('\t'*10 + ' Select an option: ')

                if backup_option == '1':
                    clean_console()
                    make_backup()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif backup_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '6' le permite al administrador salir del programa, esta opcion lo deja en el 'login' para que ingrese nuevamente
            elif admin_option == '6':
                clean_console()
                login()
            # De otro modo si la opcion no esta entre los numeros del 1-6, nos muestra un mensaje para escoger 
            # una opcion valida entre el rango de estos numeros y nos muestra nuevamente el menu de administrador
            else:
                clean_console()
                print('\t'*10 + ' '*18 + 'Invalid option')
                print('\t'*10 + ' '*8 + 'Please select a valid option (1-6)')
                print()

#_________________________________________________________________________________________________________________________________________________________________________________#
        # Si 'role' es igual a 'assitant' nos mostrara el menu del asistente (Kevin)
        elif role == 'assistant':
            assistant_menu()

            # Creamos una opcion para que el asistente elija lo que desea hacer en su menu
            assistant_option = input('\t'*10 + ' Select an option: ')

            # La opcion '1' le permite al asistente agregar los datos de un nuevo paciente
            if assistant_option == '1':
                clean_console()
                add_patient_data_menu()
                
                add_patient_option = input('\t'*10 + ' Select an option: ')

                if add_patient_option == '1':
                    clean_console()
                    add_patient_data()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif add_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '2' le permite al asistente consultar uno o todos los registros de los pacientes
            elif assistant_option == '2':
                clean_console()
                consult_patient_data()
                view_patient_option = input('\t'*10 + ' Select an option: ')

                if view_patient_option == '1':
                    view_a_patient()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_patient_option == '2':
                    view_all_patient()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_patient_option == '3':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1-3)')
                    print()

            # La opcion '3' le permite al asistente actulizar o modificar los registros de un paciente (Informacion personal)
            elif assistant_option == '3':
                clean_console()
                update_patient_data_menu()
                update_patient_option = input('\t'*10 + ' Select an option: ')

                if update_patient_option == '1':
                    clean_console()
                    update_patient_data()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif update_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '4' le permite al asistente eliminar los datos de un paciente
            elif assistant_option == '4':
                clean_console()
                delete_patient_data_menu()
                delete_patient_option = input('\t'*10 + ' Select an option: ')

                if delete_patient_option == '1':
                    clean_console()
                    delete_patient_data()

                elif delete_patient_option == '2':
                    clean_console()

                else:
                    clean_console()
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()

            # La opcion '5' le permite al asistente salir del programa, esta opcion lo deja en el 'login' para que ingrese nuevamente
            elif assistant_option == '5':
                clean_console()
                login()

            # De otro modo si la opcion no esta entre los numeros del 1-5, nos muestra un mensaje para escoger 
            # una opcion valida entre el rango de estos numeros y nos muestra nuevamente el menu del asistente
            else:
                clean_console()
                print('\t'*10 + ' '*18 + 'Invalid option')
                print('\t'*10 + ' '*8 + 'Please select a valid option (1-5)')
                print()

#_________________________________________________________________________________________________________________________________________________________________________________#
        # Si 'role' es igual a 'doc' nos mostrara el menu del doctor o medico (Samuel)
        elif role == 'doc':
            doctor_menu()

            # Creamos una opcion para que el doctor elija lo que desea hacer en su menu
            doc_option = input('\t'*10 + ' Select an option: ')

            if doc_option == '1':
                clean_console()
                add_history()
                input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                clean_console()

            # La opcion '2'
            elif doc_option == '2':
                clean_console()
                consult_history()
                view_history_option = input('\t'*10 + ' Select an option: ')

                if view_history_option == '1':
                    clean_console()
                    view_a_history()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_history_option == '2':
                    clean_console()
                    view_all_history()
                    input('\t'*10 + ' '*8 + 'Press enter to return to the menu: ')
                    clean_console()

                elif view_history_option == '3':
                    clean_console()

                else:
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1-3)')
                    print()

            elif doc_option == '3':
                clean_console()
                update_history_menu()
                update_history_option = input('\t'*10 + ' Select an option: ')

                if update_history_option == '1':
                    clean_console()
                    update_history()
                
                elif update_history_option == '2':
                    clean_console()

                else:
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()
            
            elif doc_option == '4':
                clean_console()
                delete_history_menu()
                delete_history_option = input('\t'*10 + ' Select an option: ')

                if delete_history_option == '1':
                    clean_console()
                    delete_history()

                elif delete_history_option == '2':
                    clean_console()

                else:
                    print('\t'*10 + ' '*18 + 'Invalid option')
                    print('\t'*10 + ' '*8 + 'Please select a valid option (1 or 2)')
                    print()
 
            elif doc_option == '5':
                clean_console()
                login()

            else:
                clean_console()
                print('\t'*10 + ' '*18 + 'Invalid option.')
                print('\t'*10 + ' '*8 + 'Please select a valid option (1-5)')
                print()

        else:
            print('\t'*10 + ' Dont have access to side')
            print()

#_________________________________________________________________________________________________________________________________________________________________________________#
if __name__ == '__main__':
    user_role = login()
    if user_role:
        menu(user_role)
