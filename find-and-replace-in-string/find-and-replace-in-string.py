class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, source, t in sorted(zip(indices, sources, targets), reverse = True):
            if source == s[i:i+len(source)]:
                s = s[:i] + t + s[i+len(source):]

        return s