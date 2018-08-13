# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.memo = {None: None}

    def cloneGraph(self, head):
        if head in self.memo:
            return self.memo[head]
        clone_node = UndirectedGraphNode(head.label)
        self.memo[head] = clone_node
        for neighbor in head.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))
        return clone_node
