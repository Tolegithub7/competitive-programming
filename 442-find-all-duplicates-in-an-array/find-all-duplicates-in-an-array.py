class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash = {}
        lst = []
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        for k, v in hash.items():
            if v > 1:
                lst.append(k)
        return lst