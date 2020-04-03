import unittest
from Network.graph import Graph
from Manifold.posn import SymPos

class TestNetwork(unittest.TestCase):        
    def test_create_graph(self):
        node1 = SymPos(3)
        node2 = SymPos(3)
        g = Graph([(node1, node2)])

        self.assertEqual(g.vertex_count, 2)
        self.assertEqual(g.index_of(node1), 0)
        self.assertEqual(g.index_of(node2), 1)
    
    def test_vertex_neighbors(self):
        node1 = SymPos(3)
        node2 = SymPos(3)
        node3 = SymPos(3)
        node4 = SymPos(4)
        g = Graph([(node1, node2)])
        neighborhoods = []

        g.add_connections([(node2, node4)])
        g.add_connections([(node2, node3)])
        neighborhoods.append(g.neighbors_of_index(0))
        neighborhoods.append(g.neighbors_of_index(1))
        neighborhoods.append(g.neighbors_of_index(2))
        neighborhoods.append(g.neighbors_of_index(3))

        self.assertEqual(neighborhoods[0], {1})
        self.assertEqual(neighborhoods[1], {0,2,3})
        self.assertEqual(neighborhoods[2], {1})
        self.assertEqual(neighborhoods[3], {1})
    
    def test_divergence(self):
        node1 = SymPos(3)
        node2 = SymPos(3)
        node3 = SymPos(3)
        g = Graph([(node1, node2)])
        
        g.add_connections([(node2, node3)])
        dist = 2*(node1.distance(node2) + node2.distance(node3))

        self.assertAlmostEqual(g.total_graph_divergence, dist)



    

    


        
        
        
    

    



        


