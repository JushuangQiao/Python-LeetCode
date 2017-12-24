class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = (right - left) * (height[left] if height[left] <= height[right] else height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            cur = (right - left) * (height[left] if height[left] <= height[right] else height[right])
            water = cur if cur > water else water
        return water

