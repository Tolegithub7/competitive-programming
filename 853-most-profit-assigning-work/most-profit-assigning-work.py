class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res, j, best, temp = 0, 0, 0, []
        
        for i in range(len(worker)):
            temp.append((difficulty[i], profit[i]))
        
        temp.sort()
        worker.sort()
        
        for work in worker:
            while j < len(temp) and work >= temp[j][0]:
                best = max(best, temp[j][1])
                j += 1
            
            res += best
        
        return res