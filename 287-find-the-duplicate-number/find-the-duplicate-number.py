class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {} 
        for i in nums:
            if i in hash:
                return i
            else:
                hash[i] = 1