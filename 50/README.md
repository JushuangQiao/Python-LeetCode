# LeetCode 1-50

1 [Two Sum](https://leetcode.com/problems/two-sum/description/)
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for k, v in enumerate(nums):
            if target - v in dicts:
                return [dicts.get(target-v), k]
            dicts[v] = k
```

2 [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)
```Python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = b = 0
        carry = 0
        while l1:
            a += l1.val * 10 ** carry
            carry += 1
            l1 = l1.next
        carry = 0
        while l2:
            b += l2.val * 10 ** carry
            carry += 1
            l2 = l2.next
        ret = a + b
        h = m = ListNode(0)
        if not ret:
            return h
        while ret:
            m.next = ListNode(ret % 10)
            ret /= 10
            m = m.next
        return h.next
```

3 [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
```Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashes = {}
        left, right, length = 0, 0, len(s)
        max_len = 0
        while right < length:
            if hashes.get(s[right]) and hashes[s[right]] >= left:
                left = hashes[s[right]]
            hashes[s[right]] = right + 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
```

46 [Permutations](https://leetcode.com/problems/permutations/description/)
```Python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(permutations(nums))
```

47 [Permutations II](https://leetcode.com/problems/permutations-ii/description/)
```Python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(set(permutations(nums)))
```

48 [Rotate Image](https://leetcode.com/problems/rotate-image/description/)
```Python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = 0
        while m <= n / 2:
            k = m
            while k < n - 1 - m:
                matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k], matrix[n-1-k][m] = \
                    matrix[n-1-k][m], matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k]
                k += 1
            m += 1
```

49 [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)
```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            ts = ''.join(sorted(s))
            if ret.get(ts):
                ret[ts].append(s)
            else:
                ret[ts] = [s]
        return ret.values()
```

50 [Pow(x, n)](https://leetcode.com/problems/powx-n/description/)
```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n
```

