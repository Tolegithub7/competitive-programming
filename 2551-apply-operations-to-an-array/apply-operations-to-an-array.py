class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*= 2
                nums[i + 1] = 0   
        lst_num = []
        lst_zero = []
        for j in nums:
            if j != 0:
                lst_num.append(j)
            else: 
                lst_zero.append(j) 
        return (lst_num + lst_zero)