class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            left = bisect_left(nums, target)
            right = bisect_right(nums, target) - 1

            if left<len(nums) and nums[left] == target and nums[right] == target: return [left, right]
        return [-1, -1]
        
        # n = len(nums)    
        # return [-1,-1] if target not in nums else [nums.index(target), n-1 - nums[::-1].index(target)]