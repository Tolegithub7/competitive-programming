class Solution:
    def generate(self, r: int) -> List[List[int]]:
        result = [[1]]
        for i in range(r - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1])+1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result