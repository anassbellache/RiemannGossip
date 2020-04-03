from collections import defaultdict
import numpy as np


class Graph(object):
    def __init__(self, connections, directed=False):
        """The graph in the connections 
        
        Arguments:
            connections {List(Tuple)} -- list of edges
        
        Keyword Arguments:
            directed {boolean} -- Is the graph directed or not
        """
        self._graph = defaultdict(set)
        self._directed = directed
        self._index_count = 0
        self._vertex_to_index = {}
        self.add_connections(connections)
    
    def add_connections(self, connections):
        """Add new edges to the graph
        
        Arguments:
            connections {List(Tuple)} -- List of edges (each edge is a tuple of two elements)
        """
        for node1, node2 in connections:
            self._add_vertex(node1)
            self._add_vertex(node2)
            self._add_edge(node1, node2)
    
    def _add_vertex(self, node):
        if node not in self._vertex_to_index:
            self._vertex_to_index[node] = self._index_count
            self._index_count += 1
            
    def _add_edge(self, node1, node2):
        index1 = self._vertex_to_index[node1]
        index2 = self._vertex_to_index[node2]
        self._graph[index1].add(index2)
        if not self._directed:
            self._graph[index2].add(index1)
    
    @property
    def vertex_count(self):
        return len(self._graph.keys())
    
    def _inverse_dict(self):
        return {v:k for k,v in self._vertex_to_index.items()}
    
    def vertex_at(self, index, index_to_vertex):
        return index_to_vertex[index]
    
    def index_of(self, vertex):
        return self._vertex_to_index[vertex]
    
    @property
    def total_graph_divergence(self):
        """The value of the divergence function for the graph
        
        Returns:
            float -- divergence function value
        """
        divergence = 0
        index_to_vertex = self._inverse_dict()
        for i in self._graph:
            node1 = index_to_vertex[i]
            for j in self.neighbors_of_index(i):
                node2 = index_to_vertex[j]
                divergence += node1.distance(node2)
        return divergence
    
    def neighbors_of_index(self, index):
        return self._graph[index]
    
    def random_tuple(self):
        i = np.random.randint(0, self.vertex_count)
        neighbors = self._graph[i]
        j = next(iter(neighbors))
        index_to_vertex = self._inverse_dict()
        return index_to_vertex[i], index_to_vertex[j]
    
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))