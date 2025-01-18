class Graph:
    def __init__(self):
        self.graph = {}  # Store the graph as adjacency list

    def add_node(self, node, neighbors):
        """
        Add a node with its neighbors and their costs.
        :param node: The current node.
        :param neighbors: List of tuples (neighbor(s), cost).
                         If it's an AND node, pass a list of neighbors.
        """
        self.graph[node] = neighbors

    def ao_star(self, node):
        """
        Perform AO* search from the starting node.
        :param node: The starting node.
        :return: The total cost and the optimal path.
        """
        if node not in self.graph or not self.graph[node]:  # Leaf node
            return 0, [node]

        best_cost = float('inf')
        best_path = []

        for neighbors, cost in self.graph[node]:
            if isinstance(neighbors, list):  # AND node
                sub_cost = 0
                sub_path = []
                for sub_node in neighbors:
                    c, p = self.ao_star(sub_node)
                    sub_cost += c
                    sub_path += p
                total_cost = cost + sub_cost
                path = [node] + sub_path
            else:  # OR node
                total_cost, path = cost + self.ao_star(neighbors)[0], [node] + self.ao_star(neighbors)[1]

            # Update the best cost and path
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path

        return best_cost, best_path


# Example Usage
graph = Graph()
graph.add_node('A', [(['B', 'C'], 1), ('D', 2)])  # A has AND and OR options
graph.add_node('B', [('E', 1), ('F', 2)])  # B has two OR options
graph.add_node('C', [('G', 3)])  # C has one OR option
graph.add_node('D', [])
graph.add_node('E', [])
graph.add_node('F', [])
graph.add_node('G', [])

cost, path = graph.ao_star('A')
print("Optimal Cost:", cost)
print("Optimal Path:", path)
