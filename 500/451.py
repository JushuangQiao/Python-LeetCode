class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        return ''.join([i[0]*i[1] for i in c.most_common()])
