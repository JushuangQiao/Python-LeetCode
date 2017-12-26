# LeetCode 701-750
[724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/description/)
```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = sum(nums)
        left = 0
        for k, v in enumerate(nums):
            if left * 2 + v == ret:
                return k
            left += v
        return -1
```

[725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/description/)
```Python
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ret = [None] * k
        length, move = 0, root
        while move:
            length += 1
            move = move.next
        avg, rem = length / k, length % k
        move, indexs = root, 0
        while move:
            tmp = move
            pre = ListNode(0)
            pre.next = move
            num = 0
            while num < avg:
                pre, move = pre.next, move.next
                num += 1
            if rem:
                pre, move = pre.next, move.next
                rem -= 1
            pre.next = None
            ret[indexs] = tmp
            indexs += 1
        return ret
```

[728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/description/)
```Python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            val = i
            flag = 1
            while i:
                remain = i % 10
                if not remain or val % remain != 0:
                    flag = 0
                    break
                i /= 10
            if flag:
                ret.append(val)
        return ret
```

744 [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)
```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) / 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                if mid < 1 or (mid >= 1 and letters[mid-1] <= target):
                    return letters[mid]
                right = mid - 1
        return letters[0]
```

747 [Largest Number Greater Than Twice of Others](https://leetcode.com/problems/largest-number-greater-than-twice-of-others/description/)
```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        a, b = [nums[0], 0], [nums[1], 1]
        if b[0] > a[0]:
            a, b = b, a
        for k, v in enumerate(nums):
            if k < 2:
                continue
            if b[0] < v < a[0]:
                b = [v, k]
            elif v >= a[0]:
                a, b = [v, k], a
            else:
                pass
        return a[1] if a[0] >= b[0] * 2 else -1
```
