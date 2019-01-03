class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for i in range(n)] for j in range(n)]
        v, start = 1, 0
        while start * 2 < n:
            col = row = start
            # left -> right
            while col < n - start:
                ret[row][col] = v
                col += 1
                v += 1
            # top -> bottom
            if n - 2 * start > 1 and row < n - start:
                row += 1
                col -= 1
                while row < n - start:
                    ret[row][col] = v
                    row += 1
                    v += 1
            # right -> left
            if n - 2 * start > 1 and n - 2 * start > 1 and col >= start:
                col -= 1
                row -= 1
                while col >= start:
                    ret[row][col] = v
                    col -= 1
                    v += 1
            # bottom -> top
            if n - 2 * start > 1 and n - 2 * start > 1 and row > start:
                row -= 1
                col += 1
                while row > start:
                    ret[row][col] = v
                    v += 1
                    row -= 1
            start += 1
        return ret