class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = 0
        while m <= n / 2:
            k = m
            while k < n - 1 - m:
                matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k], matrix[n-1-k][m] = \
                    matrix[n-1-k][m], matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k]
                k += 1
            m += 1
