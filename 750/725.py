# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
