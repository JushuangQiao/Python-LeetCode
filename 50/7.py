class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        t = abs(x)
        while t:
            ret = 10 * ret + t % 10
            t /= 10
        if ret > 2 ** 31 or -ret < -2 ** 31:
            return 0
        return ret if x >= 0 else -ret
