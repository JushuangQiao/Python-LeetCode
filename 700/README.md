# LeetCode 650-700

654 [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/description/)
```Python
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_value = max(nums)
        max_index = nums.index(max_value)
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root
```

657 [Judge Route Circle](https://leetcode.com/problems/judge-route-circle/description/)
```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        row = col = 0
        for s in moves:
            if s == 'U':
                col += 1
            elif s == 'D':
                col -= 1
            elif s == 'L':
                row -= 1
            elif s == 'R':
                row += 1
            else:
                pass
        if row == 0 and col == 0:
            return True
        return False
```

671 [Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/)
```Python
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if not root:
            return -1
        stack = deque([root])
        ret = [root.val]
        while stack:
            node = stack.popleft()
            if node:
                if node.val > ret[-1]:
                    if len(ret) < 2:
                        ret.append(node.val)
                else:
                    if ret[0] < node.val < ret[1]:
                        ret[1] = node.val
                    stack.append(node.left)
                    stack.append(node.right)
        return ret[1] if len(ret) == 2 else -1
```

674 [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)
```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, tmp = 0, 0
        pre = float('-inf')
        for n in nums:
            if n > pre:
                tmp += 1
            else:
                ret = max(ret, tmp)
                tmp = 1
            pre = n
        return max(ret, tmp)
```

680 [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)
```Python
class Solution(object):

    def isPalindrome(self, s, left, right, flag):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if flag == 1:
                    return False
                flag = 1
                return (self.isPalindrome(s, left+1, right, flag) or
                        self.isPalindrome(s, left, right-1, flag))
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s)-1, 0)
```

693 [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)
```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n % 2
        n = n >> 1
        while n:
            t = n % 2
            if t == a:
                return False
            a = t
            n = n >> 1
        return a != n
```


