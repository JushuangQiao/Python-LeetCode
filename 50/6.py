class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for _ in range(numRows)]
        move, counts = 0, 0
        
        for c in s:
            if move == 0:
                rows[counts].append(c)
                counts += 1
                if counts == numRows:
                    move = 1
                    counts -= 2
            else:
                rows[counts].append(c)
                counts -= 1
                if counts < 0:
                    move = 0
                    counts += 2
        return ''.join([''.join(r) for r in rows])
