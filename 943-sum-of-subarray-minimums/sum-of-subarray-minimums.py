# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         MOD = (10 ** 9) + 7
#         n = len(arr)
#         stack = []
#         result = 0
#         prevIndex = -1
#         for i in range(n):
#             while stack and arr[i] < arr[stack[-1]]:
#                 poppedIndex = stack.pop()
#                 width = i - prevIndex - 1
#                 result += arr[poppedIndex] * width
#                 result %= MOD
#             stack.append(i)
    
#         while stack:
#             poppedIndex = stack.pop()
#             width = n - prevIndex - 1
#             result += arr[poppedIndex] * width
#             result %= MOD
#         return result
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #Use DP & Montonic Stack
        arr = [0] + arr
        stack = [0]
        ans = [0] * len(arr)

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i-j)*arr[i]
            stack.append(i)
        
        return sum(ans) % (10**9 + 7)