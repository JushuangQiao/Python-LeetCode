# LeetCode 451-500

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



