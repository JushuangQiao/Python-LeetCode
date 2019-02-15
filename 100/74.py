class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        while rows > 0:
            if matrix[rows - 1][0] < target:
                return self.bin_search(matrix[rows - 1], target)
            elif matrix[rows - 1][0] == target:
                return True
            else:
                rows -= 1
        return False

    def bin_search(self, data, target):
        """
        :type data: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(data)
        while low < high:
            mid = low + (high - low) / 2
            if data[mid] == target:
                return True
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid
        return False
