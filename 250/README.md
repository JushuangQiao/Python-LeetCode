# LeetCode 201-250

204 [Count Primes](https://leetcode.com/problems/count-primes/)
```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        tmp = [1] * n
        tmp[0] = tmp[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if tmp[i]:
                for j in range(2, (n - 1)/i+1):
                    tmp[i*j] = 0
        return sum(tmp)
```

206 []()
```
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            n, head.next = head.next, pre
            pre, head = head, n
        return pre
```

226 [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)
```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```

237 [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)
```python
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node.next
        node.next, node.val = p.next, p.val
```

240 [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        start = 0
        while rows >= 0 and cols >= start:
            if matrix[rows][start] == target:
                return True
            elif matrix[rows][start] > target:
                rows -= 1
            else:
                start += 1
        return False
```