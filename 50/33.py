class Solution(object):

    def find_min(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            if right - left == 1:
                return right
            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid
            if nums[right] >= nums[mid]:
                right = mid
        return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        min_index = self.find_min(nums)
        if nums[min_index] == target:
            return min_index
        elif nums[min_index] > target:
            return -1
        else:
            left = self.search_t(nums, 0, min_index, target)
            right = self.search_t(nums, min_index, len(nums)-1, target)
            if left >= 0:
                return left
            if right >= 0:
                return right
        return -1

    def search_t(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
