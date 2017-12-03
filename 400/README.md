# LeetCode 350-400

367 [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)
```Python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = (left+right) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid -1
        return False
```


