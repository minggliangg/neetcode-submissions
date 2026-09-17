class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb = 1
        ub = max(piles)
    

        while lb < ub:
            m = lb + (ub - lb) // 2
            time_needed = 0

            for b in piles:
                time_needed += math.ceil(b / m)

            if time_needed > h:
                lb = m + 1
            else:
                ub = m

        return lb

