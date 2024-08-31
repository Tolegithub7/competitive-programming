# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordList += [beginWord]
#         adj = defaultdict(list)
#         for word in wordList:
#             for i in range(len(word)):
#                 pattern = word[:i] + '#' + word[i + 1: ]
#                 adj[pattern] += [word]
#         queue = [(beginWord, 1)]
#         visited = set()
#         while queue:
#             word, step = queue.pop(0)
#             if word == endWord:
#                 return step
#             visited.add(word)
#             for i in range(len(word)):
#                 pattern = word[:i] + '#' + word[i + 1: ]
#                 for neigh in adj[pattern]:
#                     if neigh not in visited:
#                         queue += [(neigh, step + 1)]

#         return 0
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        bs, es = set([beginWord]), set([endWord])
        visited = set()
        result = 1
        n = len(beginWord)
        while bs and es:
            bs, es = es, bs

            curr = set()
            for u in bs:
                word = list(u)
                for i, ch in enumerate(word):
                    for k in range(26):
                        word[i] = chr(k + ord("a"))
                        target = "".join(word)

                        if target in es:
                            return result + 1

                        if target not in visited and target in word_set:
                            curr.add(target)
                            visited.add(target)
                    word[i] = ch
            bs = curr
            result += 1
        return 0