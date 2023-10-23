#raul luna
    class Block:
    def __init__(self, dirección, tamaño, ocupado):
        self.dirección = dirección 
        self.tamaño = tamaño  
        self.ocupado = ocupado  

    def marcar_ocupado(self):
        self.ocupado = True

    def marcar_libre(self):
        self.ocupado = False

    def __str__(self):
        estado = "Ocupado" if self.ocupado else "Libre"
        return f"Dirección: {self.dirección}, Tamaño: {self.tamaño}, Estado: {estado}"
pass
