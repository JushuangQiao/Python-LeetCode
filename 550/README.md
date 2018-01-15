# LeetCode 501-550

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
