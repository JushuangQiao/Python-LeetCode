# LeetCode 251-300

263 [Ugly Number](https://leetcode.com/problems/ugly-number/)
```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        return False
```

264 [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)
```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        t2 = t3 = t5 = 0
        while len(ugly) < n:
            while ugly[t2] * 2<= ugly[-1]:
                t2 += 1
            while ugly[t3]*3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] *5<= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5))
        return ugly[-1]
```