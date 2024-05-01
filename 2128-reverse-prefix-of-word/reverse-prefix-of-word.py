class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = None
        for i in range(len(word)):
            if word[i] == ch:
                idx = i + 1
                break
        if idx is not None:
            rv =  word[:idx][::-1]
            return rv + word[idx:]
        return word