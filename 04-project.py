'''
    TECHNOLOGY IN SOFTWARE DEVELOPMENT
        SEMESTER 1 - SECTION 4

            MEDIC RECORDS
    MANAGEMENT OF CLINICAL HISTORIES

                BY:

    - KAMERON JOLY HERNANDEZ PAUTT
    - KEVIN JESUS PACHECO GOMEZ
    - SAMUEL JESUS TORRES PUELLO
'''

#_________________________________________________________________________________________________________________________________________________________________________________#
# Importamos todas las bibliotecas que vamos a utilizar en nuestro codigo
import os       # Importamos la biblioteca 'os' para limpiar la pantalla
import csv      # Importamos la biblioteca 'csv' para trabajar con archivos CSV 
import shutil   # Importamos la biblioteca 'shutil' para la copia de archivos
import getpass  # Importamos la biblioteca 'getpass' para ocultar la contraseña de usuario
import sys
from datetime import datetime

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para limpiar la pantalla
def clean_console():
    if os.name == 'nt':
        os.system('cls')    # Usamos 'os.system()' para ejecutar el comando 'cls', que borra la pantalla en sistemas Windows
    else:                   # De otro modo podemos usar:
        os.system('clear')  # El comando 'clear', que borra la pantalla en sistemas Unix (Linux y macOS)

# Solicitamos nuestra funcion para limpiar la pantalla
clean_console()

# Definimos una función para decorar el programa con caracteres ascii, para ello usaremos el siguiente encabezado: 'MEDICAL RECORDS MANAGEMENT'
def print_header():
    print(
'''
╔═══════════════════════════════════════════════════╗
║            MEDICAL RECORDS MANAGEMENT             ║
╚═══════════════════════════════════════════════════╝
'''
    )

def bad_option():
    print('Invalid option, please, select a valid option...')

def menu_management(menu):
    option = input('Select an option: ')
    action = menu.get(option, bad_option)
    clean_console()
    action()

def bye():
    print(
'''
╔═══════════════════════════════════════════════════╗
║            Bye! :)                                ║
╚═══════════════════════════════════════════════════╝
'''
    )
    input()
    sys.exit()




















def print_doc_menu():
    print(
f'''
Hi, {auth_info['user']['username']} !
╔═══════════════════════════════════════════════════╗
║            MEDICAL RECORDS MANAGEMENT             ║
╠═══════════════════════════════════════════════════╣
║                   DOCTOR MENU                     ║
╠═══════════════════════════════════════════════════╣
║ (1) » Create clinic history                       ║
║ (2) » Consult clinic history                      ║
║ (3) » Consult all clinic history                  ║
║ (4) » Update clinic history                       ║
║ (5) » Delete clinic history                       ║
║ (6) » Logout                                      ║
╚═══════════════════════════════════════════════════╝
'''
    )

def doc_menu():
    print_doc_menu()
    menu_management({
        "1": action_create_clinic_history,
        "2": action_consult_clinic_history, 
        "3": action_consult_all_clinic_history,
        "4": action_update_clinic_history,
        "5": action_delete_clinic_history,
        "6": log_out
    })




















def print_assistant_menu():
    print(
f'''
Hi, {auth_info['user']['username']} !
╔═══════════════════════════════════════════════════╗
║            MEDICAL RECORDS MANAGEMENT             ║
╠═══════════════════════════════════════════════════╣
║                  ASSISTANT MENU                   ║
╠═══════════════════════════════════════════════════╣
║ (1) » Create new patient record                   ║
║ (2) » Consult one patient                         ║
║ (3) » Consult all patients                        ║
║ (4) » Update patient                              ║
║ (5) » Delete patient                              ║
║ (6) » Logout                                      ║
╚═══════════════════════════════════════════════════╝
'''
    )

def assistant_menu():
    print_assistant_menu()
    menu_management({
        "1": action_create_patient,
        "2": action_consult_patient, 
        "3": action_consult_all_patient,
        "4": action_update_patient,
        "5": action_delete_patient,
        "6": log_out
    })


















def print_admin_menu():
    print(
f'''
Hi, {auth_info['user']['username']} !
╔═══════════════════════════════════════════════════╗
║            MEDICAL RECORDS MANAGEMENT             ║
╠═══════════════════════════════════════════════════╣
║                ADMINISTRATOR MENU                 ║
╠═══════════════════════════════════════════════════╣
║ (1) » Create a new user                           ║
║ (2) » Consult an user by username                 ║
║ (3) » Consult all users                           ║
║ (4) » Update user data                            ║
║ (5) » Delete an user by username                  ║
║ (6) » Backup                                      ║
║ (7) » Logout                                      ║
╚═══════════════════════════════════════════════════╝
'''
    )

def admin_menu():
    print_admin_menu()
    menu_management({
        "1": action_create_user,
        "2": action_find_user,
        "3": action_find_all_users,
        "4": action_update_user,
        "5": action_delete_user,
        "6": action_backup,
        "7": log_out
    })


















# -------------------------------------------------------------------
# HOW TO LOAD AND SAVE DATA IN CSV
def save_data_to_csv(filename, headers, data_list):
    try:
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, headers)
            writer.writeheader()
            writer.writerows(data_list)

    except Exception as e:
        print(' An error occurred while saving information to the file')
        print(f' Error {e}')
        print('═'*52)

def load_data_from_csv(filename):
    try:
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = []
            for row in reader:
                data_list.append(row)
            return data_list
    except FileNotFoundError:
        return []
    except:
        print(' An error occurred while reading info from file csv.')

# END: HOW TO SAVE AND LOAD DATA FROM CSV
# -------------------------------------------------------------------














# -----------------------------------------------------------------------------
# BEGIN: USER MODULE
def load_users(): 
    data = load_data_from_csv(user_filename)

    if len(data) == 0:
        default_users = [
            {
                'username': 'admin',
                'password': '1234',
                'role': 'admin'
            },
            {
                'username': 'assistant',
                'password': '1234',
                'role': 'assistant'
            },
            {
                'username': 'doc',
                'password': '1234',
                'role': 'doc'
            }
        ]
        save_data_to_csv(user_filename, user_headers, default_users)
        return default_users
    
    return data

user_filename = 'user-data.csv'
user_headers = ['username', 'password', 'role']
user_list = load_users()

roles_allowed = ['admin', 'assistant', 'doc']

def exists_user(username):
    for user in user_list:
        if user['username'] == username:
            return True
    return False

def action_create_user():
    print_create_user_header()
    create_user()
    print('═'*52)

def print_create_user_header():
    print_header()        # We request our header
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

def create_user():
    new_user = {}
    # Creamos los campos con los que el administrador podrá crear nuevos usuarios
    new_user['username'] = input_username()
    new_user['password'] = input_password()
    new_user['role'] = input_role()

    # Insertamos los nuevos usuarios en la lista
    user_list.append(new_user)
    save_data_to_csv(user_filename, user_headers, user_list)
    print(' The user has been saved successfully!')

def input_username():
    while True:
        username = input(' » Username: ')
        if len(username) > 3:
            if not exists_user(username):
                break
            else:
                print(f'This username {username} already exists!')
        else:
            print("The username is invalid, it's must have greater than 3 characters")
    return username

def input_password():
    while True:
        password = getpass.getpass(' » Password: ')
        if len(password) == 0:
            res = input(" The password is empty. it's right? (y/n): ")
            if res.lower() != 'n':
                break
        else:
            break
    return password
    
def input_role():
    while True:
        role = input(' » Role: ')
        if role in roles_allowed:
            break
        else:
            print('-'*50)
            print(' Invalid role, please enter a valid role.')
            print(' Valid roles: ', roles_allowed)
    return role

def find_user(username):
    for user in user_list:
        if user['username'] == username:
            return user
    return None

#Definimos una función para consultar los detos de los usuarios
def print_consult_data():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*14 + '( Consult user data )' + ' '*15 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult a user' + ' '*30 + '║')
    print('║' + '(2) » Consult all users' + ' '*27 + '║')
    print('║' + '(3) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def print_find_user():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*20 + 'Users data' + ' '*20 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una función para consultar los datos de un solo usuario
def action_find_user():
    print_find_user()
    username = input(' Enter the username to consult: ')
    user = find_user(username)

    if user == None:
        print(f' User with username {username} was not found.')
    else:
        print(user)

    print('═'*52)

# Definimos una funcion para consultar todos los usuarios
def action_find_all_users():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*20 + 'Users data' + ' '*20 + '║')
    print('╚' + '═'*50 + '╝')
    print()

    for user in user_list:
        print(user)

    print('═'*52)

def print_delete_user_menu():
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete user data' + ' '*28 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Modificamos la función delete_users_data para usar la función delete_user_from_csv
def action_delete_user():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*15  + '  ( Delete users ) ' + ' '*15 + ' ║')
    print('╚' + '═'*50 + '╝')
    print(' Enter username to delete')
    username_to_delete = input(' » ')

    user_to_delete = find_user(username_to_delete)

    if user_to_delete == None:
        print(f' User with {username_to_delete} was not found')
    else:
        user_list.remove(user_to_delete)
        save_data_to_csv(user_filename, user_headers, user_list)

        print(' User has been deleted successfuly!')

# Definimos la función para cambiar los credenciales del usuario
def action_update_user():
    clean_console()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11 + ' MEDICAL RECORDS MANAGEMENT' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + ' '*14 + '( Change Credentials )' + ' '*14 + '║')
    print('╚' + '═'*50 + '╝')

    username = input(' Enter your current username: ')
    user = find_user(username)

    if user == None:
        print(f'User with username {username} was not found.')

    change_username = input(' Do you want to change username? (y/n) default => no: ')
    if change_username.lower() == 'y':
        user['username'] = input_username()
    
    change_password = input(' Do you want to change password? (y/n) default => no: ')
    if (change_password.lower() == 'y'):
        user['password'] = input_password()

    save_data_to_csv(user_filename, user_headers, user_list)

# Definimos una funcion para el menu de hacer una copia de seguridad de datos
def print_backup_menu():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*16  + ' ( backup ) ' + ' '*16 + ' ║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Make backup' + ' '*33 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def action_backup():
    print_header()
    make_backup(user_filename)
    make_backup(patient_filename)
    make_backup(history_filename)
    print('All backups are finished successfully!')
    input('Enter to continue...')

# Definimos una funcion para crear una copia de seguridad
def make_backup(filename):
    try:
        current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename_without_extension = os.path.splitext(filename)[0]
        new_filename = f'{filename_without_extension}_{current_date}.csv'
        shutil.copy(filename, new_filename)

    except FileNotFoundError:
        print(' Error: The file was not found')
        print(f' {filename}')
        print('═'*52)

    except PermissionError:
        print(' Error: Permision denied when trying to copy')
        print(f' {filename}')
        print('═'*52)

    except Exception as e:
        print(' Unexpected error')
        print(f' {e}')
        print('═'*52)

# END: USER MODULE
# -----------------------------------------------------------------------------























# -----------------------------------------------------------------------------
# BEGIN: PATIENT MODULE
# Creamos una lista vacia para almacenar los datos
patient_filename = 'patient-data.csv'
patient_headers = ['Identification', 'Names', 'Surnames', 'Age', 'Gender', 'Address', 'Phone number', 'Health coverage']
patient_list = load_data_from_csv(patient_filename)

if len(patient_list) == 0:
    save_data_to_csv(patient_filename, patient_headers, patient_list)

def action_create_patient():
    print('action_create_patient')

def action_consult_patient():
    print('action_consult_patient')

def action_consult_all_patient():
    print('action_consult_all_patient')

def action_update_patient():
    print('action_update_patient')

def action_delete_patient():
    print('action_delete_patient')

# END: PATIENT MODULE
# -----------------------------------------------------------------------------



















# -----------------------------------------------------------------------------
# BEGIN: HISTORY MODULE
history_filename = 'clinic-history.csv'
history_headers = ['Symptoms', 'Current illness', 'Medical history', 'Family illnesses', 'Allergies', 'Treatment']
history_list = load_data_from_csv(history_filename)

if len(patient_list) == 0:
    save_data_to_csv(history_filename, history_headers, history_list)


def action_create_clinic_history():
    print('action_create_clinic_history')

def action_consult_clinic_history():
    print('action_consult_clinic_history')

def action_consult_all_clinic_history():
    print('action_consult_all_clinic_history')

def action_update_clinic_history():
    print('action_update_clinic_history')

def action_delete_clinic_history():
    print('action_delete_clinic_history')

# END: HISTORY MODULE
# -----------------------------------------------------------------------------





















#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos una funcion para el menu de administrador


#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu de asistente


def add_patient_data_menu():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*16  + ' ( Patient data ) ' + ' '*16 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Create new patient record' + ' '*19 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos la funcion para crear o añadir pacientes nuevos
def add_patient_data():
    print_header()
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
    patient_list.append(data)
    save_data_to_csv()



# Definimos una funcion para consultar los datos de los pacientes
def consult_patient_data():
    print_header()
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
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + '   ( Update patient data ) ' + ' '*11 + ' ║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Update patient' + ' '*30 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

# Función para actualizar la información de un paciente
def update_patient_data():
    clean_console()
    print_header()
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
            for data in patient_list:
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
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete patient' + ' '*30 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def delete_patient_data():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + '  ( Delete patient data ) ' + ' '*12 + '║')
    print('╚' + '═'*50 + '╝')

#_________________________________________________________________________________________________________________________________________________________________________________#
# Definimos la funcion del menu del doctor


history_list = []

# Definimos una funcion para crear la historia clinica de cada paciente
def add_history():
    print_header()
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
    save_data_to_csv(history_filename, history_headers, history_list)

# Definimos una funcion para guardar los datos en el archivo csv


# Definimos una función para crear la historia clínica de cada paciente



# Definimos una funcion para consultar la historia clinica del paciente
def consult_history():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult medical records' + ' '*21 + '║')
    print('║' + '(2) » Consult all medical records ' + ' '*16 + '║')
    print('║' + '(3) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def view_a_history():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

def view_all_history():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*11  + ' ( Consult clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para actualizar o modificar la historia clinica del paciente
def update_history_menu():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Consult medical history' + ' '*21 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def update_history():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Update clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

# Definimos una funcion para eliminar la historia clinica de un paciente
def delete_history_menu():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' + '(1) » Delete medical history' + ' '*22 + '║')
    print('║' + '(2) » Back' + ' '*40 + '║')
    print('╚' + '═'*50 + '╝')

def delete_history():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*12  + ' ( Delete clinic history ) ' + ' '*11 + '║')
    print('╚' + '═'*50 + '╝')

















# --------------------------------------------------------------------------------
# BEGIN: AUTHENTICATION MODULE

auth_info = {}

def print_login_header():
    print_header()
    print('╔' + '═'*50 + '╗')
    print('║' + ' '*22 + 'LOGIN' + ' '*23 + '║')
    print('╠' + '═'*50 + '╣')
    print('║' +  ' '*20 + 'Hello again!' + ' '*18 + '║')
    print('║' + ' '*5 + 'Please enter the credentials to continue' + ' '*5 + '║')
    print('╚' + '═'*50 + '╝')

def log_in():
    print_header()

    username = input('Username: ')
    user = find_user(username)

    if user == None:
        print(' The user is not identified!')
        return

    password = getpass.getpass('Password: ')

    if user['password'] == password:
        auth_info['user'] = user
        print('Login successfully!')
    else:
        print('The password is wrong!')

def log_out():
    auth_info['user'] = None

# END: AUTHENTICATION MODULE
# --------------------------------------------------------------------------------




def print_main_menu():
    print(
'''
╔═══════════════════════════════════════════════════╗
║            MEDICAL RECORDS MANAGEMENT             ║
╠═══════════════════════════════════════════════════╣
║ (1) » Login                                       ║
║ (2) » Exit                                        ║
╚═══════════════════════════════════════════════════╝
'''
    )

def main_menu():
    print_main_menu()
    menu_management({
        "1": log_in,
        "2": bye
    })

def execute_menu():
    menus = {
        "admin": admin_menu,
        "assistant": assistant_menu,
        "doc": doc_menu,
    }
    user_authenticated = auth_info['user']
    menu = menus.get(user_authenticated['role'])

    clean_console()
    menu()

if __name__ == '__main__':
    while True:
        if auth_info.get('user') != None:
            execute_menu()
        else:
            main_menu()

