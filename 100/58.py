class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for c in s.strip()[::-1]:
            if c == ' ':
                break
            ret += 1
        return ret