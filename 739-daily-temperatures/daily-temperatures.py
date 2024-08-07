class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                ans[stack.pop()] = i - stack[-1]
            stack.append(i)
        return ans