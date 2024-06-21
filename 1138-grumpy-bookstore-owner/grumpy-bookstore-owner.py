class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        window = 0
        for i in range(minutes):
            window += customers[i]*grumpy[i]
        maxwindow = window
        for i in range(minutes,n):
            window = window+(customers[i]*grumpy[i])-(customers[i-minutes]*grumpy[i-minutes])
            maxwindow = max(window,maxwindow)
        for i in range(n):
            maxwindow += customers[i]*(1-grumpy[i])

        return maxwindow