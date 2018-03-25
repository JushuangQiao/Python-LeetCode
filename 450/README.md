# LeegtCode 401-450

450 [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/description/)
```python
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            left, right = root.left, root.right
            root = left
            while left and left.right:
                left = left.right
            if left:
                left.right = right
            else:
                root = right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
```
