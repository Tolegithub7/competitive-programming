class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1
            ans = helper(x,n//2)
            ans = ans * ans
            return ans if n%2 == 0 else ans * x
        answer = helper(x, abs(n))
        return answer if n>=0 else 1/answer

        
            
            
        
            