class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_n = len(matrix)
        r_c = len(matrix[0])

        left = 0
        right = r_n * r_c - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // r_c
            col = mid % r_c

            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False