class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        for d in range(1, 10):
            if d * 9 * (10 ** (d - 1)) >= n:
                digit = d
                break
        num = 0
        for d in range(1, digit + 1):
            num += int(9 * (d - 1) * 10 ** (d - 2))
        ret = (n - num - 1) / digit + 10 ** (digit-1)
        return int(str(ret)[(n - num - 1) % digit])
