class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashes = {}
        left, right, length = 0, 0, len(s)
        max_len = 0
        while right < length:
            if hashes.get(s[right]) and hashes[s[right]] >= left:
                left = hashes[s[right]]
            hashes[s[right]] = right + 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
