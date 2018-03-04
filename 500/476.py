class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(map(lambda x:'1' if x=='0' else '0', bin(num)[2:])), 2)
