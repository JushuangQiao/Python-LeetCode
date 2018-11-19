class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mi = ma = -1
        for a in A:
            mi = min(mi, a) if mi > -1 else a
            ma = max(ma, a) if ma > -1 else a
        return 0 if 2 * K > ma - mi else ma - mi - 2 * K