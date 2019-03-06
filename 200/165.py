class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        k1, k2 = 0, 0
        while k1 < len(v1) and k2 < len(v2):
            if int(v1[k1]) > int(v2[k2]):
                return 1
            if int(v1[k1]) < int(v2[k2]):
                return -1
            k1 += 1
            k2 += 1
        while k1 < len(v1):
            if int(v1[k1]):
                return 1
            k1 += 1
        while k2 < len(v2):
            if int(v2[k2]):
                return -1
            k2 += 1
        return 0