class Solution:
    def maximumSwap(self, num: int) -> int:
        lists = list(str(num))
        last = {int(d): i for i, d in enumerate(lists)}
        for i, digit in enumerate(lists):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    lists[i], lists[last[d]] = lists[last[d]], lists[i]
                    return int(''.join(lists))
        return num