# from typing import List
# from heapq import heappush, heappop
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap=[]
        for i in range(len(arr)):
            for j in range(len(arr)-1,i,-1):
                if len(heap)<k:
                    heapq.heappush(heap,[-(arr[i]/arr[j]),arr[i],arr[j]])
                elif (arr[i]/arr[j])<-heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,[-(arr[i]/arr[j]),arr[i],arr[j]])
                else:
                    break
        return [heap[0][1],heap[0][2]]
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         n = len(arr)
#         heap = []
#         for i in range(n):
#             for j in range(i + 1, n):
#                 fraction = (arr[i], arr[j])
#                 heappush(heap, (arr[i] / arr[j], fraction))
#         for _ in range(k):
#             fra = heappop(heap)[1]
#         return list(fra)
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