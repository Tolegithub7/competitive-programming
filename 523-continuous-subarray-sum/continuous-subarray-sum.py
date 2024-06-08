class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_sum = {0: -1}
        curr_sum = 0

        for i in range(n):
            curr_sum += nums[i]

            if k != 0:
                curr_sum %= k

            if curr_sum in prefix_sum:
                if i - prefix_sum[curr_sum] > 1:
                    return True
            else:
                prefix_sum[curr_sum] = i

        return False

        # n = len(nums)
        # prefix_sum = [0] * (n + 1)
        
        # for i in range(1, n + 1):
        #     prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        # for l in range(n):
        #     for r in range(l + 1, n + 1):
        #         sm = prefix_sum[r] - prefix_sum[l]
        #         if sm % k == 0 and r - l > 1:
        #             return True
        # return False


        # n = len(nums)
        # for l in range(n-1):
        #     r = l+1
        #     while r<n:
        #         sm = sum(nums[l:r+1])
        #         if sm%k == 0: return True
        #         r += 1
        # return False
