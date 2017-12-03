# LeetCode 51-100

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


