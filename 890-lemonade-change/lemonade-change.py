class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10 = 0, 0
        n = len(bills)
        for i in range(n):
            if (bills[i] == 5):
                c5 += 1
            elif (bills[i] == 10):
                c10 += 1
                if c5 >= 1:
                    c5 -= 1
                else: return False
            elif (bills[i] == 20):
                if c5>= 1 and c10 >=1:
                    c5 -= 1
                    c10 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else: return False
        return True