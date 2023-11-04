# Importar la clase MemoryManager del archivo memory_manager.py
# y el módulo OS para centrar el texto de bienvenida
from memory_manager import MemoryManager
import os


# Funcion para obtener una entreda de valor entero del usuario con manejo de excepciones
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt)) # Solicita al usuario que ingrese un valor entero y lo almacena en la variable "value".
            if value <= 1: # Comprueba si el valor ingresado es menor o igual a 1.
                print("El valor debe ser un número entero mayor que 1.")
            else:
                return value # Si el valor es un entero válido y cumple con las restricciones, se devuelve como resultado de la función.
        except ValueError:
            print("Ingresa un valor entero válido. Inténtalo de nuevo.") # Maneja la excepción si el usuario ingresa un valor que no es un entero y muestra un mensaje de error.

if __name__ == "__main__":
    #Mensaje de Bienvenida y descripcion del Sistema
    message = '''
            ____        _____           _                   
            |  _ \      / ____|         | |                _ 
            | |_) |____| (___  _   _ ___| |_ ___ _ __ ___ (_)
            |  _ <______\___ \| | | / __| __/ _ \ '_ ` _ \   
            | |_) |     ____) | |_| \__ \ ||  __/ | | | | |_ 
            |____/     |_____/ \__, |___/\__\___|_| |_| |_(_)
                                __/ |                        
                                |___/                         


    Bienvenido al Sistema de Asignación de Memoria
    === ======= ======= = ======= === ========= ========
    Simulación de Sistema Compañero (03-11-2023)
    by Raúl Luna, Joel Canto y Estephany Martinez
    Este sistema te permite gestionar
    la asignación y liberación de memoria utilizando
    el método Buddy System.

    B-System it's in: https://github.com/steph22mc/Proyecto_BuddySystem.git
    '''
    # Dividir el mensaje en líneas individuales utilizando el carácter de salto de línea '\n' como separador.
    lines = message.split('\n')

    # Calcula la longitud máxima de todas las líneas en la lista 'lines'.
    # Esto se hace calculando la longitud de cada línea y seleccionando la más larga.
    max_line_length = max(len(line) for line in lines)

    # Centrar cada línea del mensaje y reconstruir el mensaje centrado.
    # Crear un nuevo mensaje centrado en la pantalla a partir del mensaje original dividido en líneas.
    centered_message = '\n'.join(line.center(max_line_length) for line in lines)
    print(centered_message)

    # Obtener el tamaño total de la memoria (potencia de 2) del usuario
    total_size = get_integer_input("Ingrese el tamaño total de la memoria (potencia de 2): ")

    # Verificar si el tamaño de la memoria es una potencia de 2.
    while total_size & (total_size - 1) != 0: 
        print("El tamaño de la memoria debe ser una potencia de 2.")
        total_size = get_integer_input("Ingrese el tamaño total de la memoria (potencia de 2): ")

    # Inicializar el gestor de memoria con el tamaño total especificado.
    manager = MemoryManager(total_size)

    while True:
        # Mostrar las opciones de gestión de memoria.
        print("\nOpciones de Gestión de Memoria:")
        print("1. Asignar Proceso")
        print("2. Desasignar Proceso")
        print("3. Mostrar Mapa de Memoria")
        print("4. Mostrar Estado de la Memoria")
        print("5. Limpiar Pantalla")
        print("6. Salir")
        choice = input("Ingrese su elección: ")

        if choice == '1':
            # Opción para asignar un proceso.
            size = get_integer_input("Ingrese el tamaño del proceso: ")
            if size <= 0:
                print("El tamaño del proceso debe ser un número entero mayor que 0.")
            else:
                manager.asignar_proceso(size)
        elif choice == '2':
            # Opción para desasignar un proceso.
            size = get_integer_input("Ingrese el tamaño del proceso a desasignar: ")
            if size <= 0:
                print("El tamaño del proceso a desasignar debe ser un número entero mayor que 0.")
            else:
                manager.liberar_proceso(size)
        elif choice == '3':
            # Opción para mostrar el mapa de asignación de memoria.
            print(f"\nMapa de Asignación de Memoria {total_size}:")
            manager.print_memory_map()
        elif choice == '4':
            # Opción para mostrar el estado de la memoria.
            manager.print_memory_state()
        elif choice == '5':
            # Opción para limpiar la pantalla
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
            print(centered_message) # Vuelve a mostrar el mensaje de bienvenida
        elif choice == '6':
            # Opción para salir del programa.
            print("Saliendo del Sistema de Asignación de Memoria. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")