class Solution:
    def findCenter(self, ed: List[List[int]]) -> int:
        for i in range(len(ed)):
            if ed[i][0] == ed[i+1][0] or ed[i][0] == ed[i+1][1]:
                return ed[i][0]
            else:
                return ed[i][1]   