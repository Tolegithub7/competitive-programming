class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # start_time = customers[0][0]
        # n = len(customers)
        # waitTime = 0
        # for i in range(n):
        #     if start_time < customers[i][0]:
        #         start_time = customers[i][0] + customers[i][1]
        #         waitTime += customers[i][1]
        #     else:
        #         start_time = start_time + customers[i][1]
        #         waitTime += ( start_time - customers[i][0] )
        # return waitTime/n

        
        finish_time = -maxsize
        total_wait_time = 0

        for time, duration in customers:
            if time < finish_time:
                total_wait_time += finish_time - time + duration
                finish_time += duration
            else:
                total_wait_time += duration
                finish_time = time + duration

        return total_wait_time / len(customers)


        