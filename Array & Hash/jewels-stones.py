class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels_set = set(J)

        for stone in S:
            if stone in jewels_set:
                counter += 1

        return counter
