class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S[::-1]
        ret = []
        leng = 0
        tmp = []
        for c in s:
            if c != '-':
                if leng == K:
                    ret.append(''.join(tmp))
                    leng = 1
                    tmp = [c.upper()]
                else:
                    tmp.append(c.upper())
                    leng += 1
        ret.append(''.join(tmp))
        return '-'.join(ret)[::-1]
