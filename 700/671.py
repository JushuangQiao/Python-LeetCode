# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if not root:
            return -1
        stack = deque([root])
        ret = [root.val]
        while stack:
            node = stack.popleft()
            if node:
                if node.val > ret[-1]:
                    if len(ret) < 2:
                        ret.append(node.val)
                else:
                    if ret[0] < node.val < ret[1]:
                        ret[1] = node.val
                    stack.append(node.left)
                    stack.append(node.right)
        return ret[1] if len(ret) == 2 else -1
