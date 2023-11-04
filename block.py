#raul luna
class Block:
    def __init__(self, tamaño):
        self.tamaño = tamaño  # Inicializa el bloque con un tamaño dado.
        self.ocupado = False # Inicialmente, el bloque no está ocupado.
        self.process = None # Inicialmente, el bloque no tiene asignado ningún proceso.

    def marcar_ocupado(self, process):
        """
        Marca el bloque como ocupado y asigna un proceso a él.

        Parametro:
            process: El proceso que se asignará al bloque.
        """
        self.ocupado = True
        self.process = process

    def marcar_libre(self):
        """
        Marca el bloque como libre y desasigna el proceso asociado.
        """
        self.ocupado = False
        self.process = None
    
    def dividir(self):
        """
        Divide el bloque en dos si es posible.

        Retorna:
            Un nuevo bloque creado a partir de la división si es posible, o None si no se puede dividir más.
        """
        if self.tamaño >= 2:
            new_size = self.tamaño // 2
            new_block = Block(new_size) # Crea un nuevo bloque con la mitad del tamaño.
            self.tamaño = new_size # Actualiza el tamaño del bloque actual.
            return new_block
        return None
    
    def is_divisible(self, required_size):
        """
        Verifica si el bloque se puede dividir en bloques más pequeños para acomodar un tamaño requerido.

        Parametro:
            required_size: El tamaño requerido.

        Retorna:
            True si el bloque se puede dividir para acomodar el tamaño requerido, False en caso contrario.
        """
        return self.tamaño / 2 >= required_size

    def __str__(self):
        # Devuelve una representación en cadena del bloque, incluyendo su dirección, tamaño y estado.
        estado = "Ocupado" if self.ocupado else "Libre"
        return f"Dirección: {self.dirección}, Tamaño: {self.tamaño}, Estado: {estado}"