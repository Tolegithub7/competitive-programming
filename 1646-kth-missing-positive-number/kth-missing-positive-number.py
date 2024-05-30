class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        stack = []
        for i in range(1, arr[-1]+1):
            if i not in arr:
                stack.append(i)
        print(stack)
        if len(stack) >= k: return stack[k-1]
        else: return (arr[-1] + k - len(stack))