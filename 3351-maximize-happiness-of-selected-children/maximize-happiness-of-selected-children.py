class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        hap = 0
        for i in range(k):
            if happiness[i]-i>0:
                hap += happiness[i]-i
        return hap
