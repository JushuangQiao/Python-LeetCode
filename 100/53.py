class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_val, cur_sum = nums[0], float('-inf')
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_val = max(max_val, cur_sum)
        return max_val
