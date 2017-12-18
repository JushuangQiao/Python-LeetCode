class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = ret = 0
        cur = None
        while left < len(nums):
            if nums[left] != cur:
                nums[ret] = nums[left]
                ret += 1
                cur = nums[left]
            left += 1
        return ret

