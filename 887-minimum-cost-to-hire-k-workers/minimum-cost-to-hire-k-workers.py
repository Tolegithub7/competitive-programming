class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float("inf")

        pairs = [] # (ratio,quality)

        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))
        
        pairs.sort(key=lambda p:p[0])

        maxHeap = [] #Qualities
        total_quality = 0

        for ratio , q in pairs:
            heapq.heappush(maxHeap,-q)
            total_quality += q

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)

            if len(maxHeap) == k:
                res = min(res, total_quality*ratio)
        return res        