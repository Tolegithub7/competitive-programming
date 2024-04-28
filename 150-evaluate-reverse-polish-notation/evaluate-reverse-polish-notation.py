class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expressions = set(["+", "-", "*", "/"])

        for element in tokens:
            if element not in expressions:
                stack.append(int(element))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if element == "+":
                    stack.append(num1 + num2)
                elif element == "-":
                    stack.append(num1 - num2)
                elif element == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))

        return stack.pop()