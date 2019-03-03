class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, carry = 0, 1
        while True:
            cnt = n / 5 ** carry
            if cnt == 0:
                return ret
            ret += cnt
            carry += 1