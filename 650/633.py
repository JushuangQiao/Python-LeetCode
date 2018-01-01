class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        for i in range(int(sqrt(c))+1):
            if (int(sqrt(c-i**2))) ** 2 + i ** 2 == c:
                return True
        return False
