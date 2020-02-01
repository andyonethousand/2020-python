class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        intersetc = set()

        for i in nums1:
            intersetc.add(i)

        for i in nums2:
            if i in intersetc and i not in result:
                result.append(i)

        return result
