class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0] * 3
        for num in nums:
            bucket[num] += 1

        counter = 0
        for i in range(3):
            for j in range(bucket[i]):
                nums[counter] = i
                counter += 1
