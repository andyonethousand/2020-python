class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        L = [0] * length
        R = [0] * length
        answer = [0] * length
        
        #L[i] contains the product of all the elements fo the left
        L[0] = 1
        
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer
