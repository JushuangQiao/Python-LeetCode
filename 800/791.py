class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_hash = {}
        t_hash = {}
        for c in T:
            t_hash[c] = t_hash.get(c, 0) + 1
        ret = []
        for c in S:
            if t_hash.get(c):
                ret.append(c * t_hash.get(c))
                del t_hash[c]
        for k in t_hash.keys():
            ret.append(k * t_hash[k])
        return ''.join(ret)