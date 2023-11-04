#raul luna
class Proceso:
    def __init__(self, tamaño):
        self.tamaño = tamaño  # Inicializa un proceso con un tamaño dado.

    def __str__(self):
        """
        Devuelve una representación en cadena del proceso.

        Retorna:
            Una cadena que describe el proceso, incluyendo su tamaño en kilobytes (kbytes).
        """
        return f"Proceso, Tamaño: {self.tamaño} kbytes"