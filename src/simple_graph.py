# -*- coding: utf-8 -*-
"""
Simple graph implementation.
"""
from __future__ import unicode_literals


class Node(object):
    """Node class.
    Has data, a unique name(string), and a list of neighboring
    node names.
    """

    def __init__(self, name, data=None):
        """Initialize the Node instance."""
        if not isinstance(name, type('')):
            raise TypeError('Name must be a string.')
        self.name = name
        self.data = data
        self.neighbors = []

    def __repr__(self):
        """Display the data in this node."""
        if hasattr(self, 'data'):
            return repr(self.data)
        return 'No data'

    def output_neighbors(self):
        """Return a list of strings indicating its neighbors."""
        output = []
        for n in self.neighbors:
            output.append("{} to {}, weight = {}".format(
                self.name,
                n[0],
                n[1]
                ))
        return output


class SimpleGraph(object):
    """SimpleGraph class which has a dict of nodes.
    The name of each node is the key, with the Node ocject being the
    value contained.
    """

    def __init__(self):
        """Initialize the graph."""
        self.node_dict = {}

    def __repr__(self):
        """Display the list of nodes."""
        return repr(self.node_dict)

    def add_node(self, n):
        """Add a node instance to the graph.
        Node must have a unique name.
        """
        if type(n) is not Node:
            raise TypeError('Arguments passed must be a Node instance.')
        if n.name in self.node_dict:
            raise KeyError('Node {} already exists as {}'.format(n.name, self))
        self.node_dict[n.name] = n

    def add_edge(self, n1, n2, weight):
        """Add n2.name to n1.neighbors.
        If either don't exist, add to graph.  n1 and n2 are Node
        instances which should be contained in the graph's node_dict.
        If n1 already contains n2 as a neighbor, n2 will not be appended
        again.  Weight is a positive integer.
        """
        try:
            if n1.name not in self.node_dict:
                self.add_node(n1)
            if n2.name not in self.node_dict:
                self.add_node(n2)
        except AttributeError:
            raise TypeError('Arguments must be Node instances.')

        if n1 is not self.node_dict[n1.name] or n2 is not self.node_dict[n2.name]:
            raise ValueError('Cannot Overwrite existing nodes in graph.')

        n1.neighbors.append((n2.name, weight))
        n1.neighbors = list(set(n1.neighbors))

    def del_node(self, n):
        """Delete node from graph.
        Also removes the node from the neighbors list from other nodes
        contained in the the node_dict.
        """
        try:
            name = n.name
            del self.node_dict[n.name]
        except KeyError:
            raise KeyError('Node does not exist in graph.')

        for key in self.node_dict:
            if name in self.node_dict[key].neighbors:
                del name

    def edges(self):
        """Return a list of all edges."""
        edges = []
        for node in self.node_dict:
            edges.extend(self.node_dict[node].output_neighbors())
        return edges

    def has_node(self, n):
        """True if Node ‘n’ inst is contained in the graph.  Else false."""
        try:
            node_in_graph = n.name in self.node_dict
        except AttributeError:
            raise TypeError('Must pass a node to has_node method.')
        return node_in_graph

    def neighbors(self, n):
        """Return the list of all nodes ‘n’ is connected to.
        Connected by edge with weight.  Raises an error if n is not in g.
        """
        try:
            node_list = self.node_dict[n.name].neighbors
        except AttributeError:
            raise TypeError('Must pass a node to neighbors method.')
        except KeyError:
            raise ValueError('Node is not contained within graph.')
        return node_list

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 -> n2.
        False if not, raises an error if either of the supplied nodes
        are not in g.
        """
        try:
            print(self.node_dict[n2.name].name)
            print(self.node_dict[n1.name].neighbors)
            for item in self.node_dict[n1.name].neighbors:
                if self.node_dict[n2.name].name in item:
                    return True
        except KeyError:
            raise ValueError(
                'Graph does not contain both nodes.  Use has_node method.'
                )
        except AttributeError:
            raise TypeError('Must pass node types to adjacent method.')
        return False

    def nodes(self):
        """Return a list of all node names contained in graph."""
        tmp = []
        for key in self.node_dict:
            tmp.append(key)
        return tmp

    def weight(self, n1, n2):
        """Return the weight of an edge.  n1 and n2 are nodes."""
        try:
            if n1.name not in self.node_dict or n2.name not in self.node_dict:
                raise KeyError('Nodes must be in graph.')
            for n in n1.neighbors:
                if n[0] == n2.name:
                    return n[1]
        except AttributeError:
            raise AttributeError('n1 and n2 must be nodes.')

    # Traversal methods
    def depth_first_traversal(self, start):
        """Perform a depth traversal.  'start' is a node."""
        curr = [start]
        ret = []

        while len(curr):
            c = curr.pop()
            ret.append(c.name)
            for n in c.neighbors:
                if self.node_dict[n[0]].name not in ret:
                    curr.append(self.node_dict[n[0]])
        return ret

    def breadth_first_traversal(self, start):
        """Perform a breadth traversal.  'start' is a node."""
        breadth_list = [start.name]
        for edge in breadth_list:
            tmp = self.neighbors(self.node_dict[edge])
            for e in tmp:
                if e[0] not in breadth_list:
                    breadth_list.append(e[0])
        return breadth_list


def heuristic(graph, curr_node):
    """Return a prediction based on the node.
    Heuristics are optimized for specific problem sets, and are underestimated.
    This one simply returns the minimum edge weight of its neighbors.
    """
    distances = [i[1] for i in graph.neighbors(curr_node)]
    try:
        return min(distances)
    except ValueError:
        return 0


def shortest_path(graph, distances, visited_set, use_heuristic=False):
    """Helper function to return node name with lowest weight from n1.
    Can use a heuristic function.
    """
    n_list = []
    h = 0
    for name, dist in distances.items():
        if name not in visited_set and dist != float('inf'):
            if use_heuristic:
                h = heuristic(graph, graph.node_dict[name])
            n_list.append((dist + h, name))
    if len(n_list):
        return min(n_list)[1]
    return None


def spt_Dijkstra(graph, start_node_name, end_node_name):
    """Perform Shortest-Path Tree."""
    distances = {}
    visited_set = set()
    for key in graph.node_dict:
        distances[key] = float('inf')
    curr_node = graph.node_dict[start_node_name]
    distances[curr_node.name] = 0

    while curr_node is not None:
        tmp = []
        for n in graph.neighbors(curr_node):
            if n not in visited_set:
                tmp.append(n[0])
            distances[n[0]] = min(distances[n[0]], distances[curr_node.name] + graph.weight(curr_node, graph.node_dict[n[0]]))
        visited_set.add(curr_node.name)
        curr_node = graph.node_dict[shortest_path(graph, distances, visited_set)]

        if curr_node is not None:
            if curr_node.name == end_node_name:
                break

    if distances[end_node_name] == float('inf'):
        return None
    return distances[end_node_name]


def spt_AStar(graph, start_node_name, end_node_name):
    """Perform Shortest-Path Tree with heuristics."""
    distances = {}
    visited_set = set()
    for key in graph.node_dict:
        distances[key] = float('inf')
    curr_node = graph.node_dict[start_node_name]
    distances[curr_node.name] = 0

    while curr_node is not None:
        tmp = []
        for n in graph.neighbors(curr_node):
            if n not in visited_set:
                tmp.append(n[0])
            distances[n[0]] = min(distances[n[0]], distances[curr_node.name] + graph.weight(curr_node, graph.node_dict[n[0]]))
        visited_set.add(curr_node.name)
        curr_node = graph.node_dict[shortest_path(graph, distances, visited_set, True)]

        if curr_node is not None:
            if curr_node.name == end_node_name:
                break

    if distances[end_node_name] == float('inf'):
        return None
    return distances[end_node_name]
