# LeetCode 501-550

504 [Base 7](https://leetcode.com/problems/base-7/description/)
```python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        ret = ''
        n = abs(num)
        while n:
            ret += str(n % 7)
            n = n / 7
        return '-' + ret[::-1] if num < 0 else ret[::-1]
```

507 [Perfect Number](https://leetcode.com/problems/perfect-number/description/)
```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        from math import sqrt
        if num <= 3:
            return False
        tsum, end = 1, int(sqrt(num)) + 1
        for n in range(2, end):
            if num % n == 0:
                tsum += n + int(num / n)
            if tsum > num:
                return False
        return tsum == num
```

513 [Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/description/)
```python
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        d = deque()
        d.append(root)
        ret = root.val
        while d:
            node = d.popleft()
            ret = node.val
            if node.right:
                d.append(node.right)
            if node.left:
                d.append(node.left)
        return ret
```

515 [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)
```python
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        level = 0
        node = [[root, level]]
        while node:
            ret.append(max(map(lambda x:x[0].val, node)))
            level += 1
            while node and node[0][1] < level:
                tmp = node.pop(0)
                if tmp[0].left:
                    node.append([tmp[0].left, level])
                if tmp[0].right:
                    node.append([tmp[0].right, level])
        return ret
```

520 [Detect Capital](https://leetcode.com/problems/detect-capital/description/)
```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()
```

530 [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)
```python
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        def dfs(r):
            if r.left: dfs(r.left)
            ret.append(r.val)
            if r.right: dfs(r.right)
        dfs(root)
        return min([abs(ret[i]-ret[i+1]) for i in range(len(ret)-1)])
```

537 [Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/description/)
```python
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a.split('+'), b.split('+')
        a1, a2 = int(a[0]), int(a[1][:-1])
        b1, b2 = int(b[0]), int(b[1][:-1])
        c = a1 * b1 - a2 * b2
        d = a1 * b2 + a2 * b1
        return str(c) + '+' + str(d) +'i'
```

539 [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/description/)
```Python
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        ret = 100000
        length = len(t)
        for i in range(length - 1):
            poor = t[i+1] - t[i]
            if poor < ret:
                ret = poor
        last = t[-1] - t[0] if t[-1]-t[0] <= 720 else 1440 - (t[-1]-t[0])
        ret = last if last < ret else ret
        return ret
```
