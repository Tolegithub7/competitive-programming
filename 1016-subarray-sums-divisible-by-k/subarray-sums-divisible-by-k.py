class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = [0] * (len(nums) + 1)
        remainders = [0] * k
        remainders[0] = 1  # Include the single element subarray with sum divisible by k
        
        for i in range(1, len(nums) + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
            remainder = prefix_sums[i] % k
            count += remainders[remainder]
            remainders[remainder] += 1
        
        return count