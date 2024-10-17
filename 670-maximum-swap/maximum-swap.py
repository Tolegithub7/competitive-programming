class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)

        for i in range(n):
            maxindex = i
            for j in range(n-1, i, -1):
                if int(num[j]) > int(num[maxindex]):
                    maxindex = j
                
            if maxindex != i:
                num[i], num[maxindex] = num[maxindex], num[i]
                break
        
        return int("".join(num))