class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, tmp = 0, 0
        pre = float('-inf')
        for n in nums:
            if n > pre:
                tmp += 1
            else:
                ret = max(ret, tmp)
                tmp = 1
            pre = n
        return max(ret, tmp)
