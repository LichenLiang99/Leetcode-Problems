class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # wordList = set(wordList)
        # queue = collections.deque([[beginWord, 1]])
        # while queue:
        #     word, length = queue.popleft()
        #     if word == endWord:
        #         return length
        #     for i in range(len(word)):
        #         for c in 'abcdefghijklmnopqrstuvwxyz':
        #             next_word = word[:i] + c + word[i+1:]
        #             if next_word in wordList:
        #                 wordList.remove(next_word)
        #                 queue.append([next_word, length + 1])
        # return 0
        
        if endWord not in wordList:
            return 0
        
        #to save heighbor[pattern]: [words]
        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)
            res += 1
        
        return 0