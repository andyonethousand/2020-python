class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {}

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1

        for i in nums:
            if dict[i] == 1:
                return i
