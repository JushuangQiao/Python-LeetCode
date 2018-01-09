# LeetCode 501-550

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
