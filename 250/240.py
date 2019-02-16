class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        start = 0
        while rows >= 0 and cols >= start:
            if matrix[rows][start] == target:
                return True
            elif matrix[rows][start] > target:
                rows -= 1
            else:
                start += 1
        return False