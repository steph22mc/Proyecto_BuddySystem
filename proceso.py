#raul luna
class Proceso:
     def __init__(self, nombre, tamaño):
        self.nombre = nombre  
        self.tamaño = tamaño  

    def __str__(self):
        return f"Proceso: {self.nombre}, Tamaño: {self.tamaño} bytes"
    pass
