class Solution:
    def maxDistance(self, P: List[int], balls: int) -> int:
        P.sort()

        def count(d):
            n = 1
            x = P[0]
            for y in P:
                if y - x > d:
                    x = y
                    n += 1
            return n

        return bisect_left(range(P[-1] - P[0]), True, key=lambda d: count(d) < balls)