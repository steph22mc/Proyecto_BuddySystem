from memoria import Memoria
from proceso import Proceso

class MemoryManager:
    def __init__(self, total_size):
        # Inicializa el administrador de memoria con un tamaño total y una instancia de la memoria.
        self.memory = Memoria(total_size)
        self.processes = []  # Inicializa una lista vacía para llevar un registro de los procesos asignados.
    
    def asignar_proceso(self, size):
        process = Proceso(size)  # Crea un nuevo proceso con un tamaño específico.
        if self.memory.asignar_memoria(process):
            # Intenta asignar memoria para el proceso en la memoria actual.
            self.processes.append(process)  # Agrega el proceso a la lista de procesos asignados.
            print("Asignación exitosa!")  # Muestra un mensaje de éxito si se asigna la memoria correctamente.
            return True
        else:
            print("No hay suficiente memoria para este proceso.")
            # Muestra un mensaje de error si no hay suficiente memoria para el proceso.
            return False
    
    def liberar_proceso(self, size):
        process_to_remove = None
        # Inicializa una variable para almacenar el proceso que se eliminará.
        for process in self.processes:
            if process.tamaño == size:
                # Busca un proceso en la lista de procesos asignados que coincida con el tamaño especificado.
                process_to_remove = process
                break
        if process_to_remove:
            # Si se encuentra un proceso que coincida, procede a eliminarlo.
            self.memory.liberar_memoria(process_to_remove)
            # Libera la memoria asignada al proceso.
            self.processes.remove(process_to_remove)
            # Elimina el proceso de la lista de procesos asignados.
            print(f"Desasignación exitosa del proceso de tamaño {size}.")
            # Muestra un mensaje de éxito después de la desasignación.
        else:
            print(f"No se encontró una asignación de tamaño {size}.")
            # Muestra un mensaje si no se encuentra una asignación con el tamaño especificado.
    
    def print_memory_map(self):
        # Muestra el mapa de asignación de memoria, incluyendo los bloques y su estado (ocupado o libre).
        for block in self.memory.bloques:
            if block.ocupado:
                print(f"Block Size: {block.tamaño}, Allocated to Process: {block.process.tamaño}")
            else:
                print(f"Block Size: {block.tamaño}, Free")
    
    def print_memory_state(self):
        print("\nEstado de la Memoria:")
        # Imprime el estado actual de la memoria, incluyendo información sobre bloques libres y ocupados.
        free_blocks = self.memory.get_free_blocks()
        # Obtiene la lista de bloques de memoria libres.

        if not free_blocks:
            print("Todos los bloques están asignados.")
            # Si no hay bloques de memoria libres, muestra un mensaje indicando que todos los bloques están asignados.
        else:
            print(f"Cantidad de bloques libres: {len(free_blocks)}")
            print("Bloques libres:")
            for size, index in free_blocks:
                print(f"Tamaño: {size}, Dirección: {index}")
            # Si hay bloques de memoria libres, muestra información sobre la cantidad y detalles de cada bloque libre.
        
        print("Bloques Ocupados:")
        for block in self.memory.bloques:
            if block.ocupado:
                
                print(f"Block Size: {block.tamaño}, Allocated to Process: {block.process.tamaño}")
            # Muestra información sobre bloques ocupados, incluyendo su tamaño y el tamaño del proceso asignado.

