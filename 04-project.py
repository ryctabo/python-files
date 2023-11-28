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
# IMPORTED LIBRARIES
import os                       # Importamos la biblioteca 'os' para limpiar la pantalla
import sys                      # Importamos la bibliotecas 'sys' para salir del programa en cualquier momento
import csv                      # Importamos la biblioteca 'csv' para trabajar con archivos CSV 
import shutil                   # Importamos la biblioteca 'shutil' para la copia de archivos
import getpass                  # Importamos la biblioteca 'getpass' para ocultar la contraseña de usuario
from datetime import datetime   # Importamos la biblioteca 'datetime' para colocar la fecha y hora de las copias de seguridad

#_________________________________________________________________________________________________________________________________________________________________________________#
# FUNCTION TO CLEAN CONSOLE
def clean_console():
    if os.name == 'nt':
        os.system('cls')    # Usamos 'os.system()' para ejecutar el comando 'cls', que borra la pantalla en sistemas Windows
    else:                   # De otro modo podemos usar:
        os.system('clear')  # El comando 'clear', que borra la pantalla en sistemas Unix (Linux y macOS)
clean_console()
#_________________________________________________________________________________________________________________________________________________________________________________#

def print_header():
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                   MEDICAL RECORDS MANAGEMENT                     ║
╚══════════════════════════════════════════════════════════════════╝''')

def bad_option():
    print(' Invalid option, please, select a valid option...')

def menu_management(menu):
    option = input(' Select an option: ')
    action = menu.get(option, bad_option)
    clean_console()
    action()

def bye():
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                         See you later!                           ║
╚══════════════════════════════════════════════════════════════════╝''')
    input()
    sys.exit()

#_________________________________________________________________________________________________________________________________________________________________________________#
# BEGIN MODULE: USER MENUS
def print_doc_menu():
    print(f'''
 Hi, {auth_info['user']['username']}!
╔══════════════════════════════════════════════════════════════════╗
║                   MEDICAL RECORDS MANAGEMENT                     ║
╠══════════════════════════════════════════════════════════════════╣
║                          DOCTOR MENU                             ║
╠══════════════════════════════════════════════════════════════════╣
║ (1) » Create clinic history                                      ║
║ (2) » Consult clinic history                                     ║
║ (3) » Consult all clinic history                                 ║
║ (4) » Update clinic history                                      ║
║ (5) » Delete clinic history                                      ║
║ (6) » Logout                                                     ║
╚══════════════════════════════════════════════════════════════════╝
''')

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
    print(f'''
 Hi, {auth_info['user']['username']}!
╔══════════════════════════════════════════════════════════════════╗
║                   MEDICAL RECORDS MANAGEMENT                     ║
╠══════════════════════════════════════════════════════════════════╣
║                         ASSISTANT MENU                           ║
╠══════════════════════════════════════════════════════════════════╣
║ (1) » Create new patient record                                  ║
║ (2) » Consult one patient                                        ║
║ (3) » Consult all patients                                       ║
║ (4) » Update patient                                             ║
║ (5) » Delete patient                                             ║
║ (6) » Logout                                                     ║
╚══════════════════════════════════════════════════════════════════╝
''')

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
 Hi, {auth_info['user']['username']}!
╔══════════════════════════════════════════════════════════════════╗
║                   MEDICAL RECORDS MANAGEMENT                     ║
╠══════════════════════════════════════════════════════════════════╣
║                       ADMINISTRATOR MENU                         ║
╠══════════════════════════════════════════════════════════════════╣
║ (1) » Create a new user                                          ║
║ (2) » Consult an user by username                                ║
║ (3) » Consult all users                                          ║
║ (4) » Update user data                                           ║
║ (5) » Delete an user by username                                 ║
║ (6) » Backup                                                     ║
║ (7) » Logout                                                     ║
╚══════════════════════════════════════════════════════════════════╝
''')

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
# END MODULE: USER MENUS
#_________________________________________________________________________________________________________________________________________________________________________________#





#_________________________________________________________________________________________________________________________________________________________________________________#
# HOW TO LOAD AND SAVE DATA IN CSV
def save_data_to_csv(filename, headers, data_list):
    try:
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, headers)
            writer.writeheader()
            writer.writerows(data_list)
            print('═'*68)
            print(' '*18 + 'It has been done successfully!')
            print('═'*68)

    except Exception as e:
        print('═'*68)
        print(' An error occurred while saving information to the file.')
        print(f' Error {e}')
        print('═'*68)

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
        print('═'*68)
        print(' An error occurred while reading info from file csv.')
        print('═'*68)

# END: HOW TO SAVE AND LOAD DATA FROM CSV
#_________________________________________________________________________________________________________________________________________________________________________________#





#_________________________________________________________________________________________________________________________________________________________________________________#
# BEGIN: USER MODULE

# We define the functions to decorate the administrator menu options
def print_create_user_header():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                         CREATE NEW USER                          ║
╠══════════════════════════════════════════════════════════════════╣
║ → Enter a username to continue. Use more than 3 characters.      ║
║                                                                  ║
║ → The password can be any combination of letters, numbers, and   ║
║   symbols. Use minimun 8 characters.                             ║
║                                                                  ║
║ → Assign a user role (admin, assistant, doc).                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    ''')

def print_find_user():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                          CONSULT USER                            ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_update_user():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                          UPDATE USER                             ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_delete_user():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                          DELETE USER                             ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_backup():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                             BACKUP                               ║
╠══════════════════════════════════════════════════════════════════╣
║ Backing up files:                                                ║
║                                                                  ║
║ - User data                                                      ║
║ - Patient data                                                   ║
║ - Medical records                                                ║
╚══════════════════════════════════════════════════════════════════╝''')

# We define a function to load the default users in the csv file
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
    print('═'*68)

def create_user():
    new_user = {}
    # Creamos los campos con los que el administrador podrá crear nuevos usuarios
    new_user['username'] = input_username()
    new_user['password'] = input_password()
    new_user['role'] = input_role()

    # Insertamos los nuevos usuarios en la lista
    user_list.append(new_user)
    save_data_to_csv(user_filename, user_headers, user_list)
    input(' '*16 + 'Press enter to return to the menu: ')

def input_username():
    while True:
        username = input(' » Username: ')
        if len(username) > 3:
            if not exists_user(username):
                break
            else:
                print(f' This username {username} already exists! ')
        else:
            clean_console()
            print_create_user_header()
            print(" The username is invalid, it's must have greater than 3 characters")
            print()
    return username

def input_password():
    while True:
        password = getpass.getpass(' » Password: ')
        if len(password) == 0:
            print('═'*68)
            res = input(" The password is empty. It's right? (y/n): ")
            print()
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
            print('═'*68)
            print(' Invalid role, please enter a valid role.')
            print(' Valid roles → ', roles_allowed)
            print()
    return role

def find_user(username):
    for user in user_list:
        if user['username'] == username:
            return user
    return None

# Definimos una función para consultar los datos de un solo usuario
def action_find_user():
    print_find_user()
    username = input(' » Enter the username to consult: ')
    user = find_user(username)

    if user == None:
        print('═'*68)
        print(f' User with username {username} was not found.')
        print()
        print(' Please try again with another username. The username may not')
        print(' exist in the database.')
    else:
        print()
        for key, value in user.items():
            print(f' {key}: {value}')

    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

# Definimos una funcion para consultar todos los usuarios
def action_find_all_users():
    print_find_user()

    for user_dict in user_list:
        print()
        for key, value in user_dict.items():
            print(f'{key}: {value}')

    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_delete_user():
    print_delete_user()
    username_to_delete = input(' » Enter username to delete: ')
    print()
    user_to_delete = find_user(username_to_delete)

    if user_to_delete == None:
        print('═'*68)
        print(f' User with username {username_to_delete} was not found')
        print()
        print(' Please try again with another username. The username may not')
        print(' exist in the database.')
        print('═'*68)
    else:
        user_list.remove(user_to_delete)
        save_data_to_csv(user_filename, user_headers, user_list)
    input(' '*16 + 'Press enter to return to the menu: ')



def action_update_user():
    print_update_user()
    username = input(' » Enter your current username: ')
    user = find_user(username)

    if user == None:
        print('═'*68)
        print(f' User with username {username} was not found.')
        print()
        print(' Please try again with another username. The username may not')
        print(' exist in the database.')
        print('═'*68)

    else:
        print('═'*68)
        print(' To change credentials select an option (y/n)')
        print(' Press enter, to keep your username or password.')
        print('═'*68)
        print()
        change_username = input(' Do you want to change username? (y/n): ')
        if change_username.lower() == 'y':
            user['username'] = input_username()
        
        change_password = input(' Do you want to change password? (y/n): ')
        if change_password.lower() == 'y':
            user['password'] = input_password()
        
        save_data_to_csv(user_filename, user_headers, user_list)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_backup():
    print_backup()
    make_backup(user_filename)
    make_backup(patient_filename)
    make_backup(history_filename)
    input(' '*16 + 'Press enter to return to the menu: ')

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
        print('═'*67)

    except PermissionError:
        print(' Error: Permision denied when trying to copy')
        print(f' {filename}')
        print('═'*67)

    except Exception as e:
        print(' Unexpected error')
        print(f' {e}')
        print('═'*67)

# END: USER MODULE
#_________________________________________________________________________________________________________________________________________________________________________________#





#_________________________________________________________________________________________________________________________________________________________________________________#
# BEGIN: PATIENT MODULE
patient_filename = 'patient-data.csv'
patient_headers = ['Identification', 'Name', 'Lastname', 'Age', 'Gender', 'Address', 'Phone number', 'Health coverage']
patient_list = load_data_from_csv(patient_filename)

def print_create_patient():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                         CREATE PATIENT                           ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_find_patient():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                        CONSULT PATIENT                           ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_update_patient():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                         UPDATE PATIENT                           ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_delete_patient():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                         DELETE PATIENT                           ║
╚══════════════════════════════════════════════════════════════════╝''')

if len(patient_list) == 0:
    save_data_to_csv(patient_filename, patient_headers, patient_list)

def find_patient(identification):
    for id in patient_list:
        if id['Identification'] == identification:
            return id
    return None

def action_create_patient():
    print_create_patient()
    id = input(' » Id: ')
    name = input(' » Name: ')
    lastname = input(' » Lastname: ')
    age = input(' » Age: ')
    gender = input(' » Gender: ')
    address = input(' » Address: ')
    phone = input(' » Phone number: ')
    health_coverage = input(' » Health coverage: ')

    patient_dict = {
        'Identification': id,
        'Name': name,
        'Lastname': lastname,
        'Age': age,
        'Gender': gender,
        'Address': address,
        'Phone number': phone,
        'Health coverage': health_coverage
    }
    patient_list.append(patient_dict)
    save_data_to_csv(patient_filename, patient_headers, patient_list)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_consult_patient():
    print_find_patient()
    identification = input(' » Enter the patient id to consult: ')
    patient = find_patient(identification)

    if patient == None:
        print('═'*68)
        print(f' Patient with id {identification} was not found')
        print()
        print(' .Check if the id is correct, otherwise the patient may ')
        print(' not be found in the database')
    else:
        print('═'*68)
        print(f' Patient with id {identification} was found')
        print()
        for key, value in patient.items():
            print(f' {key}: {value}')
    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_consult_all_patient():
    print_find_patient()
    print(' All patients:')
    for patient_dict in patient_list:
        print()
        for key, value in patient_dict.items():
            print(f' {key}: {value}')

    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

def input_or_default(message, default):
    value = input(message)
    if value == None or len(value.strip()) == 0:
        return default
    return value
    
def input_by_option(message, prop, default):
    option = input(f'Do you want to change {prop}? (y/n*): ')
    if option.lower() == 'y':
        return input(message)
    return default

def action_update_patient():
    print_update_patient()

    identification = input(' » Enter the patient id to consult: ')
    patient = find_patient(identification)

    # First option:
    patient['name'] = input(' » Name: ')

    # Second option:
    change_name = input('Do you want to change patient name? (y/n): ')
    if (change_name.lower() == 'y'):
        patient['name'] = input(' » Name: ')

    # Three option:
    patient['name'] = input_or_default(' » Name: ', patient['name'])

    # 4 option:
    patient['name'] = input_by_option(' » Name: ', 'patient name', patient['name'])

    save_data_to_csv(patient_filename, patient_headers, patient_list)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_delete_patient():
    print_delete_patient()
    id = input(' » Enter the patient id to delete: ')
    patient_to_delete = find_patient(id)

    if patient_to_delete == None:
        print('═'*68)
        print(f' Patient with id {id} was not found')
        print()
        print(' Check if the id is correct, otherwise the patient may ')
        print(' not be found in the database.')
        print('═'*68)
    else:
        patient_list.remove(patient_to_delete)
        save_data_to_csv(patient_filename, patient_headers, patient_list)

    input(' '*16 + 'Press enter to return to the menu: ')

# END: PATIENT MODULE
#_________________________________________________________________________________________________________________________________________________________________________________#





#_________________________________________________________________________________________________________________________________________________________________________________#
# BEGIN: HISTORY MODULE
history_filename = 'clinic-history.csv'
history_headers = ['Num identification','Symptoms', 'Current illness', 'Medical history', 'Family illnesses', 'Allergies', 'Treatment']
history_list = load_data_from_csv(history_filename)

def print_create_history():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                      CREATE CLINIC HISTORY                       ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_consult_history():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                      CONSULT CLINIC HISTORY                      ║
╚══════════════════════════════════════════════════════════════════╝''')
    
def print_update_history():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                      UPDATE CLINIC HISTORY                       ║
╚══════════════════════════════════════════════════════════════════╝''')

def print_delete_history():
    print_header()
    print('''
╔══════════════════════════════════════════════════════════════════╗
║                      DELETE CLINIC HISTORY                       ║
╚══════════════════════════════════════════════════════════════════╝''')

if len(patient_list) == 0:
    save_data_to_csv(history_filename, history_headers, history_list)

def find_history(identification_history):
    for history in history_list:
        if history['Num identification'] == identification_history:
            return history
    return None

def action_create_clinic_history():
    print_create_history()
    iden = input(' » Clinic history number: ')
    symptoms =  input(' » Reason for consultation: ')
    current_illness = input(' » Current illness: ')
    medical_history = input(' » Medical history: ')
    family_illnesses = input(' » Family illnesses: ')
    allergies = input(' » Allergies: ')
    treatment = input(' » Treatment: ')

    history_dict = {
        'Num identification': iden,
        'Symptoms': symptoms,
        'Current illness': current_illness,
        'Medical history': medical_history,
        'Family illnesses': family_illnesses,
        'Allergies': allergies,
        'Treatment': treatment
    }

    history_list.append(history_dict)
    save_data_to_csv(history_filename, history_headers, history_list)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_consult_clinic_history():
    print_consult_history()
    number_registration = input('» Enter the clinic history number to consult: ')
    num = find_history(number_registration)

    if num == None:
        print('═'*68)
        print(f' Clinic history with number {number_registration} was not found')
        print()
        print(' Check if the clinic history number is correct, otherwise')
        print(' the medical record may not be found in the database.')
    else:
        print('═'*68)
        print(f' Clinic history with number {number_registration} was found')
        print()
        for key, value in num.items():
            print(f' {key}: {value}')

    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_consult_all_clinic_history():
    print_consult_history()
    print(' All medical records:')
    for history_dict in history_list:
        print()
        for key, value in history_dict.items():
            print(f' {key}: {value}')

    print('═'*68)
    input(' '*16 + 'Press enter to return to the menu: ')

def action_update_clinic_history():
    print_update_history()
    input(' '*16 + 'Press enter to return to the menu: ')

def action_delete_clinic_history():
    print_delete_history()
    history_num_to_delete = input(' » Enter the clinic history number to delete: ')
    history_to_delete = find_history(history_num_to_delete)

    if history_to_delete == None:
        print('═'*68)
        print(f' Clinic history with number {history_num_to_delete} was not found')
        print()
        print(' Check if the clinic history number is correct, otherwise')
        print(' the medical record may not be found in the database.')
        print('═'*68)
    else:
        history_list.remove(history_to_delete)
        save_data_to_csv(history_filename, history_headers, history_list)

    input(' '*16 + 'Press enter to return to the menu: ')

# END: HISTORY MODULE
#_________________________________________________________________________________________________________________________________________________________________________________#





#_________________________________________________________________________________________________________________________________________________________________________________#
# BEGIN: AUTHENTICATION MODULE

auth_info = {}

def print_login_header():
    print(
'''
╔══════════════════════════════════════════════════════════════════╗
║                             LOGIN                                ║
╠══════════════════════════════════════════════════════════════════╣
║                          HELLO AGAIN!                            ║
║            Please enter the credentials to continue              ║
╚══════════════════════════════════════════════════════════════════╝
'''
    )

def log_in():
    clean_console()
    print_header()
    print_login_header()

    username = input(' » Username: ')
    user = find_user(username)

    if user == None:
        clean_console()
        print(' '*20 + 'The user is not identified!')
        return

    password = getpass.getpass(' » Password: ')

    if user['password'] == password:
        auth_info['user'] = user
    else:
        clean_console()
        print(' '*22 + 'The password is wrong!')

def log_out():
    auth_info['user'] = None

# END: AUTHENTICATION MODULE
#_________________________________________________________________________________________________________________________________________________________________________________#

def print_main_menu():
    print(
'''
╔══════════════════════════════════════════════════════════════════╗
║              WELCOME TO MEDICAL RECORDS MANAGEMENT               ║
╚══════════════════════════════════════════════════════════════════╝
 ■■■■■ We work for you leading the way to medical excellence! ■■■■■

╔══════════════════════════════════════════════════════════════════╗
║                           MAIN MENU                              ║
╠══════════════════════════════════════════════════════════════════╣
║ (1) » Login                                                      ║
║ (2) » Exit                                                       ║
╚══════════════════════════════════════════════════════════════════╝
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
