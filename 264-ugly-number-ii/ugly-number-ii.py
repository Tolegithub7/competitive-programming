class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = 0
        heap = [1]
        while n > 0:
            while heap[0] == num:
                heapq.heappop(heap)
            
            num = heapq.heappop(heap)
            n -= 1
            
            heapq.heappush(heap, num*2)
            heapq.heappush(heap, num*3)
            heapq.heappush(heap, num*5)
            
        return num