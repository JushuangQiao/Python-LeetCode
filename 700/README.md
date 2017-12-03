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


