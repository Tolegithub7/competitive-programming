class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        mx = max(arr)
        peak = arr.index(mx)
        if n<3:
            return False
        if arr[0] == mx or arr[n-1] == mx:
            return False
        for i in range(1, peak+1):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(peak+1, n-1):
            if arr[i+1] >= arr[i]:
                return False
        return True