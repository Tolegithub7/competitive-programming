class Solution:
    def getRow(self, r: int) -> List[int]:
        if r == 0:
            return [1]
        arr = self.getRow(r-1)
        res = [1]
        for i in range(len(arr)-1):
            res.append(arr[i] + arr[i+1])
        res.append(1)
        return res