class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        sorted_set = sorted(list(set(arr)))
        for i in range(len(sorted_set)): 
            dic[sorted_set[i]] = i + 1
        for r in range(len(arr)): 
            arr[r] = dic[arr[r]]
        
        return arr 