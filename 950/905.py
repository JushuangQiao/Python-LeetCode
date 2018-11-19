class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start, end = 0, len(A) - 1
        while start <= end:
            if A[start] % 2 and not A[end] % 2:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            elif A[start] % 2 and A[end] % 2:
                end -= 1
            elif not A[start] % 2 and not A[end] % 2:
                start += 1
            else:
                start += 1
                end -= 1
        return A
