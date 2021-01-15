from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    current_portion = [start_node]
    the_order = [start_node]
    next_portion = []
    while len(the_order) < len(g.nodes):
        for node in current_portion:
            for next_node in g.neighbors(node):
                if next_node not in the_order:
                    the_order.append(next_node)
                    next_portion.append(next_node)
        current_portion = next_portion
        next_portion = []
    return "".join(the_order)
