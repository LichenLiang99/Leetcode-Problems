class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())

        count = collections.Counter(words)
        print(count)
        for w in banned:
            del count[w]
        print(count)
        return max(count, key = count.get)