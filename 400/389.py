class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chars = dict()
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        ret = list()
        for c in t:
            if chars.get(c):
                chars[c] -= 1
            else:
                ret.append(c)
        return ''.join(ret)
