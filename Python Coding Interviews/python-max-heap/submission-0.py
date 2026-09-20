import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = [-i for i in nums]
    heapq.heapify(heap)
    return [-heapq.heappop(heap) for _ in range(len(heap))]

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
