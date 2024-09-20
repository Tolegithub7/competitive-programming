class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev, n, rev1 ,i = '',len(s), '',  0
        for j in range(n):
            rev += s[n-j-1]

        for j in range(n-1,-1,-1):
            if s[i] == s[j]:
                i += 1
        if i == n:
            return s
        string = s[i:n]
        for j in range(len(string)):
            rev1 += string[len(string)-j-1]

        return rev1 + Solution.shortestPalindrome(self, s[0:i]) + s[i:]
            