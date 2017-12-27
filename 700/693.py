class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n % 2
        n = n >> 1
        while n:
            t = n % 2
            if t == a:
                return False
            a = t
            n = n >> 1
        return a != n
