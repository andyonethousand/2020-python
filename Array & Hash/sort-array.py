class Solution(object):
    def sortArrayByParity(self, A):
        x = sorted(A, key = lambda x: x % 2)
        return x
