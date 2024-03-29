class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = ans = 0
        cur = 1
        if (k <= 1):
            return 0
        for r in range(len(nums)):
            cur *= nums[r]
            while (cur >= k and l<len(nums)):
                cur //= nums[l]
                l += 1
            ans += (r - l +1)
        return ans