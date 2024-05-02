class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        encounteredVals = {}
        max_ = -1
        for element in nums:
            if -element in encounteredVals and abs(element) > max_:
                max_ = abs(element)
            else:
                encounteredVals[element] = 0
        return max_