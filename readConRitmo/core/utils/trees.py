class NodoLibro:
    def __init__(self, libro):
        self.libro = libro 
        self.left = None
        self.right = None

class LibroBST:
    def __init__(self):
        self.root = None

    def insertar(self, libro):
        if not self.root:
            self.root = NodoLibro(libro)
        else: 
            self._insertar(self.root, libro)

    def _insertar(self, nodo, libro):
        if libro.titulo < nodo.libro.titulo:
            if nodo.left:
                self._insertar(nodo.left, libro)
            else:
                nodo.left = NodoLibro(libro)
        else:
            if nodo.right:
                self._insertar(nodo.right, libro)
            else:
                nodo.right = NodoLibro(libro)

    def in_order(self):
        libros_ordenados = []
        self._in_order(self.root, libros_ordenados)
        return libros_ordenados
    
    def _in_order(self, nodo, lista):
        if nodo:
            self._in_order(nodo.left, lista)
            lista.append(nodo.libro)
            self._in_order(nodo.right, lista)
        