"""
Author: Valerio Velardo
Email: valeriovelardo@gmail.com
Website: http://valeriovelardo.com
Python AI mailing list (free AI and ML tutorials): https://bit.ly/2K4gqE5

This file contains an implementation of breadth-first search (BFS) for
traversing a graph, and for getting the shortest path between 2 nodes
of a graph.
"""

def bfs_connected_component(graph, start):
    """Visits all the nodes of a search space (connected component) using BFS

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

        # pop shallowest node (first node) from queue
        node = queue.pop(0)

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


def bfs_shortest_path(graph, start, goal):
    """Finds shortest path between 2 nodes in search space using BFS

    Args:
        graph (dict): Search space represented by a graph
        start (str): Starting state
        goal (str): Goal state

    Returns:
        new_path (list): List of the states that bring you from the start to
            the goal state, in the quickest way possible
    """

    # keep track of explored nodes
    explored = [ ]

    # keep track of all the paths to be checked
    queue = [start]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start == goal"

    # keep looping until all possible paths have been checked
    while queue:

        # pop the first path from the queue
        path = queue.pop(0)

        # get the last node from the path
        node = path[-1]
        if node not in explored:

            # get neighbours if node is present, otherwise default to empty
            # list
            neighbours = graph.get(node, [ ])

            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


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

    explored = bfs_connected_component(graph, 'A')
    shortest_path = bfs_shortest_path(graph, 'G', 'D')

    print("\nHere's the nodes of the search space visited by "
          "breadth-first search, starting from node 'A': {}".format(explored))

    print("\nHere's the shortest path between nodes 'G' and 'D': {}".format(
        shortest_path))