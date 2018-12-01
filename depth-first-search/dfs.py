"""
Author: Valerio Velardo
Email: valeriovelardo@gmail.com
Website: http://valeriovelardo.com
Python AI mailing list (free AI and ML tutorials): https://bit.ly/2K4gqE5

This file contains an implementation of depth-first search (BFS) for
traversing a graph.
"""

def dfs_connected_component(graph, start):
    """Visits all the nodes of a search space (connected component) using DFS

    Args:
        graph (dict): Search space represented by a graph
        start (str): Starting state

    Returns:
        explored (list): List of the explored nodes
    """

    # list to keep track of all visited nodes
    explored = [ ]

    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:

        # pop last node (first node) from queue. This is the only difference
        # between DFS and BFS
        node = queue.pop()

        if node not in explored:

            # add node to list of checked nodes
            explored.append(node)

            # get neighbours if node is present, otherwise default to empty
            # list
            neighbours = graph.get(node, [ ])

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)

    return explored


if __name__ == '__main__':

    # sample search space, represented by a dictionary
    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    explored = dfs_connected_component(graph, 'A')

    print("\nHere's the nodes of the search space visited by "
          "depth-first search, starting from node 'A': {}".format(explored))
