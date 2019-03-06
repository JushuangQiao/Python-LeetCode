# LeetCode 151-200

151 [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/submissions/)
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        return ' '.join(tmp[::-1])
```

165 [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)
```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        k1, k2 = 0, 0
        while k1 < len(v1) and k2 < len(v2):
            if int(v1[k1]) > int(v2[k2]):
                return 1
            if int(v1[k1]) < int(v2[k2]):
                return -1
            k1 += 1
            k2 += 1
        while k1 < len(v1):
            if int(v1[k1]):
                return 1
            k1 += 1
        while k2 < len(v2):
            if int(v2[k2]):
                return -1
            k2 += 1
        return 0
```

171 [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        track = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        for k, v in enumerate(s):
            ret += track[v] * 26 ** (len(s) - 1 - k)
        return ret
```

172 [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
```
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, carry = 0, 1
        while True:
            cnt = n / 5 ** carry
            if cnt == 0:
                return ret
            ret += cnt
            carry += 1
```
