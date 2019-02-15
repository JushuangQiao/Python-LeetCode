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

54 [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix[0]) == 0:
            return []
        ret = []
        start, m, n = 0, len(matrix), len(matrix[0])
        while start * 2 < m and start * 2 < n:
            col = row = start
            # left -> right
            while col < n - start:
                ret.append(matrix[row][col])
                col += 1
            # top -> bottom
            if m - 2 * start > 1 and row < m - start:
                row += 1
                col -= 1
                while row < m - start:
                    ret.append(matrix[row][col])
                    row += 1
            # right -> left
            if m - 2 * start > 1 and n - 2 * start > 1 and col >= start:
                col -= 1
                row -= 1
                while col >= start:
                    ret.append(matrix[row][col])
                    col -= 1
            # bottom -> top
            if m - 2 * start > 1 and n - 2 * start > 1 and row > start:
                row -= 1
                col += 1
                while row > start:
                    ret.append(matrix[row][col])
                    row -= 1
            start += 1
        return ret
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

59 [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for i in range(n)] for j in range(n)]
        v, start = 1, 0
        while start * 2 < n:
            col = row = start
            # left -> right
            while col < n - start:
                ret[row][col] = v
                col += 1
                v += 1
            # top -> bottom
            if n - 2 * start > 1 and row < n - start:
                row += 1
                col -= 1
                while row < n - start:
                    ret[row][col] = v
                    row += 1
                    v += 1
            # right -> left
            if n - 2 * start > 1 and n - 2 * start > 1 and col >= start:
                col -= 1
                row -= 1
                while col >= start:
                    ret[row][col] = v
                    col -= 1
                    v += 1
            # bottom -> top
            if n - 2 * start > 1 and n - 2 * start > 1 and row > start:
                row -= 1
                col += 1
                while row > start:
                    ret[row][col] = v
                    v += 1
                    row -= 1
            start += 1
        return ret
```

74 [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        while rows > 0:
            if matrix[rows - 1][0] < target:
                return self.bin_search(matrix[rows - 1], target)
            elif matrix[rows - 1][0] == target:
                return True
            else:
                rows -= 1
        return False

    def bin_search(self, data, target):
        """
        :type data: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(data)
        while low < high:
            mid = low + (high - low) / 2
            if data[mid] == target:
                return True
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid
        return False
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

98 [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = []

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            ret.append(root.val)
            in_order(root.right)
        in_order(root)
        leng = len(ret)
        for k in range(leng - 1):
            if ret[k] >= ret[k + 1]:
                return False
        return True
```

99 [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)
```
class Solution(object):

    def __init__(self):
        self.first = None
        self.second = None
        self.pre = TreeNode(float('-inf'))

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder_traversal(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        if not self.first and root.val <= self.pre.val:
            self.first = self.pre
        if self.first and root.val <= self.pre.val:
            self.second = root
        self.pre = root
        self.inorder_traversal(root.right)
```

100 [Same Tree](https://leetcode.com/problems/same-tree/)
```python
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```
