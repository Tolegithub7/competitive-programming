class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #This problem is similar to minimum sum subarray
        #The sub array should have equal remainder as total array
        d={}
        d[0]=-1
        rem=sum(nums)%p
        ps=0
        res=len(nums)
        if rem==0:
            return 0
        for i in range(len(nums)):
            ps+=nums[i]
            current_remainder=ps%p
            target_remainder=(current_remainder-rem+p)%p
            if target_remainder in d:
                res=min(res,i-d[target_remainder])
            d[current_remainder]=i
        return res if res!=len(nums) else -1