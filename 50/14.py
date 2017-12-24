class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        pre = strs[0]
        for s in strs:
            len_pre = len(pre)
            while s[0:len_pre] != pre:
                len_pre -= 1
                pre = pre[0:len_pre]
                if not pre:
                    return pre
        return pre
