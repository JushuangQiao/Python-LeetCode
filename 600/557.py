class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda t:t[::-1], s.split(' ')))
