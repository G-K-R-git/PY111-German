from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    counted shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    visited = []
    current_node = starting_node
    node_weights = {node: float("inf") for node in g}
    node_weights[starting_node] = 0
    next_node = None
    to_visit_later = set()
    while len(visited) < len(g):
        next_node_weight = float("inf")
        counted = 0  # Количество непосещённых соседей у текущего узла
        for node in g.neighbors(current_node):
            if node not in visited:
                counted += 1
                if (g[current_node][node]["weight"] + node_weights[current_node]) < node_weights[node]:
                    node_weights[node] = g[current_node][node]["weight"] + node_weights[current_node]
                if node_weights[node] <= next_node_weight:  # Проверка на выбор следующего узла
                    if node_weights[node] == next_node_weight:  # Если вес рассматриваемого узла уже был
                        to_visit_later.add(node)                # в одном из других узлов, то записываем его
                    next_node = node
                    next_node_weight = node_weights[node]
        if not counted:  # Если не осталось соседей
            if not to_visit_later:  # И нет узлов с развилками
                return node_weights
            else:  # Обработка развилки (встречены соседи с одинаковыми весами)
                current_node = to_visit_later.pop()
                visited.append(current_node)
        else:  # Ветка если остались соседи у текущего узла
            visited.append(current_node)
            current_node = next_node
    return node_weights


if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_nodes_from("ABCDEFG")
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    print(dijkstra_algo(G, 'A'),"\n" ,dijkstra_algo(G, 'D'))
    nx.draw_planar(G, with_labels=True)
    plt.show()
