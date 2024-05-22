class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def best_score_diff(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            score_diff_i = nums[i] - best_score_diff(i + 1, j)
            score_diff_j = nums[j] - best_score_diff(i, j - 1)
            return max(score_diff_i, score_diff_j)
        
        return best_score_diff(0, len(nums) - 1) >= 0


            