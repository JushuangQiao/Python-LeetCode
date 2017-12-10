class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(n-1):
            c = start[0]
            nums = 0
            tmp = []
            for s in start:
                if s == c:
                    nums += 1
                else:
                    tmp.append([nums, c])
                    nums = 1
                    c = s
            tmp.append([nums, c])
            start = ''.join([str(d[0])+d[1] for d in tmp])
        return start
