class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = {}
        for m in magazine:
            chars[m] = chars.get(m, 0) + 1
        for r in ransomNote:
            if chars.get(r, -1) > 0:
                chars[r] -= 1
            else:
                return False
        return True
