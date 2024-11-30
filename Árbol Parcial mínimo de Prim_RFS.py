import sys
import networkx as nx
import matplotlib.pyplot as plt

V = 6  # Número de vértices

# Función para seleccionar el vértice con el valor mínimo
def select_min_vertex(value, set_mst):
    minimum = sys.maxsize
    vertex = -1
    for i in range(V):
        if not set_mst[i] and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex

# Función para encontrar el MST
def find_mst(graph):
    parent = [-1] * V  # Almacena el MST
    value = [sys.maxsize] * V  # Usado para la relajación de los bordes
    set_mst = [False] * V  # True -> Vértice incluido en el MST

    # Asumimos que el punto de inicio es el Nodo-0
    value[0] = 0  # El nodo de inicio tiene valor 0 para ser seleccionado primero

    # Formamos el MST con (V-1) aristas
    for _ in range(V - 1):
        # Seleccionamos el mejor vértice aplicando el método codicioso
        u = select_min_vertex(value, set_mst)
        set_mst[u] = True  # Incluimos el nuevo vértice en el MST

        # Relajamos los vértices adyacentes (no incluidos en el MST)
        for j in range(V):
            if graph[u][j] != 0 and not set_mst[j] and graph[u][j] < value[j]:
                value[j] = graph[u][j]
                parent[j] = u

    # Imprimimos el MST
    edges = []
    for i in range(1, V):
        print(f'U->V: {parent[i]}->{i}  wt = {graph[parent[i]][i]}')
        edges.append((parent[i], i, graph[parent[i]][i]))

    # Visualización del grafo y el MST
    plot_graph(graph, edges)

# Función para visualizar el grafo y el MST
def plot_graph(graph, mst_edges):
    G = nx.Graph()

    # Agregamos los nodos y los bordes al grafo
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Dibujamos el grafo original
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold', edge_color='gray')

    # Dibujamos las aristas del MST
    mst = nx.Graph()
    mst.add_weighted_edges_from(mst_edges)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)

    # Mostramos las etiquetas de peso en las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("MST Visualizado en un Grafo")
    plt.show()

# Función principal
def main():
    graph = [
        [0, 4, 6, 0, 0, 0],
        [4, 0, 6, 3, 4, 0],
        [6, 6, 0, 1, 8, 0],
        [0, 3, 1, 0, 2, 3],
        [0, 4, 8, 2, 0, 7],
        [0, 0, 0, 3, 7, 0]
    ]
    
    find_mst(graph)

# Llamada a la función principal
if __name__ == "__main__":
    main()
