class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        a = b = c = float('-inf')
        for n in nums:
            if n > a:
                b, c, a = a, b, n
            elif a > n > b:
                c, b = b, n
            elif b > n > c:
                c = n
        return c if len(nums) >= 3 else a
