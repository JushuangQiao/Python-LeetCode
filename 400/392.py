class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        loc = 0
        for i in s:
            loc = t.find(i, loc) + 1
            if loc == 0:
                return False
        return True
