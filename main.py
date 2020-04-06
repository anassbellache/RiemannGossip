import click
from Network.graph import Graph
from Manifold.posn import SymPos
from Manifold.rotations import Rotation
import numpy as np
import matplotlib.pyplot as plt


def generate_manifold(data_space):
    if data_space == 'posn':
        return SymPos(3)
    elif data_space == 'rotations':
        return Rotation()
    else:
        return None

def generate_linear_graph(num_elts, data_space):
    vertices = []
    for _ in range(num_elts):
        vertices.append(generate_manifold(data_space))
    g = Graph([])
    for i in range(1, num_elts):
        g.add_connections([(vertices[i-1], vertices[i])])
    return g

def generate_complete_graph(num_elts, data_space):
    vertices = []
    for _ in range(num_elts):
        vertices.append(generate_manifold(data_space))
    g = Graph([])
    for i in range(num_elts):
        for j in range(i):
            g.add_connections([(vertices[i], vertices[j])])
    return g

def generate_graph(graph_type, num_elts, data_space):
    if graph_type == 'linear':
        return generate_linear_graph(num_elts, data_space)
    elif graph_type == 'complete':
        return generate_complete_graph(num_elts, data_space)
    else:
        return None

def update(g):
    node1, node2 = g.random_tuple()
    mid = node1.midpoint(node2)
    node1.coordinates = mid.coordinates
    node2.coordinates = mid.coordinates

@click.command()
@click.argument('space')
@click.option('--graph_type', '-g', default='linear')
@click.option('--num_elts', '-n', default=50)
@click.option('--epochs', '-e', default=100)
def main(space, graph_type, num_elts, epochs):
    divergence = []
    g = generate_graph(graph_type, num_elts, space)
    print("Graph generated")
    for i in range(epochs):
        div = g.total_graph_divergence
        divergence.append(div)
        if i % 10 == 0:
            print("epoch: {}, divergence:{}".format(i, div))
        update(g)
    x = np.arange(0, epochs, 1)
    y = np.array(divergence)
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()

    
    