from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    the_order = []
    depth_stack = [start_node]
    while len(the_order) < len(g):
        current_node = depth_stack.pop()
        the_order.append(current_node)
        for neighbour in g.neighbors(current_node):
            if neighbour not in the_order:
                depth_stack.append(neighbour)
    return the_order
