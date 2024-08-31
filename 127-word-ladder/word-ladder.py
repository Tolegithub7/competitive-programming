class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList += [beginWord]
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '#' + word[i + 1: ]
                adj[pattern] += [word]
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            word, step = queue.pop(0)
            if word == endWord:
                return step
            visited.add(word)
            for i in range(len(word)):
                pattern = word[:i] + '#' + word[i + 1: ]
                for neigh in adj[pattern]:
                    if neigh not in visited:
                        queue += [(neigh, step + 1)]

        return 0