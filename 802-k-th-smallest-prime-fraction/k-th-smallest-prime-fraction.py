from typing import List
from heapq import heappush, heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                fraction = (arr[i], arr[j])
                heappush(heap, (arr[i] / arr[j], fraction))
        for _ in range(k):
            fra = heappop(heap)[1]
        return list(fra)
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         n = len(arr)
#         stack = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 frac = arr[i], arr[j]
#                 stack.append((arr[i]/arr[j], frac))
#         stack.sort(key=lambda x:x[0])
#         for _ in range(k):
#             a, b = stack.pop(0)
#         return list(b)