class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        i = 0

        for c in order:
            dic[c] = i
            i += 1

        result = True
        last_seen = None

        for word in words:
            c = word[0]
            if last_seen is None or dic[c] > last_seen:
                last_seen = dic[c]
            else:
                return False

        return result
