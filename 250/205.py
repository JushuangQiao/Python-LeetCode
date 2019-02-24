class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False
        if len_s == len_t == 0:
            return True
        maps, mapt = {}, {}
        for a, v in zip(s, t):
            if not maps.get(a):
                maps[a] = v
            if not mapt.get(v):
                mapt[v] = a
            if maps[a] != v or mapt[v] != a:
                return False
        return True