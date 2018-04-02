class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = {}
        for a in A:
            for b in B:
                AB[a+b] = AB.get(a+b, 0) + 1
        ret = 0
        for c in C:
            for d in D:
                if -c-d in AB:
                    ret += AB.get(-c-d)
        return ret
