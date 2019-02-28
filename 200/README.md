# LeetCode 150-200

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
