class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            md = (l+r)//2
            if nums[md] == target: return md
            elif nums[md]>target: r = md-1
            elif nums[md]<target: l = md+1
        return -1
        # l, r = 0, len(nums)-1
        # while l<=r:
        #     md = (l+r)//2
        #     if (nums[md] > target):
        #         r = md - 1
        #     elif (nums[md] < target):
        #         l = md + 1
        #     else:
        #         return md
        # return -1