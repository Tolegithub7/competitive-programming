class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        window = []
        for num in nums:
            insort(window, num)
            if window[-1] - window[0] > limit:
                window.pop(bisect_left(window, nums[i]))
                i += 1
        return len(window)