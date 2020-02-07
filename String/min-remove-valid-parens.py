class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        opens = []
        closes = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                opens.append(i)
            if c == ')':
                if len(opens) == 0:
                    closes.append(i)
                else:
                    # remove last item from list
                    opens.pop()

        hashset = set(opens + closes)

        return ''.join(s[i] for i in range(len(s)) if i not in hashset)
