class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # mn = 1
        # for i in nums:
        #     if i>0 and mn not in nums:
        #         return mn
        #     elif(i>0):
        #         mn += 1
        # return mn
       
        # nums = set(nums)
        # x = 1
        # while x in nums:
        #     x+=1
        # return x

        num_set = set(nums)
        for i in range(1, len(nums) + 2): 
            if i not in num_set:
                return i