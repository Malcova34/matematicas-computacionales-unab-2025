import random
import matplotlib.pyplot as plt
import networkx as nx

# -----------------------
# Clase Nodo
# -----------------------
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# -----------------------
# Clase Árbol Binario
# -----------------------
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregarValor(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(self.raiz, valor)

    def _agregar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar(nodo.derecho, valor)

    def buscarValor(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierdo, valor)
        else:
            return self._buscar(nodo.derecho, valor)

    def imprimirValores(self):
        valores = []
        self._inOrden(self.raiz, valores)
        return valores

    def _inOrden(self, nodo, valores):
        if nodo:
            self._inOrden(nodo.izquierdo, valores)
            valores.append(nodo.valor)
            self._inOrden(nodo.derecho, valores)

# -----------------------
# Visualización del Árbol
# -----------------------
def agregar_nodos_edges(nodo, graph, pos={}, x=0, y=0, nivel=1):
    if nodo is not None:
        pos[nodo.valor] = (x, y)
        if nodo.izquierdo:
            graph.add_edge(nodo.valor, nodo.izquierdo.valor)
            pos = agregar_nodos_edges(nodo.izquierdo, graph, pos, x - 1 / 2 ** nivel, y - 1, nivel + 1)
        if nodo.derecho:
            graph.add_edge(nodo.valor, nodo.derecho.valor)
            pos = agregar_nodos_edges(nodo.derecho, graph, pos, x + 1 / 2 ** nivel, y - 1, nivel + 1)
    return pos

def graficar_arbol(raiz):
    G = nx.DiGraph()
    pos = agregar_nodos_edges(raiz, G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=10, font_weight='bold', arrows=False)
    plt.title("Árbol Binario de Búsqueda")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# -----------------------
# Programa Principal
# -----------------------
if __name__ == "__main__":
    # Generar 20 números únicos aleatorios
    numeros = random.sample(range(1, 101), 20)
    print("Números generados:", numeros)

    # Crear el árbol
    arbol = ArbolBinario()
    for num in numeros:
        arbol.agregarValor(num)

    # Menú
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar número en el árbol")
        print("2. Imprimir valores en orden ascendente")
        print("3. Mostrar gráfico del árbol")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese el número a buscar: "))
            encontrado = arbol.buscarValor(valor)
            print("Resultado:", "Encontrado" if encontrado else "No encontrado")
        elif opcion == "2":
            ordenados = arbol.imprimirValores()
            print("Valores en orden ascendente:", ordenados)
        elif opcion == "3":
            graficar_arbol(arbol.raiz)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
