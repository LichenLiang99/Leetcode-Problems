class Solution:
    def findSubstring(self, str1: str, words: List[str]) -> List[int]:
        result = []
        wordBag = collections.Counter(words)
        wordCount = len(words)
        wordLength = len(words[0])
        totalLength = wordCount * wordLength

        for i in range(len(str1) - totalLength + 1):   
            seen = collections.defaultdict(int)

            for j in range(i, i + totalLength, wordLength):
                word = str1[j: j + wordLength]
                if word in wordBag:
                    seen[word] += 1

                    if seen[word] > wordBag[word]:
                        break

                else:
                    break

            if seen == wordBag:
                result.append(i)

        return result