class Solution:
    def minProcessingTime(self, A: List[int], T: List[int]) -> int:
        A.sort(reverse=True)
        T.sort()
        N = len(T)
        ans = 0
        for i in range(N):
            ans = max(ans, T[i]+A[i//4])
        return ans