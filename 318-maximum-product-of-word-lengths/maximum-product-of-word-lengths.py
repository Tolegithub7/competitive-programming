class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mp = 0
        char_set = []
        
        for i in range(len(words)):
            char_set.append(set(words[i]))
                                                          
        for i in range(len(words)):

            for j in range(i+1,len(words)):
                if not (char_set[i] & char_set[j]):
                    
                    if mp<(len(words[i])*len(words[j])):
                        mp=len(words[i])*len(words[j])

        return mp