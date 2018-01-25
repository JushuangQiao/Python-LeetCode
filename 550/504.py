class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        ret = ''
        n = abs(num)
        while n:
            ret += str(n % 7)
            n = n / 7
        return '-' + ret[::-1] if num < 0 else ret[::-1]
