# LeetCode 451-500

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



