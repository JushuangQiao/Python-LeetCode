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
