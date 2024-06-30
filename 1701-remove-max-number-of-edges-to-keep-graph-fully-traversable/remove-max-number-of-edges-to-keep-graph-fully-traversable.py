class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.cnt = n
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union_(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += 1
        else:
            self.parent[root1] = root2
            self.size[root2] += 1
        
        self.cnt -= 1

class Solution:
    def helper(self, edges, uf, cnt_edge):
        for _, u, v in edges:
            if uf.find(u) == uf.find(v):
                continue
            uf.union_(u, v)
            cnt_edge[0] += 1
        return

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        common_edges = [edge for edge in edges if edge[0] == 3]
        alice_edges = [edge for edge in edges if edge[0] == 1]
        bob_edges = [edge for edge in edges if edge[0] == 2]
        cnt_edge = [0]

        self.helper(common_edges, uf, cnt_edge)
        
        uf_a = copy.deepcopy(uf)
        uf_b = copy.deepcopy(uf)

        self.helper(alice_edges, uf_a, cnt_edge)
        self.helper(bob_edges, uf_b, cnt_edge)
        return len(edges) - cnt_edge[0] if uf_a.cnt == 1 and uf_b.cnt == 1 else -1