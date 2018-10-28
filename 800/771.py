class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_hash = {c: True for c in J}
        ret = 0
        for c in S:
            if j_hash.get(c):
                ret += 1
        return ret
