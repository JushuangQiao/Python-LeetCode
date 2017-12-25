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

6 [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/description/)
```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for _ in range(numRows)]
        move, counts = 0, 0
        
        for c in s:
            if move == 0:
                rows[counts].append(c)
                counts += 1
                if counts == numRows:
                    move = 1
                    counts -= 2
            else:
                rows[counts].append(c)
                counts -= 1
                if counts < 0:
                    move = 0
                    counts += 2
        return ''.join([''.join(r) for r in rows])
```

7 [Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        t = abs(x)
        while t:
            ret = 10 * ret + t % 10
            t /= 10
        if ret > 2 ** 31 or -ret < -2 ** 31:
            return 0
        return ret if x >= 0 else -ret
```

8 [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/)
```python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = ''
        for i in str.strip():
            if i == '-' or i == '+' or i.isdigit():
                if '-' not in s or '+' not in s:
                    s += i
            else:
                break
        try:
            ret = int(s)
            if ret >= -2147483648 and ret <= 2147483647:
                return ret
            elif ret < -2147483648:
                return -2147483648
            elif ret > 2147483647:
                return 2147483647
            else:
                return 0
        except:
            return 0
```

9 [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        r = 0
        t = x
        while t:
            r = r * 10 + t % 10
            t /= 10
        return r == x
```

11 [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = (right - left) * (height[left] if height[left] <= height[right] else height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            cur = (right - left) * (height[left] if height[left] <= height[right] else height[right])
            water = cur if cur > water else water
        return water
```

14 [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        pre = strs[0]
        for s in strs:
            len_pre = len(pre)
            while s[0:len_pre] != pre:
                len_pre -= 1
                pre = pre[0:len_pre]
                if not pre:
                    return pre
        return pre
```

19 [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        move = head
        while move:
            stack.append(move)
            move = move.next
        if len(stack) == n:
            return head.next
        if n == 1:
            stack[-n-1].next = None
        else:
            stack[-n-1].next = stack[-n+1]
            stack[-n].next = None
        return head
```

20 [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
```

21 [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)
```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ret = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        while l1:
            pre.next = l1
            l1 = l1.next
            pre = pre.next
        while l2:
            pre.next = l2
            l2, pre = l2.next, pre.next
        return ret.next
```

23 [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        min_heap = []
        ret = head = ListNode(0)
        for k, link in enumerate(lists):
            if link:
                heapq.heappush(min_heap, [link.val, link])
        while min_heap:
            cur = heapq.heappop(min_heap)
            ret.next = cur[-1]
            ret = ret.next
            if ret.next:
                heapq.heappush(min_heap, [ret.next.val, ret.next])
        return head.next
```

24 [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = m_pre = ListNode(0)
        pre.next = head
        while head and head.next:
            hn = head.next
            hnn = hn.next
            pre.next, hn.next, head.next = hn, head, hnn
            pre, head = head, hnn
        return m_pre.next
```

26 [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = ret = 0
        cur = None
        while left < len(nums):
            if nums[left] != cur:
                nums[ret] = nums[left]
                ret += 1
                cur = nums[left]
            left += 1
        return ret
```

27 [Remove Element](https://leetcode.com/problems/remove-element/description/)
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left
```

28 [Implement strStr()](https://leetcode.com/problems/implement-strstr/description/)
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
```

33 [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
```python
class Solution(object):

    def find_min(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            if right - left == 1:
                return right
            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid
            if nums[right] >= nums[mid]:
                right = mid
        return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        min_index = self.find_min(nums)
        if nums[min_index] == target:
            return min_index
        elif nums[min_index] > target:
            return -1
        else:
            left = self.search_t(nums, 0, min_index, target)
            right = self.search_t(nums, min_index, len(nums)-1, target)
            if left >= 0:
                return left
            if right >= 0:
                return right
        return -1

    def search_t(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

34 [Search for a Range](https://leetcode.com/problems/search-for-a-range/description/)
```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left(nums, target), self.search_right(nums, target)]
    
    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid+1] > target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

35 [Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        mid = (left + right) / 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) / 2
        if nums[mid] > target:
            return mid - 1 if mid > 0 else 0
        return mid + 1
```

38 [Count and Say](https://leetcode.com/problems/count-and-say/description/)
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(n-1):
            c = start[0]
            nums = 0
            tmp = []
            for s in start:
                if s == c:
                    nums += 1
                else:
                    tmp.append([nums, c])
                    nums = 1
                    c = s
            tmp.append([nums, c])
            start = ''.join([str(d[0])+d[1] for d in tmp])
        return start
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

