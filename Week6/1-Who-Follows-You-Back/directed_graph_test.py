from directed_graph import DirectedGraph
import unittest


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def set_up_graph(self):
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "F")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("D", "C")
        self.graph.add_edge("Z", "D")

    def test_add_edge(self):
        self.graph.add_edge("A", "B")
        graph_repr = {
            "A":["B"],
            "B":[]
        }
        self.assertEqual(self.graph.graph_dict, graph_repr)

    def test_path_between_true(self):
        self.set_up_graph()
        self.assertTrue(self.graph.build_network("A", "C"))

    def test_path_between_false(self):
        self.set_up_graph()
        self.assertFalse(self.graph.build_network("B", "Z"))

if __name__ == '__main__':
    unittest.main()
