# LeetCode 51-100

53 [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_val, cur_sum = nums[0], float('-inf')
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_val = max(max_val, cur_sum)
        return max_val
```

58 [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for c in s.strip()[::-1]:
            if c == ' ':
                break
            ret += 1
        return ret
```
94 [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
```Python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                ret.append(t.val)
                root = t.right
        return ret
```


