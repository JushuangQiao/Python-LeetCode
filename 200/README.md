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
