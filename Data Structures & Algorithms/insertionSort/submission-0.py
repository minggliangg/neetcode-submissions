# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# class Solution:
#     def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
#         results = [pairs.copy()]
#         for i in range(len(pairs) - 1):
#             j = i + 1
#             for j in range(j, 1, -1):
#                 if pairs[j].key > pairs[j-1].key:
#                     break
#                 if pairs[j].key < pairs[j-1].key:
#                     temp = pairs[j-1]
#                     pairs[j-1] = pairs[j]
#                     pairs[j] = temp
#                     results.append(pairs.copy())
#                 j -= 1
#         return results

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        results = []

        for i in range(len(pairs)):
            j = i

            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]
                j -= 1

            # Save exactly one state per insertion
            results.append(pairs.copy())

        return results