class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in nums[i+1:]:
                second_index = nums[i+1:].index(to_find) + i+1
                return [i,second_index]


        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        