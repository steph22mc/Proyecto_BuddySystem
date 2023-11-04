# Importar clases
from block import Block

class ProcessTreeNode:

    def __init__(self, size):
        self.size = size
        self.process = None
        self.left_child = None
        self.right_child = None