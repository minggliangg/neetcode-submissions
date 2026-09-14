# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        pivot = pairs[len(pairs) - 1]
        j = 0
        for i in range(0, len(pairs) - 1):
            if pairs[i].key < pivot.key:
                temp = pairs[j]
                pairs[j] = pairs[i]
                pairs[i] = temp
                j+=1
        temp = pairs[j]
        pairs[j] = pivot
        pairs[len(pairs) - 1] = temp
        left = self.quickSort(pairs[:j])
        right = self.quickSort(pairs[j+1:])
        left.append(pivot)
        left.extend(right)
        return left
