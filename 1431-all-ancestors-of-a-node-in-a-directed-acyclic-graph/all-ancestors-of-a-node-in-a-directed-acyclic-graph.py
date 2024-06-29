class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        direct_child = defaultdict(list)
        ans = [[] for _ in range(n)]
        for x, y in edges:
            direct_child[x].append(y)
    
        def dfs(x, curr):
            for ch in direct_child[curr]:
                if ans[ch] and ans[ch][-1] == x: continue
                ans[ch].append(x)
                dfs(x, ch) 
    
        for i in range(n): dfs(i, i)
        return ans