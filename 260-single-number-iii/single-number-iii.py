class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash_num = {}
        ans = []
        for num in nums:
            if num in hash_num:
                hash_num[num] += 1
            else:
                hash_num[num] = 1
        for num, count in hash_num.items():
            if count == 1:
                ans.append(num)
        return ans