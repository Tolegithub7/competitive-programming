class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            max_index = 0
            for j in range(1, i):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[:max_index+1] = reversed(arr[:max_index+1])
            result.append(max_index+1)
            arr[:i] = reversed(arr[:i])
            result.append(i)
        return result