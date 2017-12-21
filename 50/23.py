# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
