class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
        #     if i == (len(arr) - 1):
        #         arr[i] = -1
        #     else:
        #         arr[i] = max(arr[i + 1 :])
        # return arr

        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max,arr[i])
            arr[i]= right_max
            right_max = new_max

            
        return arr
