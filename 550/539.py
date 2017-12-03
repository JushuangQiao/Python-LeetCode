class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        ret = 100000
        length = len(t)
        for i in range(length - 1):
            poor = t[i+1] - t[i]
            if poor < ret:
                ret = poor
        last = t[-1] - t[0] if t[-1]-t[0] <= 720 else 1440 - (t[-1]-t[0])
        ret = last if last < ret else ret
        return ret
