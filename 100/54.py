class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix[0]) == 0:
            return []
        ret = []
        start, m, n = 0, len(matrix), len(matrix[0])
        while start * 2 < m and start * 2 < n:
            col = row = start
            # left -> right
            while col < n - start:
                ret.append(matrix[row][col])
                col += 1
            # top -> bottom
            if m - 2 * start > 1 and row < m - start:
                row += 1
                col -= 1
                while row < m - start:
                    ret.append(matrix[row][col])
                    row += 1
            # right -> left
            if m - 2 * start > 1 and n - 2 * start > 1 and col >= start:
                col -= 1
                row -= 1
                while col >= start:
                    ret.append(matrix[row][col])
                    col -= 1
            # bottom -> top
            if m - 2 * start > 1 and n - 2 * start > 1 and row > start:
                row -= 1
                col += 1
                while row > start:
                    ret.append(matrix[row][col])
                    row -= 1
            start += 1
        return ret