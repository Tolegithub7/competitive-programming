class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        for i in range(1, len(rating)-1):
            less_l, less_r, greater_l, greater_r = 0, 0, 0, 0
            for j in range(i):
                if rating[j] < rating[i]:
                    less_l += 1
                else:
                    greater_l += 1
            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    less_r += 1
                else:
                    greater_r += 1
            total += (less_l * greater_r) + (greater_l * less_r)
        return total