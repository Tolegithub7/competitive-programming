class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        lst = []
        for i in range(n):
            lst.append([])
            for j in range(n):
                if  image[i][n-j-1] == 0:
                    lst[i].append(1)
                else:
                    lst[i].append(0)
        return lst