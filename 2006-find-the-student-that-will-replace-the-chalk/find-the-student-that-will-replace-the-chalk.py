class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ps = [0]
        for c in chalk:
            ps.append(ps[-1] + c)

        k %= ps[-1]
        l, r = 0, len(chalk) - 1
        while l <= r:
            m = (l + r) >> 1
            if ps[m + 1] > k:
                r = m - 1
            else:
                l = m + 1
        return l