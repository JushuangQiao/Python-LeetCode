class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) / 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                if mid < 1 or (mid >= 1 and letters[mid-1] <= target):
                    return letters[mid]
                right = mid - 1
        return letters[0]
