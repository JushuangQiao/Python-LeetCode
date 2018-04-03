class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                ret.append(abs(n))
            else:
                nums[abs(n) - 1] = -nums[abs(n) - 1]
        return ret
            
