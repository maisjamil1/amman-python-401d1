from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        # self.neighbors = []


# [
#     node(val, []),
#     node(val, []),
#     node(val, [])
# ]

# {
#     node1: [],
#     node2: [],
#     ....
# }

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        # self._adjacency_list.push(node)
        self._adjacency_list[node] = []

    def add_edge(self, start_node, end_node, weight=1):
        pass

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        pass

    def size(self):
        pass

    def bfs(self, start_node):
        q = Queue()
        q.enqueue(start_node)
        while len(q):
            cur = q.dequeue()
            # mark the node as visited so you don't enqueue(visit) it again
            print(cur.value)
            neighbors = self._adjacency_list[cur]
            for n in neighbors:
                q.enqueue(n)

    def dfs(self, start_node):
        pass

if __name__ == "__main__":
    g = Graph()
    # print(g._adjacency_list)
    # g.add_node('a')
    # g.add_node('b')
    # g.add_node('c')
    # print(g.get_nodes())

    # Not best practice for testing, but only for bfs
    a = Node('a')
    b = Node('b')
    c = Node('c')
    g._adjacency_list[a] = [b, c]
    g._adjacency_list[b] = [a, c]
    g._adjacency_list[c] = [a, b]
    g.bfs(a)

# {
#     a: [b, c],
#     b: [a, c],
#     c: [a, b]
# }



# Reference: Breadth First Algorithm for Binary Trees
#         3
#     6       7
#    1 9     4 10

# 1. en(root)
#     2. cur = dequeue()
#     3. action (print or add to a list)
#     4. check if left and right
#         5. enqueue them
# 6. check if loop is not empty, repeat 2-5
# 7. if empty return

# queue = []

# [3 6 7 1 9 4 10]
