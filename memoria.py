from block import Block
class Memoria:
    def __init__(self, tamaño):
        # Inicializa la memoria con un tamaño especificado y crea un bloque inicial del tamaño total.
        self.tamaño = tamaño
        self.bloques = [Block(tamaño)]

    def asignar_memoria(self, proceso):
        """
        Asigna memoria a un proceso si hay bloques disponibles.

        Parametro:
            proceso: El proceso que se va a asignar a la memoria.

        Retorna:
            True si se asigna memoria al proceso, False si no hay espacio suficiente.
        """
        for bloque in self.bloques:
            if not bloque.ocupado and bloque.tamaño >= proceso.tamaño:
                # Verifica si el bloque no está ocupado y si su tamaño es mayor o igual al tamaño del proceso.
                while bloque.tamaño >= 2 * proceso.tamaño:
                    # Mientras el tamaño del bloque sea al menos el doble del tamaño del proceso, dividir el bloque.
                    new_block = bloque.dividir()
                    if new_block:
                        # Si se puede dividir el bloque, inserta el nuevo bloque en la lista de bloques.
                        self.bloques.insert(self.bloques.index(bloque) + 1, new_block)
                # Marca el bloque como ocupado por el proceso.
                bloque.marcar_ocupado(proceso)
                return True  # Indica que se asignó memoria al proceso.
        return False  # Si llega aquí, no se encontró un bloque adecuado para asignar memoria al proceso.


    def liberar_memoria(self, proceso):
        """
        Libera la memoria ocupada por un proceso y fusiona bloques libres adyacentes.

        Parametro:
            proceso: El proceso cuya memoria se va a liberar.
        """
        for bloque in self.bloques:
            if bloque.ocupado and bloque.process == proceso:
                # Si el bloque está ocupado y pertenece al proceso especificado.
                bloque.marcar_libre()  # Marca el bloque como libre.
                self.unir_blocks()  # Llama a la función para fusionar bloques libres adyacentes.

    def split_block(self, bloque, size):
        """
        Divide un bloque en dos bloques más pequeños.

        Parametro:
            bloque: El bloque que se va a dividir.
            size: El tamaño mínimo para dividir el bloque.
        """
        index = self.bloques.index(bloque)  # Encuentra el índice del bloque que se va a dividir.
        while bloque.tamaño > size:  # Mientras el tamaño del bloque sea mayor que el tamaño mínimo para dividir:
            new_block = Block(bloque.tamaño // 2, ocupado=False)  # Crea un nuevo bloque con la mitad del tamaño del bloque actual y sin ocupar.
            self.bloques.insert(index + 1, new_block)  # Inserta el nuevo bloque después del bloque actual en la lista de bloques.
            bloque.tamaño = bloque.tamaño // 2  # Reduce el tamaño del bloque actual a la mitad.

    
    def unir_blocks(self):
        """
        Fusiona bloques libres adyacentes en la memoria.
        """
        i = 0  # Inicializa un índice para recorrer la lista de bloques.
        while i < len(self.bloques) - 1:  # Mientras no se haya llegado al último bloque.
            if not self.bloques[i].ocupado and not self.bloques[i + 1].ocupado:
                # Si el bloque actual y el siguiente no están ocupados.
                self.bloques[i].tamaño += self.bloques[i + 1].tamaño  # Fusiona el bloque actual con el siguiente.
                del self.bloques[i + 1]  # Elimina el siguiente bloque que ya no es necesario.
            else:
                i += 1  # Si no se fusionan, pasa al siguiente bloque en la lista.

    
    def get_free_blocks(self):
        """
        Obtiene una lista de bloques libres junto con sus tamaños y ubicaciones.

        Retorna:
            Una lista de tuplas, donde cada tupla contiene el tamaño y la ubicación de un bloque libre.
        """
        free_blocks = []  # Inicializa una lista vacía para almacenar bloques de memoria libres.
        for index, block in enumerate(self.bloques):
            # Itera a través de todos los bloques de memoria en la lista 'self.bloques' junto con su índice.
            if not block.ocupado:
                # Comprueba si el bloque no está ocupado (es decir, está libre).
                free_blocks.append((block.tamaño, index))
                # Si el bloque está libre, agrega una tupla que contiene su tamaño y su ubicación (índice) en la memoria a la lista 'free_blocks'.
        return free_blocks  # Devuelve la lista de bloques de memoria libres junto con sus tamaños y ubicaciones.
