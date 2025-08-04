class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # interate through jewels and count result starting from 0
        # Best solution
        result = 0
        for x in stones:
            if x in jewels:
                result += 1
        return result

sol = Solution()
print(sol.numJewelsInStones("aA","aAAbbbb"))