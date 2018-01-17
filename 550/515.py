# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        level = 0
        node = [[root, level]]
        while node:
            ret.append(max(map(lambda x:x[0].val, node)))
            level += 1
            while node and node[0][1] < level:
                tmp = node.pop(0)
                if tmp[0].left:
                    node.append([tmp[0].left, level])
                if tmp[0].right:
                    node.append([tmp[0].right, level])
        return ret
