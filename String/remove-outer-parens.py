class Solution:
    def removeOuterParentheses(self, S):
        result = []
        opened = 0
        for i in S:
            if i == '(' and opened > 0:
                result.append(i)

            if i == ')' and opened > 1:
                result.append(i)

            if i == '(':
                opened += 1
            if i == ')':
                opened -= 1


        return "".join(result)

          
