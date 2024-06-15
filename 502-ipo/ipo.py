import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_profit_heap = []
        current_capital = w
        project_index = 0
        
        for _ in range(k):
            while project_index < len(projects) and projects[project_index][0] <= current_capital:
                heapq.heappush(max_profit_heap, -projects[project_index][1])
                project_index += 1
            if not max_profit_heap:
                break
            current_capital += -heapq.heappop(max_profit_heap)
        
        return current_capital