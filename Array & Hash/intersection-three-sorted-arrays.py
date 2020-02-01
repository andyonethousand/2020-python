class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        combined_values = arr1 + arr2 + arr3

        return ([key for key, val in (collections.Counter(combined_values)).items() if val == 3])
