class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0

        for i in range(0, len(nums)):
            num = nums[i]
            if num != 0:
                nums[position], nums[i] = nums[i], nums[position]
                position += 1


        
