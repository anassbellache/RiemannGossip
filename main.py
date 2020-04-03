from Network.graph import Graph
from Manifold.posn import SymPos
from Manifold.rotations import Rotation
import numpy as np
import matplotlib.pyplot as plt

def generate_linear_graph(num_elts):
    vertices = []
    for _ in range(num_elts):
        vertices.append(SymPos(3))
    g = Graph([])
    for i in range(1, num_elts):
        g.add_connections([(vertices[i-1], vertices[i])])
    return g

def generate_complete_graph(num_elts):
    vertices = []
    for _ in range(num_elts):
        vertices.append(SymPos(3))
    g = Graph([])
    for i in range(num_elts):
        for j in range(i):
            g.add_connections([(vertices[i], vertices[j])])
    return g

def update(g):
    node1, node2 = g.random_tuple()
    mid = node1.midpoint(node2)
    node1.coordinates = mid.coordinates
    node2.coordinates = mid.coordinates

if __name__ == '__main__':
    N_elts = 50
    N_iter = 200
    divergence = []
    g = generate_complete_graph(N_elts)
    print("Graph generated")
    for i in range(N_iter):
        div = g.total_graph_divergence
        divergence.append(div)
        if i % 10 == 0:
            print("epoch: {}, divergence:{}".format(i, div))
        update(g)
    x = np.arange(0, N_iter, 1)
    y = np.array(divergence)
    plt.plot(x, y)
    plt.show()

    
    