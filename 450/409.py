class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict = {}
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        ret, remain = 0, 0
        for k in sdict.keys():
            if sdict[k] % 2 == 0:
                ret += sdict[k]
            else:
                ret += (sdict[k] - 1)
                remain = 1
        return ret + remain
