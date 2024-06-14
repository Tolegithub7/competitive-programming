class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        x0, M=min(nums), max(nums)
        n=len(nums)
        freq=[0]*(M+n)
        for x in nums:
            freq[x]+=1
        cnt, inc=0, 0
        x=x0
        for x in range(x0, n+M):
            f=freq[x]
            cnt+=(f!=0)
            if f<=1: continue
            freq[x+1]+=(f-1)
            inc+=(f-1)
            if cnt>=n-1: break
        return inc