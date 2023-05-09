import networkx as nx
import matplotlib.pyplot as plt


# Función que encuentra un camino de Euler en un grafo no dirigido y conexo

def fleury_algorithm(G, start_node):
    # Inicialización de variables
    visited = []
    path = []
    current_node = start_node

    # Ciclo principal
    while len(path) < len(G.edges()):
        path.append(current_node)
        neighbors = list(G.neighbors(current_node))

        # Si el vertice actual tiene un adyacente, se visita ese adyacente
        if len(neighbors) == 1:
            visited.append(current_node)
            next_node = neighbors[0]
        else:
            # Se elige un vertice adyacente que no corte el grafo
            for neighbor in neighbors:
                if not is_cut_node(G, current_node, neighbor):
                    next_node = neighbor
                    break
            visited.append(current_node)

        # Se mueve al siguiente vertice
        current_node = next_node

    # Se agrega el último vertice al camino
    path.append(current_node)

    return path


# Función que determina si un vertice es un corte en del grafo
def is_cut_node(G, node, neighbor):
    # Se elimina el vertice y se verifica si el grafo se desconecta
    G.remove_edge(node, neighbor)
    connected = nx.is_connected(G)
    G.add_edge(node, neighbor)
    return not connected


# Obtener la matriz de adyacencia del usuario
n = int(input("Ingrese el número de vertices: "))
matriz = []
for i in range(n):
    fila = list(map(int, input(f"Ingrese la fila {i + 1} de la matriz separando los elementos por espacios: ").split()))
    matriz.append(fila)

# Crear el grafo a partir de la matriz
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if matriz[j][i] == 1:
            G.add_edge(i + 1, j + 1)

# Obtener el vertice inicial del usuario
start_node = int(input("Ingrese el vertce inicial: "))

# Encontrar el camino euleriano
path = fleury_algorithm(G, start_node)

# Imprimir el camino euleriano
path = fleury_algorithm(G, start_node)
print("Camino de Euler: ", path)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()