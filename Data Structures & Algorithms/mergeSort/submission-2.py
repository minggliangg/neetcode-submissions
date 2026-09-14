# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
  def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
    if len(pairs) == 1 or len(pairs) == 0:
      return pairs

    middle = len(pairs) // 2
    left = self.mergeSort(pairs[:middle])
    right = self.mergeSort(pairs[middle:])

    left_pointer = right_pointer = 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
      if left[left_pointer].key < right[right_pointer].key:
        result.append(left[left_pointer])
        left_pointer += 1
      elif left[left_pointer].key > right[right_pointer].key:
        result.append(right[right_pointer])
        right_pointer += 1
      else:
        result.append(left[left_pointer])
        left_pointer += 1
        result.append(right[right_pointer])
        right_pointer += 1

    remaining = left[left_pointer:] + right[right_pointer:]
    result.extend(remaining)
    return result
