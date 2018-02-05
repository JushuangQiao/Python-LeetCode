class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        s = int(sqrt(area))
        while area % s != 0:
            s -= 1
        return [area/ s, s]
