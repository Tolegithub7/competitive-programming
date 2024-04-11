class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums

        # holder, seeker, length = 0, 0, len(nums)
        # while seeker<length:
        #     if nums[seeker] != 0:
        #         nums[holder], nums[seeker] = nums[seeker], nums[holder]
        #         holder += 1
        #     seeker += 1
        # return nums 
        