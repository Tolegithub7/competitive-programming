class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        while start <= end:
            mid = (start + end)//2
            sqr = mid*mid
            if sqr == x :
                return mid
            if sqr < x:
                start = mid + 1
                answer = mid
            else:
                end = mid - 1
        return answer