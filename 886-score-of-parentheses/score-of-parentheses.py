class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack = []
        # count = 0
        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     else:
        #         if stack and i == ")":
        #             stack.pop()
        #             count += 1
        # return count

        
        stack = [0]
        total = 0

        for ch in s:
            if ch == "(":
                stack.append(0)

            else:
                top = stack.pop()
                val = max(1,2*top)

                stack[-1] += val

        return stack.pop()