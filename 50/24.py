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
