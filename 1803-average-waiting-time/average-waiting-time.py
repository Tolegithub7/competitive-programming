class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start_time = customers[0][0]
        n = len(customers)
        waitTime = 0
        for i in range(n):
            if start_time < customers[i][0]:
                start_time = customers[i][0] + customers[i][1]
                waitTime += customers[i][1]
            else:
                start_time = start_time + customers[i][1]
                waitTime += ( start_time - customers[i][0] )
        return waitTime/n



        