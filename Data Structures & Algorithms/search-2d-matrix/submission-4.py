class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs = 0
        re = len(matrix) - 1

        while rs <= re:
            rm = rs + (re - rs) // 2

            if target < matrix[rm][0]:
                re = rm - 1
            elif target > matrix[rm][-1]:
                rs = rm + 1
            else:
                return self.rowHelper(matrix[rm], target)

        return False

    def rowHelper(self, array: List[int], target: int) -> bool:
        s = 0
        e = len(array) - 1

        while s <= e:
            m = s + (e - s) // 2

            if target > array[m]:
                s = m + 1
            elif target < array[m]:
                e = m - 1
            else:
                return True

        return False