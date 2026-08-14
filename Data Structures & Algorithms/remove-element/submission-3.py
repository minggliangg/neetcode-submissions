class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]== val:
        #         nums[i] = None
        # return len(nums)
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] =nums [i]
                k+=1
        return k