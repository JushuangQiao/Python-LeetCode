class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = sum(nums)
        left = 0
        for k, v in enumerate(nums):
            if left * 2 + v == ret:
                return k
            left += v
        return -1

