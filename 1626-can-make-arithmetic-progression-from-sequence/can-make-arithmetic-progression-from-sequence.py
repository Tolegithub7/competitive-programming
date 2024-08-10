class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr=sorted(arr)
        dfr=arr[1]-arr[0]
        for i in range(2,len(arr)):
            if(arr[i]-arr[i-1]!=dfr):
                return False
        return True