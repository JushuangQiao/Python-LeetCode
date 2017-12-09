class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            ts = ''.join(sorted(s))
            if ret.get(ts):
                ret[ts].append(s)
            else:
                ret[ts] = [s]
        return ret.values()

