class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(C):
                if target == matrix[r][c]:
                    return True

        return False

        