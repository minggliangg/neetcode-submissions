from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        left = n - 1
        right = n - 2
        return self.climbStairs(n=left) + self.climbStairs(n=right)
