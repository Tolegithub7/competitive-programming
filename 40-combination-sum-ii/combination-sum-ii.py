class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        ss = set()
        c.sort()
        n = len(c)
        def gen(s,l,i):
            if s>target:
                return
            if s==target:
                ss.add(tuple(sorted(l)))
                return
            else:
                for x in range(i,n):
                    if x>i and c[x]==c[x-1]:
                        continue
                    gen(s+c[x],l+[c[x]],x+1)
        gen(0,[],0)
        return ss