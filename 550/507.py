class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        from math import sqrt
        if num <= 3:
            return False
        tsum, end = 1, int(sqrt(num)) + 1
        for n in range(2, end):
            if num % n == 0:
                tsum += n + int(num / n)
            if tsum > num:
                return False
        return tsum == num
