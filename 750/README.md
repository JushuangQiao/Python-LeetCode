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
