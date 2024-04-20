class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == tot - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1