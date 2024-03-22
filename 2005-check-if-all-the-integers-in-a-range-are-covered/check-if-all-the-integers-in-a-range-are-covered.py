class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lis = set()
        for i, j in ranges:
            lis.update(range(i, j + 1))
        for num in range(left, right + 1):
            if num not in lis:
                return False
        return True