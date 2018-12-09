# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        move, count = head, 0
        while move:
            count += 1
            move = move.next
        if count < k:
            return head
        move, current_count, current_last = head, 0, head
        move_pre = None
        while current_count < k:
            m_next = move.next
            move.next, move_pre = move_pre, move
            move = m_next
            current_count += 1
        current_last.next = self.reverseKGroup(move, k)
        return move_pre
