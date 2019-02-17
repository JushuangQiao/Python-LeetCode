# LeetCode 101-150

105 [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
```
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        loc = inorder.index(preorder[0])
        left, right = inorder[0:loc], inorder[loc+1:]
        root.left = self.buildTree(preorder[1:len(left)+1], left)
        root.right = self.buildTree(preorder[len(left)+1:] ,right)
        return root
```

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
