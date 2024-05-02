class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # encounteredVals = {}
        # max_ = -1
        # for element in nums:
        #     if -element in encounteredVals and abs(element) > max_:
        #         max_ = abs(element)
        #     else:
        #         encounteredVals[element] = 0
        # return max_

        st = set(nums)
        mx = -1
        for elt in nums:
            if elt>0 and -elt in st:
                mx = max(elt, mx)
        return mx
