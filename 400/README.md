# LeetCode 350-400

367 [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)
```Python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = (left+right) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid -1
        return False
```

394 [Decode String](https://leetcode.com/problems/decode-string/description/) (30ms beat 98%)
```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums, chars = [], []
        i, length = 0, len(s)
        while i < length:
            j = i + 1
            if s[i].isdigit():
                num = int(s[i])
                while j < length:
                    if s[j].isdigit():
                        num = num * 10 + int(s[j])
                        j += 1
                    else:
                        break
                nums.append(num)
            elif s[i] == '[' or s[i].isalpha():
                chars.append(s[i])
            else:
                t, tmpc = chars.pop(), []
                while t != '[':
                    tmpc.append(t)
                    t = chars.pop()
                tchars = nums.pop() * ''.join(tmpc[::-1])
                chars.append(tchars)
            i = j
        return ''.join(chars)
```

400 [Nth Digit](https://leetcode.com/problems/nth-digit/description/)
```python
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        for d in range(1, 10):
            if d * 9 * (10 ** (d - 1)) >= n:
                digit = d
                break
        num = 0
        for d in range(1, digit + 1):
            num += int(9 * (d - 1) * 10 ** (d - 2))
        ret = (n - num - 1) / digit + 10 ** (digit-1)
        return int(str(ret)[(n - num - 1) % digit])
```

