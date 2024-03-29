class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
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
