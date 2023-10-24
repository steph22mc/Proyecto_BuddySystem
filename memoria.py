class Memoria:
class Memoria:
    def _init_(self, tamaño):
        self.tamaño = tamaño
        self.bloques = [Block(dirección=i, tamaño=64, ocupado=False) for i in range(0, tamaño, 64)]

    def asignar_memoria(self, proceso):
        for bloque in self.bloques:
            if not bloque.ocupado and bloque.tamaño >= proceso.tamaño:
                bloque.marcar_ocupado()
                return True
        return False

    def liberar_memoria(self, proceso):
        for bloque in self.bloques:
            if bloque.ocupado and bloque.tamaño >= proceso.tamaño:
                bloque.marcar_libre()
                return True
        return False

    def imprimir_estado(self):
        for bloque in self.bloques:
            print(bloque)

from block import Block

    
    pass
