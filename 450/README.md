# LeegtCode 401-450

404 [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/)
```python
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.sum_of_left(root.left, True) + self.sum_of_left(root.right, False)
    
    def sum_of_left(self, root, is_left):
        if not root:
            return 0
        if root and not root.left and not root.right:
            return root.val if is_left else 0
        return self.sum_of_left(root.left, True) + self.sum_of_left(root.right, False)
```

409 [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/)
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict = {}
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        ret, remain = 0, 0
        for k in sdict.keys():
            if sdict[k] % 2 == 0:
                ret += sdict[k]
            else:
                ret += (sdict[k] - 1)
                remain = 1
        return ret + remain
```

412 [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/)
```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [(not i % 3)*'Fizz' + (not i % 5)*'Buzz' or str(i) for i in range(1, n+1)]
```

414 [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/description/)
415 [Add Strings](https://leetcode.com/problems/add-strings/description/)
```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        min_len = len(num1) if len(num1) < len(num2) else len(num2)
        max_len = len(num1) if len(num1) > len(num2) else len(num2)
        ret, carry, digit = '', 0, -1
        if len(num1) <= len(num2):
            num1 = '0' * (max_len - min_len) + num1
        else:
            num2 = '0' * (max_len - min_len) + num2
        while digit >= -max_len:
            n1 = ord(num1[digit]) - ord('0')
            n2 = ord(num2[digit]) - ord('0')
            ret += str((n1 + n2 + carry) % 10)
            carry = (n1 + n2 + carry) / 10
            digit -= 1
        if carry != 0:
            ret += str(carry)
        return ret[::-1]
```

434 [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/description/)
```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
```

441 [Arranging Coins](https://leetcode.com/problems/arranging-coins/description/)
```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((2 + 8*n) ** 0.5 - 1) / 2) 
```

442 [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)
```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                ret.append(abs(n))
            else:
                nums[abs(n) - 1] = -nums[abs(n) - 1]
        return ret
```

445 [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/description/)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        from collections import deque
        l1_vals, l2_vals = deque(), deque()
        while l1 and l2:
            l1_vals.append(l1.val)
            l2_vals.append(l2.val)
            l1, l2 = l1.next, l2.next
        while l1:
            l1_vals.append(l1.val)
            l1 = l1.next
        while l2:
            l2_vals.append(l2.val)
            l2 = l2.next
        ret, carry = deque(), 0
        while l1_vals and l2_vals:
            val = l1_vals.pop() + l2_vals.pop() + carry
            ret.append(ListNode(val % 10))
            carry = val / 10
        while l1_vals:
            val = l1_vals.pop() + carry
            ret.append(ListNode(val % 10))
            carry = val / 10
        while l2_vals:
            val = l2_vals.pop() + carry
            ret.append(ListNode(val % 10))
            carry = val / 10
        h = head = ListNode(0)
        if carry:
            h.next, h = ListNode(carry), h.next
        while ret:
            h.next = ret.pop()
            h = h.next
        return head.next
```

448 [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            t = abs(n) - 1
            nums[t] = -abs(nums[t])
        return [k + 1 for k, v in enumerate(nums) if v > 0]
```        

450 [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/description/)
```python
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            left, right = root.left, root.right
            root = left
            while left and left.right:
                left = left.right
            if left:
                left.right = right
            else:
                root = right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
```
