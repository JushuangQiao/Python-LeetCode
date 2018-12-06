class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd, length = 0, 1, len(A)
        while odd < length and even < length:
            if A[even] % 2 != 0 and A[odd] % 2 == 0:
                A[even], A[odd] = A[odd], A[even]
                odd += 2
                even += 2
            elif A[even] % 2 != 0 and A[odd] % 2 != 0:
                odd += 2
            elif A[even] % 2 == 0 and A[odd] % 2 == 0:
                even += 2
            else:
                odd += 2
                even += 2
        return A