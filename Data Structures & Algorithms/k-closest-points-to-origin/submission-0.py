class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSort(points)[:k]

    def quickSort(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 1:
            return points
        pivot = points[len(points) - 1]
        pivotDistance = math.sqrt((pivot[0] - 0) ** 2 + (pivot[1] - 0) ** 2)

        j = 0

        for i in range(len(points) - 1):
            currentDistance = math.sqrt((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2)
            if currentDistance < pivotDistance:
                temp = points[j]
                points[j] = points[i]
                points[i] = temp
                j += 1

        temp = points[j]
        points[j] = pivot
        points[len(points) - 1] = temp

        left = self.quickSort(points[:j])
        right = self.quickSort(points[j + 1 :])
        return left + [pivot] + right
