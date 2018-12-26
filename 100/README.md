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


