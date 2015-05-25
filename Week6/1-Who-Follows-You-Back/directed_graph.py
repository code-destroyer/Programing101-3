import requests


r = requests.get('https://api.github.com/users/code-destroyer?client_id=e5c28458254f1ff935ae&client_secret=    657bc35ae8dec386d7d1b24853375afba253ace7')
print(r)


class DirectedGraph:

    def __init__(self):
        self.graph_dict = {}

    def build_network(self, start, level):
        visited = set()
        queue = []
        visited.add(start)
        queue.append(start)

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == level:
                break

        network = DirectedGraph.get_neighbors_for(self, current_node)
        for follower in network("followers"):
            if follower not in visited:
                queue.add_edge(follower, current_node)
                visited.add(follower)
                queue.append(current_node+1, follower)

    def add_edge(self, node_a, node_b):
        # edge = set()
        # (node_a, node_b) = tuple(edge)
        if node_a not in self.graph_dict:
            self.graph_dict[node_a] = [node_b]
        else :
            self.graph_dict[node_a].append(node_b)
        if node_b not in self.graph_dict:
            self.graph_dict[node_b] = []

    def get_neighbors_for(self, node):
        if node not in self.graph_dict:
            print("Node is not in the graph!")
            return
        return self.graph_dict[node]

    def print_graph(self):
        print(self.graph_dict)



