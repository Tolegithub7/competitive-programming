class Solution:
    def maximumSwap(self, num: int) -> int:
        # lists = list(str(num))
        # last = {int(d): i for i, d in enumerate(lists)}
        # for i, digit in enumerate(lists):
        #     for d in range(9, int(digit), -1):
        #         if last.get(d, -1) > i:
        #             lists[i], lists[last[d]] = lists[last[d]], lists[i]
        #             return int(''.join(lists))
        # return num

        ans = list(str(num))
        n = len(ans)
        highest = -1
        swapL = -1
        swapR = -1
        for i in range(n-1,-1,-1):
            digit = ans[i]
            if highest == -1 or digit > ans[highest]:
                highest = i
            elif digit < ans[highest]:
                swapL = i
                swapR = highest
        if swapR != -1 and swapL != -1:
            ans[swapR],ans[swapL] = ans[swapL],ans[swapR]

        return int(''.join(ans))