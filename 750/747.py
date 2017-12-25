class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        a, b = [nums[0], 0], [nums[1], 1]
        if b[0] > a[0]:
            a, b = b, a
        for k, v in enumerate(nums):
            if k < 2:
                continue
            if b[0] < v < a[0]:
                b = [v, k]
            elif v >= a[0]:
                a, b = [v, k], a
            else:
                pass
        return a[1] if a[0] >= b[0] * 2 else -1

