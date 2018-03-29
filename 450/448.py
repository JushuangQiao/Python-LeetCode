class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            t = abs(n) - 1
            nums[t] = -abs(nums[t])
        return [k + 1 for k, v in enumerate(nums) if v > 0]

