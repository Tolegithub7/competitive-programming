class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_avg = float("-inf")
        # l = cur = 0
        # for r in range(len(nums)):
        #     cur += nums[r]
        #     if (r-l+1) == k:
        #         max_avg = max(max_avg, cur/k)
        #         cur -= nums[l]
        #         l += 1
        # return max_avg
       
        # l = 1
        # average_window = sum(nums[:k])/k
        # max_window = average_window
        # for idx in range(k, len(nums)):
        #     new_average = (sum(nums[l: idx+1]))/k
        #     max_window = max(max_window, new_average)
        #     l += 1
        # return max_window

        window_sum = sum(nums[:k])
        max_sum = window_sum/k
        for idx in range(k, len(nums)):
            window_sum += nums[idx]
            window_sum -= nums[idx-k]
            new_average = window_sum/k
            max_sum = max(max_sum, new_average)
        return max_sum