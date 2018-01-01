# LeetCode 601-650

606 [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/)
```python
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        root = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if right:
            return root + '(' + left + ')(' + right + ')'
        else:
            if left:
                return root + '(' + left + ')'
            else:
                return root
```

617 [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/description/)
```python
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        root = TreeNode(t1.val+t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root
```

633 [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/description/)
```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        for i in range(int(sqrt(c))+1):
            if (int(sqrt(c-i**2))) ** 2 + i ** 2 == c:
                return True
        return False
```
