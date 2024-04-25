class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        for char in s:

            if char in ')]}':
                if char == ')' and stack and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return  not stack

        # stack = []
        # my_dict = {'(':')', '[':']', '{':'}'}
        # for i in range(len(s)):
        #     if s[i] in my_dict.keys():
        #         stack.append(s[i])
        #     else:
        #         if not stack:
        #             return False
        #         a = stack.pop()
        #         if s[i] != my_dict[a]:
        #             return False
        # return not stack