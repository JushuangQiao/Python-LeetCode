class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length, mv = len(bits), 0
        while mv < length - 1:
            mv += (1 + bits[mv])
        return mv <= length - 1