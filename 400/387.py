class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars, index = {}, {}
        for k, v in enumerate(s):
            chars[v] = chars.get(v, 0) + 1
            index[v] = index.get(v) or k
        first = float('inf')
        for c in chars.keys():
            if chars[c] == 1:
                first = min(index[c], first)
        return first if first < float('inf') else -1
            
