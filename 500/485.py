class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = tmp = 0
        for n in nums:
            if n:
                tmp += 1
            else:
                ret = max(tmp, ret)
                tmp = 0
        return max(ret, tmp)
