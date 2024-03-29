class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # n = len(nums)
        # l = 0
        # r = n-1
        # counter = 0
        # while l<r:
        #     if nums[l] + nums[r] == k:
        #         counter += 1
        #         l += 1
        #         r -= 1
        #     elif nums[l] + nums[r] < k:
        #         l += 1
        #     else:
        #         r -= 1
        # return counter
        nums.sort()
        count, lt, rt = 0, 0, len(nums)-1
        while lt<rt:
            if nums[lt]+nums[rt] == k:
                count += 1
                lt += 1
                rt -= 1
            elif nums[lt]+nums[rt] > k:
                rt -= 1
            else:
                lt += 1
        return count
