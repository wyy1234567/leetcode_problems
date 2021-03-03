# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return node 
    mapping = {node: Node(node.val)}
    deque = collections.deque([node])
    while deque:
        curr = deque.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in mapping:
                deque.append(neighbor)
                mapping[neighbor] = Node(neighbor.val)
            mapping[curr].neighbors.append(mapping[neighbor])
    return mapping[node]
