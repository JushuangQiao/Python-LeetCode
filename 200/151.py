class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        return ' '.join(tmp[::-1])