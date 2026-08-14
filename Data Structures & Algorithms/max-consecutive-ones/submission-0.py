class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
            else:
                result = max(result,current_max)
                current_max = 0
        return max(result,current_max)
        