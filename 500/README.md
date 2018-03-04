# LeetCode 451-500

476 [Number Complement](https://leetcode.com/problems/number-complement/description/)
```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(map(lambda x:'1' if x=='0' else '0', bin(num)[2:])), 2)
```

482 [License Key Formatting](https://leetcode.com/problems/license-key-formatting/description/)
```python
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S[::-1]
        ret = []
        leng = 0
        tmp = []
        for c in s:
            if c != '-':
                if leng == K:
                    ret.append(''.join(tmp))
                    leng = 1
                    tmp = [c.upper()]
                else:
                    tmp.append(c.upper())
                    leng += 1
        ret.append(''.join(tmp))
        return '-'.join(ret)[::-1]
```

485 [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/)
```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = tmp = 0
        for n in nums:
            if n:
                tmp += 1
            else:
                ret = max(tmp, ret)
                tmp = 0
        return max(ret, tmp)
```

492 [Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/description/)
```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        s = int(sqrt(area))
        while area % s != 0:
            s -= 1
        return [area/ s, s]
```

500 [Keyboard Row](https://leetcode.com/problems/keyboard-row/description/)
```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        return [word for word in words if any([set(word.lower()).issubset(row) for row in rows])]
```



