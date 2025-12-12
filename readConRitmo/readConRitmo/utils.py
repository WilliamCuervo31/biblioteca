from core.models import Etiqueta

def obtener_descendientes(etiqueta):

    resultado = []

    def dfs(nodo):
        hijos = Etiqueta.objects.filter(padre=nodo)

        for hijo in hijos:
            resultado.append(hijo)  
            dfs(hijo)

    dfs(etiqueta)

    return resultado