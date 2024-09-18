class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        def compare(x, y):
            return int(y + x) - int(x + y)
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))