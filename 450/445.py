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
