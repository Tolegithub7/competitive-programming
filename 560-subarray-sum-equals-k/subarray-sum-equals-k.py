class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if i==j and nums[i] == k:
        #             count += 1
        #         if j > i:
        #             target = sum(nums[i:j+1])
        #             if target == k:
        #                 count += 1
        #             if target > k:
        #                 continue
        # return count

        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }
        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res