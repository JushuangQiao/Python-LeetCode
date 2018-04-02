# LeetCode 451-500

451 [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/description/)
```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        return ''.join([i[0]*i[1] for i in c.most_common()])
```

454 [4Sum II](https://leetcode.com/problems/4sum-ii/description/)
```python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = {}
        for a in A:
            for b in B:
                AB[a+b] = AB.get(a+b, 0) + 1
        ret = 0
        for c in C:
            for d in D:
                if -c-d in AB:
                    ret += AB.get(-c-d)
        return ret
```

455 [Assign Cookies](https://leetcode.com/problems/assign-cookies/description/)
```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
```

461 [Hamming Distance](https://leetcode.com/problems/hamming-distance/description/)
```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
```

468 [Validate IP Address](https://leetcode.com/problems/validate-ip-address/description/)
```python
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_ipv4(ip):
            sub = ip.split('.')
            for s in sub:
                if not s.isdigit() or (len(s) != len(str(int(s)))) or not (0 <= int(s) <= 255) :
                    return False
            return len(sub) == 4
        
        def is_ipv6(ip):
            sub = ip.split(':')
            for s in sub:
                if len(s) > 4 or not ('0' <= s.upper() <= 'FFFF'):
                    return False
            return len(sub) == 8
        
        if is_ipv4(IP):
            return 'IPv4'
        if is_ipv6(IP):
            return 'IPv6'
        return 'Neither'
```

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



