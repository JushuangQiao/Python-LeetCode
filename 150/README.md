# LeetCode 101-150

144 [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
```Python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                root = t.right
        return ret
```

145 [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
```Python
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.right
            if stack:
                top = stack.pop()
                root = top.left
        return ret[::-1]
```
