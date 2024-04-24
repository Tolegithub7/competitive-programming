class Solution:
    def removeStars(self, s: str) -> str:
        # result = []
        # for i in s:
        #     if i == "*":
        #         result.pop()
        #     else:
        #         result += i
        # return "".join(result)

        stack = []
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
