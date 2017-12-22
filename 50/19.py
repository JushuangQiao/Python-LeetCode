# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
