# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = self.get_length()

    def get_length(self):
        length, head = 0, self.head
        while head:
            length += 1
            head = head.next
        return length

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        num = random.choice(range(0, self.length))
        head = self.head
        while num:
            head = head.next
            num -= 1
        return head.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# -*- coding: utf-8 -*-
