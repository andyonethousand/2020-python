class Solution:
    def isHappy(self, n: int) -> bool:
        set_lookup = set()
        result = 0
        
        while n != 1:
            if n in set_lookup:
                return False
            result = 0
            for i in str(n):
                result += int(i) ** 2
            set_lookup.add(n)
            n = result 

        if n == 1:
            return True
