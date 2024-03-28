class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        dic = defaultdict(int)
        max_len = 0

        for end in range(len(nums)):
            dic[nums[end]] += 1

            while dic[nums[end]] > k:
                dic[nums[start]] -= 1
                start += 1

            max_len = max_len if max_len >= end - start + 1 else end - start + 1

        return (max_len)
