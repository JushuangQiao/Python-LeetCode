class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        t2 = t3 = t5 = 0
        while len(ugly) < n:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5))
        return ugly[-1]