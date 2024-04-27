class Solution:
    def removeStars(self, s: str) -> str:
        stach = []
        for i in s:
            if i != "*":
                stach.append(i)
            else:
                if stach: stach.pop()
        return "".join(stach)
        # stack = []
        # for i in s:
        #     if i != '*':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        # return "".join(stack)
