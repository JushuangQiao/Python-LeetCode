# LeetCode 751-800

771 [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_hash = {c: True for c in J}
        ret = 0
        for c in S:
            if j_hash.get(c):
                ret += 1
        return ret
```
783 [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/)
```python
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)
        dfs(root)
        return min([ret[i] - ret[i-1] for i in range(1, len(ret))])
```

791 [Custom Sort String](https://leetcode.com/problems/custom-sort-string/description/)
```python
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_hash = {}
        t_hash = {}
        for c in T:
            t_hash[c] = t_hash.get(c, 0) + 1
        ret = []
        for c in S:
            if t_hash.get(c):
                ret.append(c * t_hash.get(c))
                del t_hash[c]
        for k in t_hash.keys():
            ret.append(k * t_hash[k])
        return ''.join(ret)
```
796 [Rotate String](https://leetcode.com/problems/rotate-string/description/)
```python
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in (A + A)
```
